from strategies.simple_rsi import simple_rsi_strategy

def main():
    # List of stocks to monitor
    symbols = ['AAPL', 'TSLA', 'AMZN', 'MSFT', 'GOOGL']

    # Run the strategy for each symbol
    for symbol in symbols:
        print(f"Running strategy for {symbol}")
        simple_rsi_strategy(symbol)

    if __name__ == '__main__':
        main()
