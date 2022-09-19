from datetime import datetime
import sqlite3

con = sqlite3.connect('data/database.db', check_same_thread=False)


def insertOrderDB(getApiData):
    """Update new orders to database"""
    cur = con.cursor()
    orders = getApiData

    for order in orders:
        symbol, orderId       = order['symbol'], order['orderId']
        orderListId           = order['orderListId']
        clientOrderId         = order['clientOrderId']
        price, origQty        = order['price'], order['origQty']
        executedQty           = order['executedQty']
        cummulativeQuoteQty   = order['cummulativeQuoteQty']
        status, timeInForce   = order['status'], order['timeInForce']
        type, side            = order['type'], order['side']
        stopPrice, icebergQty = order['stopPrice'], order['icebergQty']
        time, updateTime      = order['time'], order['updateTime']
        isWorking             = order['isWorking']
        origQuoteOrderQty     = order['origQuoteOrderQty']
        isDCA                 = str()

        sql = """INSERT OR IGNORE INTO orders VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
        val = (symbol, orderId, orderListId, clientOrderId, price, origQty, executedQty,
               cummulativeQuoteQty, status, timeInForce, type, side, stopPrice, icebergQty,
               time, updateTime, isWorking, origQuoteOrderQty, isDCA)
        cur.execute(sql, val)
    con.commit()
    cur.close()


def insertTradesDB(getApiData):
    """Update new trade to database"""
    cur = con.cursor()
    trades = getApiData
    
    for trade in trades:
        symbol, id                    = trade['symbol'], trade['id']
        orderId, orderListId          = trade['orderId'], trade['orderListId']
        price                         = trade['price']
        qty, quoteQty                 = trade['qty'], trade['quoteQty']
        commission, commissionAsset   = trade['commission'], trade['commissionAsset']
        time                          = trade['time']
        isBuyer, isMaker              = trade['isBuyer'], trade['isMaker']
        isBestMatch                   = trade['isBestMatch']
        DCA                           = str()

        sql = """INSERT OR IGNORE INTO trades VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?"""
        val = (symbol, id, orderId, orderListId, price, qty, quoteQty,
               commission, commissionAsset, time, isBuyer, isMaker, isBestMatch, DCA)
        cur.execute(sql, val)
    con.commit()
    cur.close()



def insertCandleDB(interval, data):
    """Update new candle to database"""
    cur = con.cursor()
    
    candles = data
    
    for candle in candles:
        Id                   = None
        Pair, Interval       = 'BNBBUSD', interval
        OpenTime             = candle[0]
        Open, Hight          = candle[1], candle[2]
        Low, Close           = candle[3], candle[4]
        Volume, CloseTime    = candle[5], candle[6]
        QuoteVolume          = candle[7]
        NumTrades            = candle[8]
        TakerBuyVolume       = candle[9]
        TakerBuyQuoteVolume  = candle[10]
        Ignore               = candle[11]

        sql = """INSERT OR IGNORE INTO candle VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
        val = (Id, Pair, Interval, OpenTime, Open, Hight, Low, Close, Volume, CloseTime, QuoteVolume,
                NumTrades, TakerBuyVolume, TakerBuyQuoteVolume,Ignore)
        cur.execute(sql, val)
    con.commit()
    cur.close()


def insertBalanceDB(balance):
    """Update the account balance"""

    cur = con.cursor()
    
    Id, Time   = None, datetime.now()
    BnbLocked  = balance['bnb'][1]
    BnbFree    = balance['bnb'][0]
    BusdLocked = balance['busd'][1]
    BusdFree   = balance['busd'][0]
    
    sql = """INSERT OR IGNORE INTO account_info VALUES(?,?,?,?,?,?)"""
    val = (Id, Time, BnbLocked, BnbFree, BusdLocked, BusdFree)
        
    cur.execute(sql, val)
    con.commit()
    cur.close()

