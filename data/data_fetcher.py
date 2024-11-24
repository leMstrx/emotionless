import alpaca_trade_api as tradeapi
from config import ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL

#Initialize the API
api = tradeapi.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL, api_version='v2')

def fetch_historical_data(symbol, timeframe="1D",limit=100):
    try:
        bars = api.get_bars(symbol, timeframe, limit=limit).df
        return bars
    except Exception as e:
        print('Error fetching historical data', str(e))
        return None