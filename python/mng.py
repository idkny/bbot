from writeDb import *
from gtDataDB import *
from getApi import *
from numpy import arange
from datetime import datetime


# Check if the current price is 10% greater then the sarting price
#   if yes, new starting price is current price -5% else start price = start price.
def strP(price, strPrice=0):
    """create a starting price to trade"""
    if float(price) > strPrice + ((strPrice / 100) * 10):
        newStrPrice = price - ((price / 100) * 5)
        strPrice = int(newStrPrice)
        return strPrice


# Itirate over a range of price that start at the starting price and
#   stop at the starting price +10% with a step of 2.5 .
# If the itiration value is >= (start price +10%)-2.5, the function is called again
#   and iterate over the same price range .
def buyP(startPrice):
    """Generate a buying price"""
    endP = startPrice + (startPrice / 100) * 10
    for b in arange(startPrice, endP, 2.5):
        yield (b)

    return b


def updt_account_tbl():
    """Get API account balances, update datatbase"""
    bnb = api_balance("BNB")
    busd = api_balance("BUSD")

    data = {"bnb": (bnb["free"], bnb["locked"]), "busd": (busd["free"], busd["locked"])}

    insertBalanceDB(data)


def account_info(price):
    """Calculate the busd value of the account"""
    data = account_balance()

    # Get the current value of the account in usd
    """return the current state of the account"""
    bnb_free, bnb_locked = data[0][3], data[0][2]
    busd_free, busd_locked = data[0][4], data[0][5]

    # return the busd value of bnb in the account
    bnb_value = float(price) * ((float(bnb_locked)) + float(bnb_free))

    # return the busd value of all locked asset in the account
    locked_bnb_in_busd = float(price) * float(bnb_locked)
    locked_asset = locked_bnb_in_busd + float(busd_locked)
    # return the busd value of the account
    balance_value = bnb_value + (float(busd_free) + float(busd_locked))

    return balance_value, bnb_value, locked_asset, busd_free


def cancel_non_dca_order():
    """Cancel all non dca open orders"""
    orderIDS = get_orders_id()
    for id in orderIDS:
        if id[1] != True:
            api_cancel_orders(id)
            print(f"order number {id}: Was canceled")


# ----CHECK THAT TABLE CANDLE IN THE DATABASE IS UPTODATE, IF NECESSARY UPDATE --------


def check_candleDB():
    # Get database last update date of table candle
    daily_candle = last_k_line("1D")
    weekly_candle = last_k_line("1W")

    # Count the number of days pass between the last update to today
    days_pass1D = count_days(daily_candle[0])
    days_pass1W = count_days(weekly_candle[0])

    # If more then one day pass since last daily candle update, update.
    if days_pass1D > 1:
        # Get and format starting and ending dates to fit api requirement
        dates = format_dates(daily_candle[0])
        data = api_k_lines("1D", dates[0], dates[1])
        # Update the database
        insertCandleDB("1D", data)

    # If more then 7 days pass since last weekly candle update, update.
    if days_pass1W > 7:
        # Get and format starting and ending dates to fit api requirement
        dates = format_dates(weekly_candle)
        data = api_k_lines("1W", dates[0], dates[1])
        # Update the database
        insertCandleDB("1W", data)


# ------------CHECK MARKET STATS ---------------


def last_Kline_Color(data):
    """CHeck if candle is green"""

    daily, weekly = get_1D_Data(), get_1W_data
    daily_green, weekly_green = bool(), bool()

    if daily[0][0] > daily[1][1]:
        daily_green = True

    if weekly[0][0] > weekly[1][1]:
        weekly_green = True

    return daily_green, weekly_green


# Check the number of days pass between a certain date up today
def count_days(Data):
    """Check the num of days pass between a certain date up today"""

    # Get the curent date
    Timenow = datetime.now()

    # Change the current date to int format and epoch time
    now = int(round(Timenow.timestamp()))

    # Read the data recived and retrive the last date the database was update
    last_time = Data / 1000

    # Compaire the num of days pass between the last data avialble to today
    delta = now - last_time
    num_of_days = int(datetime.fromtimestamp(delta).strftime("%d"))

    return num_of_days


# Change the date format so it will be acepeted by the api
def format_dates(Data):
    """format dates to fit api"""
    # Get the curent date
    Timenow = datetime.now()
    # Change the date to int format and epoch time
    now = int(round(Timenow.timestamp()))

    # Format to api standart
    start = datetime.fromtimestamp(Data / 1000).strftime("%d-%b-%Y")
    end = datetime.fromtimestamp(now).strftime("%d-%b-%Y")

    return start, end


def dca3(startPrice, quantity):

    percent3 = (3, 5, 7, 10, 14, 16)
    dca_buy = [x for x in percent3]


def dca5(startPrice, quantity):

    percent3 = (5, 7, 10, 13, 16, 19)
    dca_buy = [x for x in percent3]
