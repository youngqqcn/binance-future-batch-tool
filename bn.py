#coding:utf8


# api: 8pIn3CxgkJ2m4k98i1CfZQdc6wXYmt0uzxrvfRxXuBEqljJT0TZhypz3F9WYYf2V


from pprint import pprint
from binance.spot import Spot
from binance.cm_futures import CMFutures
import logging
from binance.um_futures import UMFutures
from binance.lib.utils import config_logging
from binance.error import ClientError

config_logging(logging, logging.DEBUG)


class  BnUmWrapper(object):
    """币安U本位合约封装"""

    def __init__(self, apiKey, secretKey):
        # U本位合约
        self.um_futures_client = UMFutures(key=apiKey, secret=secretKey)
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
            ret = self.um_futures_client.change_margin_type(symbol=symbol, marginType='ISOLATED')
            return True
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )
            return False

    def getTokenBalance(self, token: str):
        """获取指定代币的余额"""

        if 'USDT' in token:
            token = token.replace('USDT', '')

        # Get account and balance information
        ret = self.um_futures_client.balance()
        for x in ret:
            if x['asset'] == token:
                return float(x['balance'])
        pass

    def getPrecision(self, symbol):
        """获取精度, 返回数量精度，价格精度"""

        exInfo = self.um_futures_client.exchange_info()
        for x in exInfo['symbols']:
            if x['symbol'] == symbol:
                quantityPrecision = int(x['quantityPrecision'])
                pricePrecision = int(x['pricePrecision'])
                return quantityPrecision, pricePrecision
        raise Exception("not found symbol: {}".format(symbol))

    def changeLeverage(self, leverage: int):
        # 调整杠杆模式
        try:
            ret = self.um_futures_client.change_leverage(symbol='RENUSDT', leverage=leverage)
            logging.info("调整杠杆倍数： {}, 成功".format(ret))
        except ClientError as error:
             logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
        )
        pass

    def getLatestPrice(self, symbol):
         # 获取最新价格，来计算下单数量, 不用标记价格
        ret = self.um_futures_client.ticker_price(symbol=symbol)
        latestPrice = float(ret['price'])
        logging.info(latestPrice)
        return latestPrice


    def createOrders(self, usdtQuantity: float, symbol: str , side: str ):
        """创建新订单"""

        assert usdtQuantity > 5  , '无效参数, usdtQuantity'
        assert side in ['BUY', 'SELL'], '无效参数 side'
        assert  'USDT' in symbol and len(symbol) > 5 , '无效参数 symbol'

        try:
            latestPrice = self.getLatestPrice(symbol=symbol)

            qp, pp = self.getPrecision(symbol=symbol)
            tokenQuantity = usdtQuantity/latestPrice

            quantity = f"%.{qp}f"%tokenQuantity

            stopPrice = f"%.{pp}f"%(latestPrice * (1 - 0.05)) # 要乘以杠杆倍数
            logging.info("stopPrice ===> {}".format(stopPrice))
            logging.info( 'tokenQuantity============>{}'.format( tokenQuantity))


            orders = [
                # 市价下单
                {
                    "symbol":   "RENUSDT",
                    "side":     "BUY",   # BUY:买入开多，SELL:卖出开空
                    "type":     "MARKET", # MARKET 市价单
                    "quantity": quantity,  # 币的数量
                },

                # 市价止损单
                {
                    "symbol":           "RENUSDT",
                    "side":             "SELL",
                    "type":             "STOP_MARKET", # STOP_MARKET 市价止盈/损单
                    "stopPrice":        stopPrice,  # 触发价格
                    "closePosition":    "true",  # 触发后，全部平仓
                    "workingType":      "MARK_PRICE" # 按标记价格止损
                },
            ]

            response = self.um_futures_client.new_batch_order(batchOrders=orders)
            logging.info(response)
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )
        pass



def main():

    apiKey = '8pIn3CxgkJ2m4k98i1CfZQdc6wXYmt0uzxrvfRxXuBEqljJT0TZhypz3F9WYYf2V'
    secretKey = 'rE6uFZxkmROfhT1hXuFdu00BTTsDYEJ8WoIWyxZ8UIeTiVdvvYJr4HA2xuJaJD1m'
    bn =  BnUmWrapper(apiKey=apiKey, secretKey=secretKey)

    print( bn.getAccountBalance(symbol='USDT') )
    pass

if __name__ == '__main__':
    main()
