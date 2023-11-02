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


    params = [
        {
            "symbol": "RENUSDT",
            "side": "BUY",   # BUY:买入开多，SELL:卖出开空
            "type": "MARKET", # MARKET 市价单
            "quantity": "0.1",  # USDT 数量
            "timeInForce": "GTC",
        },
        # {
        #     "symbol": "QTUMUSDT",
        #     "side": "LONG",
        #     "type": "MARKET",
        #     "quantity": "0.1",
        #     "timeInForce": "GTC",
        #     "price": "8000.1",
        # },
    ]

    # 切换到 “逐仓”模式
    # try:
    #     ret = um_futures_client.change_margin_type(symbol='RENUSDT', marginType='ISOLATED')
    # except ClientError as error:
    #      logging.error(
    #         "Found error. status: {}, error code: {}, error message: {}".format(
    #             error.status_code, error.error_code, error.error_message
    #         )
    #     )


    # 获取最新价格


    try:
        usdtQuantity = 5
        quantityPrecision = 0

        exInfo = um_futures_client.exchange_info()
        for x in exInfo['symbols']:
            if x['symbol'] == 'RENUSDT':
                quantityPrecision = int(x['quantityPrecision'])
                logging.info(x['quantityPrecision']) # 数量精度


        # logging.info(exInfo['symbols'])
        # return

        ret = um_futures_client.ticker_price(symbol='RENUSDT')
        logging.info(ret['price'])

        tokenQuantity = usdtQuantity/float(ret['price'])


        quantity = f"%.{quantityPrecision}f"%tokenQuantity
        logging.info( 'tokenQuantity============>{}'.format( tokenQuantity))

        response = um_futures_client.new_order_test(
            symbol= "RENUSDT",
            side= "BUY",   # BUY:买入开多，SELL:卖出开空
            type= "MARKET", # MARKET 市价单
            quantity = quantity,  # 币的数量
            # timeInForce= "GTC",
        )

        # response = um_futures_client.new_batch_order(params)
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
