import alpaca_trade_api as tradeapi
from config import ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL

#Initialize the API
api = tradeapi.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL, api_version='v2')

def place_market_order(symbol, qty, side):
    try:
        order = api.submit_order(
            symbol=symbol,
            qty=qty,
            side=side,
            type='market',
            time_in_force='gtc'
        )
        print(f"Order submitted: {order}")
        return order
    except Exception as e:
        print(f"Error placing order for {symbol}: {e}")
        return None
    
def list_positions():
    try:
        positions = api.list_positions()
        return positions
    except Exception as e:
        print(f"Error fetching positions: {e}")
        return None