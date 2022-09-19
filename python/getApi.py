from time import sleep
from binance import Client, exceptions
from binance.enums import *
import os

api_key = os.environ.get('api_key')
api_secret = os.environ.get('api_secret')

client = Client(api_key, api_secret)


def api_balance(asset_name):
    try:
        data = client.get_asset_balance(asset=asset_name)
    except exceptions.BinanceAPIException as err:
        print(f"{asset_name} API error response: {err.status_code}")
        sleep(err.message)
    return data


def api_orders_trades(endpoint):
    if endpoint == "orders":
        try:
            orders = client.get_all_orders(symbol="BNBBUSD")
        except exceptions.BinanceAPIException as err:
            print(f"Orders API error response: {err.status_code}")
            sleep(err.message)
    else:
        try:
            trades = client.get_my_trades(symbol="BNBBUSD")
        except exceptions.BinanceAPIException as err:
            print(f"Trades API error response: {err.status_code}")
            sleep(err.message)
    return orders, trades


def api_k_lines(interval, start_date, end_date):
    if interval == "1W":
        try:
            candle1W = client.get_historical_klines(
                "BNBBUSD", Client.KLINE_INTERVAL_1WEEK, start_date, end_date
            )
        except exceptions.BinanceAPIException as err:
            print(f"{interval} API error response: {err.status_code}")
            sleep(err.message)
    else:
        try:
            candle1D = (
                client.get_historical_klines(
                    "BNBBUSD", Client.KLINE_INTERVAL_1DAY, start_date, end_date
                ),
            )
        except exceptions.BinanceAPIException as err:
            print(f"{interval} API error response: {err.status_code}")
            sleep(err.message)
    return candle1W, candle1D


def api_create_Lorders(Side, Quantity, Price):
    """Creat a limit buy and/or sell order"""
    quan = float(Quantity)
    if Side == "buy":
        try:
            buy_order = client.order_limit_buy(
                symbol="BNBBUSD", quantity=quan, price=Price
            )
        except exceptions.BinanceAPIException as err:
            print(f"{Side} API error response: {err.status_code}")
            sleep(err.message)
    else:
        try:
            sell_order = client.order_limit_sell(
                symbol="BNBBUSD", quantity=quan, price=Price
            )
        except exceptions.BinanceAPIException as err:
            print(f"{Side} API error response: {err.status_code}")
            sleep(err.message)


def api_create_Morders(Side, Quantity):
    """Creat a market buy and/or sell order"""
    quan = float(Quantity)
    if Side == "buy":
        try:
            buy_order = client.order_market_buy(symbol="BNBBUSD", quantity=quan)
        except exceptions.BinanceAPIException as err:
            print(f"{Side} API error response: {err.status_code}")
            sleep(err.message)
    else:
        try:
            sell_order = client.order_market_sell(symbol="BNBBUSD", quantity=quan)
        except exceptions.BinanceAPIException as err:
            print(f"{Side} API error response: {err.status_code}")
            sleep(err.message)


def api_cancel_orders(order_id):
    try:
        cancel_order = client.cancel_order("BNBBUSD", orderId=order_id)
    except exceptions.BinanceAPIException as err:
        print(f"Cancel orders API error response: {err.status_code}")
        sleep(err.message)


"""
# Connect to Binance API, get data: insert arguments to the function.
#   the first argument calls the stream/endpoint, then depending on the choice
#   add the relevent argument/s as a dictionary (**kwargs)

# FORMAT EXAMPLE: con_data('balance', asset='BNB')
#                 con_data('orders', smbol='BNBBUSD')
#                 con_data('candle1D', smbol='BNBBUSD', strt_date="1 Dec, 2021", end_date="1 Jan, 2022")
def con_data(call_stream, **kwargs):
    Connect and retrive data from Binance API

    arg = {'asset': str(), 'smbol': str(), 'strt_date': str(), 'end_date': str(),
           'quantity': str(), 'price': str(), 'orderId': str()}

    for key, value in kwargs.items():
        if key in arg:
            arg[key] = value

    endPoint = {'balance': client.get_asset_balance(asset=arg['asset']),
                'orders': client.get_all_orders(symbol=arg['smbol']),
                'trades': client.get_my_trades(symbol=arg['smbol']),
                'server_time': client.get_server_time(),
                'candle1W': client.get_historical_klines(arg['smbol'], Client.KLINE_INTERVAL_1WEEK,
                                                         arg['strt_date'], arg['end_date']),
                'candle1D': client.get_historical_klines(arg['smbol'], Client.KLINE_INTERVAL_1DAY,
                                                         arg['strt_date'], arg['end_date']),
                'buy_order': client.order_limit_buy(symbol=arg['smbol'], quantity=arg['quantity'],
                                                    price=arg['price']),
                'sell_order': client.order_limit_sell(symbol=arg['smbol'], quantity=arg['quantity'],
                                                      price=arg['price']),
                'cancel_order': client.cancel_order(arg['smbol'], orderId=arg['orderId']),
                'status': client.get_account_api_trading_status(),
                'order_status': client.get_order(symbol=arg['smbol'], orderId=arg['orderId']),
                 'avg_price': client.get_avg_price(symbol=arg['smbol'])}

    if call_stream in endPoint:
        try:
            print(call_stream)
            data = endPoint[call_stream]
        except exceptions.BinanceAPIException as err:
            print(f'API error response: {err.status_code}')
            sleep(err.message)
    print(data)
    return data
    """
