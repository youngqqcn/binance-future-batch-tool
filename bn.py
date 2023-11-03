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



def main():


    # U本位合约账户
    um_futures_client = UMFutures(key='8pIn3CxgkJ2m4k98i1CfZQdc6wXYmt0uzxrvfRxXuBEqljJT0TZhypz3F9WYYf2V',
                  secret='rE6uFZxkmROfhT1hXuFdu00BTTsDYEJ8WoIWyxZ8UIeTiVdvvYJr4HA2xuJaJD1m')

    # Get account and balance information
    # pprint(um_futures_client.balance(recvWindow=6000))


    # 默认是 单向持仓
    # ret = um_futures_client.change_position_mode(dualSidePosition="false")
    # logging.info(ret)


    # 切换到 “逐仓”模式
    # try:
    #     ret = um_futures_client.change_margin_type(symbol='RENUSDT', marginType='ISOLATED')
    # except ClientError as error:
    #      logging.error(
    #         "Found error. status: {}, error code: {}, error message: {}".format(
    #             error.status_code, error.error_code, error.error_message
    #         )
    #     )



    # 调整杠杆模式
    # try:
    #     ret = um_futures_client.change_leverage(symbol='RENUSDT', leverage=2)
    #     logging.info("调整杠杆倍数： {}".format(ret))
    # except ClientError as error:
    #      logging.error(
    #         "Found error. status: {}, error code: {}, error message: {}".format(
    #             error.status_code, error.error_code, error.error_message
    #         )
    # )

    # return


    try:
        usdtQuantity = 5.5
        quantityPrecision = 0
        pricePrecision = 0

        exInfo = um_futures_client.exchange_info()
        for x in exInfo['symbols']:
            if x['symbol'] == 'RENUSDT':
                quantityPrecision = int(x['quantityPrecision'])
                pricePrecision = int(x['pricePrecision'])
                logging.info(x['quantityPrecision']) # 数量精度
                logging.info(x['pricePrecision']) # 数量精度


        # logging.info(exInfo['symbols'])
        # return

        # 获取最新价格，来计算下单数量, 不用标记价格
        ret = um_futures_client.ticker_price(symbol='RENUSDT')
        latestPrice = float(ret['price'])
        logging.info(latestPrice)

        tokenQuantity = usdtQuantity/latestPrice


        quantity = f"%.{quantityPrecision}f"%tokenQuantity
        logging.info( 'tokenQuantity============>{}'.format( tokenQuantity))

        # response = um_futures_client.new_order_test(
        #     symbol= "RENUSDT",
        #     side= "BUY",   # BUY:买入开多，SELL:卖出开空
        #     type= "MARKET", # MARKET 市价单
        #     quantity = quantity,  # 币的数量
        #     # timeInForce= "GTC",
        # )


        stopPrice = f"%.{pricePrecision}f"%(latestPrice * (1 - 0.05)) # 要乘以杠杆倍数
        logging.info("stopPrice ===> {}".format(stopPrice))

        # 下止损单, 触发后，按照市价(标记价格)全部平仓
        # response = um_futures_client.new_order_test(
        #     symbol= "RENUSDT",
        #     side= "SELL",   # 开空时, 买入止损;  开多时，卖出止损
        #     type= "STOP_MARKET", # STOP_MARKET 市价止盈/损单
        #     stopPrice= stopPrice,  # 触发价格
        #     closePosition="true",  # 触发后，全部平仓
        #     workingType ="MARK_PRICE" # 按标记价格止损
        # )

        params = [
            {
                "symbol":   "RENUSDT",
                "side":     "BUY",   # BUY:买入开多，SELL:卖出开空
                "type":     "MARKET", # MARKET 市价单
                "quantity": quantity,  # 币的数量
            },
            {
                "symbol":           "RENUSDT",
                "side":             "SELL",
                "type":             "STOP_MARKET", # STOP_MARKET 市价止盈/损单
                "stopPrice":        stopPrice,  # 触发价格
                "closePosition":    "true",  # 触发后，全部平仓
                "workingType":      "MARK_PRICE" # 按标记价格止损
            },
        ]

        response = um_futures_client.new_batch_order(params)
        logging.info(response)
    except ClientError as error:
        logging.error(
            "Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )


    pass

if __name__ == '__main__':
    main()
