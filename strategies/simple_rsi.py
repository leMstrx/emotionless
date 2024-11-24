import ta.momentum
from data.data_fetcher import fetch_historical_data
from trade_manager import place_market_order
import ta

def simple_rsi_strategy(symbol, period=14, oversold=30, overbought=70, qty=1):
    # Fetch historical data
    data = fetch_historical_data(symbol, timeframe="1D", limit=period+1)
    if data is None or data.empty:
        print("No data to apply the stratgey")
        return
    
    #Calculate RSI
    data['rsi'] = ta.momentum.RSIIndicator(data['close'], window=period).rsi()

    #Get the most recent RSI value
    current_rsi = data['rsi'].iloc[-1]
    print(f"{symbol} RSI: {current_rsi}")

    #Decision Logic

    if current_rsi < oversold:
        print("OverSold! Buy")
        place_market_order(symbol, qty, 'buy')
    elif current_rsi > overbought:
        print("OverBought! Sell")
        place_market_order(symbol, qty, 'sell')
    else:
        print("No trade signal")
