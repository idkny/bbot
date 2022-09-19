import sqlite3

con = sqlite3.connect("database.db", check_same_thread=False)


# Get Open time of candle
def last_k_line(interval):
    """check if the data is uptodate and update if necessary"""
    try:
        cur = con.cursor()
        cur.execute(
            f'SELECT OpenTime, Max(Id) FROM candle WHERE Interval = "{interval}"'
        )
        Data = cur.fetchall()
    except sqlite3.Error as err:
        print(f"DB error response: {err}")
    return Data


# Get open and close price of the 2 last 1D candle data
def get_1D_Data():
    """Get open and close Prices of the 2 last 1 day candles"""
    try:
        cur = con.cursor()
        cur.execute(
            'SELECT Open, Close FROM candle WHERE Interval = "1D" ORDER BY Id DESC LIMIT(2)'
        )
        Data = cur.fetchall()
    except sqlite3.Error as err:
        print(f"DB error response: {err}")
    return Data


# Get open and close price of the 2 last Wekly candle data
def get_1W_data():
    """Get open and close Prices of the 2 last 1 weekly candles"""
    try:
        cur = con.cursor()
        cur.execute(
            'SELECT Open, Close FROM candle WHERE Interval = "1W" ORDER BY Id DESC LIMIT(2)'
        )
        Data = cur.fetchall()
    except sqlite3.Error as err:
        print(f"DB error response: {err}")
    return Data


# Get open orders id and if is dca
def get_orders_id():
    try:
        cur = con.cursor()
        cur.execute('SELECT orderId, isDCA FROM orders WHERE status = "NEW" ')
        Data = cur.fetchall()
    except sqlite3.Error as err:
        print(f"DB error response: {err}")
    return Data


def account_balance():
    try:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM account_info ORDER BY id DESC LIMIT 1")
        Data = cur.fetchall()
    except sqlite3.Error as err:
        print(f"DB error response: {err}")
    return Data


# Get non dca open orders prices side buy
def opn_buy_orders_prices():
    try:
        cur = con.cursor()
        cur.execute('SELECT price FROM orders WHERE status = "NEW" AND side = "BUY" ')
        Data = cur.fetchall()
    except sqlite3.Error as err:
        print(f"DB error response: {err}")
    return Data


def opn_sell_orders_prices():
    try:
        cur = con.cursor()
        cur.execute('SELECT price FROM orders WHERE status = "NEW" AND side = "SELL" ')
        Data = cur.fetchall()
    except sqlite3.Error as err:
        print(f"DB error response: {err}")
    return Data


print(account_balance())
