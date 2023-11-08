#coding:utf8
#author:yqq
#date: 2023-11-3

from pprint import pprint
# from binance.spot import Spot
# from binance.cm_futures import CMFutures
import logging
from binance.um_futures import UMFutures
from binance.lib.utils import config_logging
from binance.error import ClientError

config_logging(logging, logging.INFO)


class  BnUmWrapper(object):
    """币安U本位合约封装"""

    def __init__(self, apiKey, secretKey):
        # U本位合约
        self.um_futures_client = UMFutures(key=apiKey, secret=secretKey)


        # 获取交易信息
        self.exchangeInfo = None # self.um_futures_client.exchange_info()
        pass


    def ping(self):
        try:
            self.um_futures_client.ping()
            return True
        except ClientError as error:
            return False

    def changePositionMode(self):
        try:
            self.um_futures_client.change_position_mode(dualSidePosition="false")
            return True
        except ClientError as error:
            return False


    def changeMarginTypeToIsolated(self, symbol):
        """切换到 “逐仓”模式"""
        try:
            self.um_futures_client.change_margin_type(symbol=symbol, marginType='ISOLATED')
            return True
        except ClientError as error:

            # 如果已经是逐仓模式，则忽略
            if error.error_code == -4046:
                return True

            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )
            return False

    def getTokenBalance(self, token: str):
        """获取指定代币的余额"""

        # Get account and balance information
        ret = self.um_futures_client.balance()
        # logging.info(ret)

        for x in ret:
            if x['asset'] == token:
                return float(x['balance']), float(x['availableBalance'])
        return 0, 0

    def getPrecision(self, symbol):
        """获取精度, 返回数量精度，价格精度"""

        if self.exchangeInfo == None:
            self.exchangeInfo = self.um_futures_client.exchange_info()

        for x in self.exchangeInfo['symbols']:
            if x['symbol'] == symbol:
                quantityPrecision = int(x['quantityPrecision'])
                pricePrecision = int(x['pricePrecision'])
                return quantityPrecision, pricePrecision
        raise Exception("not found symbol: {}".format(symbol))



    def changeLeverage(self, symbol: str,  leverage: int):
        # 调整杠杆倍数, 如果有逐仓仓位，不能降低杠杆
        positions = self.getCurrentPosition()
        curLeverage = 1

        for x in positions:
            if x['symbol'] == symbol:
                curLeverage = int(x['leverage'])  # 杠杆倍数，只搞整数
                if leverage < curLeverage:
                    raise Exception("逐仓模式不能降低杠杆倍数, 如需降低杠杆倍数，请先平仓，然后重新建仓")
                break
        return self.um_futures_client.change_leverage(symbol=symbol, leverage=leverage)


    def getLatestPrice(self, symbol):
         # 获取最新价格，来计算下单数量, 不用标记价格
        ret = self.um_futures_client.ticker_price(symbol=symbol)
        latestPrice = float(ret['price'])
        logging.info(latestPrice)
        return latestPrice

    def checkSingleSidePositionSide(self):
        """检查是否是单向持仓"""

        ret = self.um_futures_client.get_position_mode()
        if ret['dualSidePosition'] == False:
            return True
        return False


    def createNewOrders(self, usdtQuantity: float, symbol: str , side: str, stopRatio: float, leverage: int ):
        """
        创建新订单
        Args:
            usdtQuantity (float): usdt数量,会自动换算成币的数量( 实际仓位 = usdt数量 * 杠杆倍数 / 币价)
            symbol (str): 交易对, 例如: BTCUSDT
            side (str):  下单方向, 开多: BUY  ;  开空: SELL
            stopRatio (float):  市价止损单,价格浮动百分比, 达到这个价格就市价止损
            leverage (int): 杠杆倍数
        """


        assert usdtQuantity * leverage > 10  , '无效参数, usdtQuantity {}'.format(usdtQuantity)
        assert side in ['BUY', 'SELL'], '无效参数 side {}'.format(side)
        assert  'USDT' in symbol and len(symbol) > 5 , '无效参数 symbol, {}'.format(symbol)
        assert 0 < stopRatio < 0.99, '无效止损： {}'.format(stopRatio)
        assert 1 <= leverage <= 99 , '无效杠杆倍数: {}'.format(leverage)

        # 调整杠杆倍数
        self.changeLeverage(symbol=symbol, leverage=leverage)

        latestPrice = self.getLatestPrice(symbol=symbol)

        qp, pp = self.getPrecision(symbol=symbol)

        # 下单的数量，币的数量
        tokenQuantity = (usdtQuantity * leverage) / latestPrice
        quantity = f"%.{qp}f"%tokenQuantity
        logging.info('quantity=====>{}'.format( quantity))

        # 止损市价单的触发价格
        stopPrice = latestPrice
        if side == 'BUY':   # 开多
            stopPrice = latestPrice * (1 - stopRatio/leverage)
        else: # SELL  开空
            stopPrice = latestPrice * (1 + stopRatio/leverage)
        stopPrice = f"%.{pp}f"%stopPrice # 要乘以杠杆倍数

        logging.info("stopPrice ===> {}".format(stopPrice))


        # 止损方向
        stopSide = 'BUY' if side == 'SELL' else 'SELL'
        assert stopSide != side

        orders = [
            # 市价下单
            {
                "symbol":   symbol,
                "side":     side,   # BUY:买入开多，SELL:卖出开空
                "type":     "MARKET", # MARKET 市价单
                "quantity": quantity,  # 币的数量
            },

            # 市价止损单
            {
                "symbol":           symbol,
                "side":             stopSide,
                "type":             "STOP_MARKET", # STOP_MARKET 市价止盈/损单
                "stopPrice":        stopPrice,  # 触发价格
                "closePosition":    "true",  # 触发后，全部平仓
                "workingType":      "MARK_PRICE" # 按标记价格止损
            },
        ]

        response = self.um_futures_client.new_batch_order(batchOrders=orders)
        logging.info(response)
        return response




    def closeAllPositionMarket(self):
        """市价全部平仓"""

        # 确保是单向持仓模式
        if not self.checkSingleSidePositionSide():
            raise Exception("仅支持单向持仓模式的 一键全部市价平仓")

        closePositionsOrders = []
        # 获取当前所有仓位
        positions = self.getCurrentPosition()
        if len(positions) == 0:
            return
        logging.info('当前仓位:{}'.format(positions))

        for pos in positions:
            closeSide = 'BUY' if pos['side'] == 'SELL' else 'SELL'

            # 空单的仓位量是负数
            quantity = str(pos['positionAmt']).replace('-', '')

            # 反向单
            order = {
                "symbol":           pos['symbol'],
                "side":             closeSide,
                "type":             "MARKET", # MARKET 市价平仓
                "quantity":         quantity,  # 币的数量
            }

            closePositionsOrders.append(order)

            # 最多5个
            if len(closePositionsOrders) >= 5:
                self.um_futures_client.new_batch_order(batchOrders=closePositionsOrders)
                closePositionsOrders = []

        if len(closePositionsOrders) > 0:
            self.um_futures_client.new_batch_order(batchOrders=closePositionsOrders)
        pass


    def getCurrentPosition(self):
        """获取当前仓位信息"""
        poss = []
        positions = self.um_futures_client.get_position_risk()
        for x in positions:
            # positionAmt 小于0则是空单; 大于0是多单
            if float(x['positionAmt']) != 0:
                x['side'] = 'SELL' if float(x['positionAmt']) < 0 else 'BUY'   # SELL:空单 ， BUY: 多单
                poss.append(x)
        return poss

    def getOpenOrders(self):
        """获取当前所有委托单"""
        ret = self.um_futures_client.get_orders()
        return ret



    def cancelAllOrders(self):
        """撤销所有委托单"""
        logging.info("撤销所有委托单")
        orders = self.um_futures_client.get_orders()
        symbols = set()
        for x in orders:
            symbols.add(x['symbol'])

        for x in symbols:
            self.um_futures_client.cancel_open_orders(symbol=x)




def main():

    apiKey = '8pIn3CxgkJ2m4k98i1CfZQdc6wXYmt0uzxrvfRxXuBEqljJT0TZhypz3F9WYYf2V'
    secretKey = 'rE6uFZxkmROfhT1hXuFdu00BTTsDYEJ8WoIWyxZ8UIeTiVdvvYJr4HA2xuJaJD1m'
    bn =  BnUmWrapper(apiKey=apiKey, secretKey=secretKey)

    # print( bn.getAccountBalance(symbol='USDT') )
    print('==================')
    # pprint(bn.getPrecision('BTCUSDT'))
    pprint(bn.um_futures_client.exchange_info())

    # pprint(bn.createNewOrders(5.5, 'RENUSDT', 'SELL', 0.05, 2))
    # pprint(bn.getCurrentPosition())
    # pprint(bn.getOpenOrders())
    # pprint(bn.changeMarginTypeToIsolated('RENUSDT'))
    # pprint(bn.changeLeverage(symbol='RENUSDT', leverage=2))
    # pprint(bn.closeAllPositionMarket())
    # pprint(bn.cancelAllOrders())

    pass

if __name__ == '__main__':
    main()
