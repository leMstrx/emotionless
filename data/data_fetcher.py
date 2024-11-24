import alpaca_trade_api as tradeapi
from config import ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL

#Initialize the API
api = tradeapi.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL, api_version='v2')

def fetch_historical_data(symbol, timeframe="1D",limit=100):
    try:
        print(f"Fetching historical data for {symbol} with limit {limit} and timeframe {timeframe}")
        bars = api.get_bars(symbol, timeframe, limit=limit).df
        if bars.empty:
            print(f"No data found for {symbol}")
            return None
        print(f"Data fetched for {symbol}:")
        print(bars.head())
        return bars
    except Exception as e:
        print('Error fetching historical data', str(e))
        return None