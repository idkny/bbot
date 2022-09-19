from mng import *
from binance import ThreadedWebsocketManager
from time import sleep
import asyncio


def main():

    
    symbol = 'BNBBUSD'
   
    twm = ThreadedWebsocketManager(api_key=api_key, api_secret=api_secret)
    twm.start()


    def handle_socket_message(msg):

        price            = float(msg['data']['c'])
        startPrice       = strP(price, strPrice=0)
        endPrice         = startPrice + ((startPrice /100) *10)
        balance          = account_info(price)
        open_buy_orders  = opn_buy_orders_prices()
        open_sell_orders = opn_sell_orders_prices()
        buyPrice         = range(startPrice, endPrice, 2)
        sellPrice        = open_buy_orders + (open_buy_orders /100) 
        buyQuantity      = balance[0] /100
        sellQuantity     = []
        task             = asyncio.create_task(sell())

        msg = msg['data'] if 'data' in msg else msg    
        while 'e ' == '24hrMiniTicker' and 'c' in msg:
            async def buy():
                if balance[3] < (balance[0] /100) *30:
                    for buy in buyPrice:
                        if price > buy not in open_buy_orders[0]:
                            await asyncio.sleep(1.5)
                            api_create_Lorders('buy' ,buyQuantity, buy)
                            
            async def sell():
                for sell in :
                    
                        
                            api_create_Lorders('sell' ,Quantity, buy)

          


            #----------------------PREPARE FOR DCA------------------------#
              
            # While the price is 1% lower then the starting price.
           # while price < start_price -((start_price /100)* 1):
            #    pass
           
    
            # If the price dropt to -2% from starting price cancel all non dca orders

                 
    streams = ['bnbbusd@miniTicker']
    twm.start_multiplex_socket(callback=handle_socket_message, streams=streams)
    twm.join()
        
        # create a will loop till it reconnect, check max reconnect
    twm.stop() 
    sleep(2)
    twm.start()
    print("interrupted")
    """
    {
    'e': 'error',
    'm': 'Max reconnect retries reached'
}

# check for it like so
def process_message(msg):
    if msg['e'] == 'error':
        # close and restart the socket
    else:
        # process message normally
    """       
            

if __name__ == "__main__":
    main()