import alpaca_trade_api as tradeapi
from config import ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL

api = tradeapi.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, base_url=ALPACA_BASE_URL, api_version='v2')

symbol = "AAPL"
timeframe = "1D"
limit = 15

try:
    print(f"Fetching historical data for {symbol}...")
    bars = api.get_bars(symbol, timeframe, limit=limit).df
    if bars.empty:
        print(f"No data found for {symbol}.")
    else:
        print(f"Data for {symbol}:")
        print(bars)
except Exception as e:
    print(f"Error fetching data for {symbol}: {e}")