import ccxt
import time

# Initialize exchanges with API keys (replace with your actual keys)
ex1 = ccxt.binance({
    'apiKey': 'YOUR_BINANCE_API_KEY',
    'secret': 'YOUR_BINANCE_SECRET',
})
ex2 = ccxt.kraken({
    'apiKey': 'YOUR_KRAKEN_API_KEY',
    'secret': 'YOUR_KRAKEN_SECRET',
})

SYMBOL = 'BTC/USDT'
THRESHOLD = 0.5  # Spread threshold in percentage
MAX_POSITION = 1.0  # Max BTC per side

# Position tracking
positions = {
    'ex1': 0.0,
    'ex2': 0.0
}

def get_price(exchange):
    """Fetch the latest price for SYMBOL from the given exchange."""
    ticker = exchange.fetch_ticker(SYMBOL)
    return ticker['last']

def place_order(exchange, side, amount):
    """Place a market order and update position tracking."""
    try:
        order = exchange.create_market_order(SYMBOL, side, amount)
        print(f"Placed {side} order on {exchange.name} for {amount} {SYMBOL}")
        # Update position
        if exchange == ex1:
            positions['ex1'] += amount if side == 'buy' else -amount
        elif exchange == ex2:
            positions['ex2'] += amount if side == 'buy' else -amount
        return order
    except Exception as e:
        print(f"Order failed on {exchange.name}: {e}")

def check_arbitrage():
    """Check for arbitrage and execute trades if opportunity exists."""
    p1 = get_price(ex1)
    p2 = get_price(ex2)

    spread = ((p2 - p1) / p1) * 100
    print(f"Binance: {p1} | Kraken: {p2} | Spread: {spread:.3f}%")
    
    # Determine if spread exceeds threshold
    if abs(spread) > THRESHOLD:
        # Decide direction: buy low, sell high
        if spread > 0:
            # Kraken price higher: buy on Binance, sell on Kraken
            if positions['ex1'] < MAX_POSITION and positions['ex2'] > -MAX_POSITION:
                print("Arbitrage: Buy on Binance, Sell on Kraken")
                place_order(ex1, 'buy', 0.01)
                place_order(ex2, 'sell', 0.01)
        else:
            # Binance price higher: buy on Kraken, sell on Binance
            if positions['ex2'] < MAX_POSITION and positions['ex1'] > -MAX_POSITION:
                print("Arbitrage: Buy on Kraken, Sell on Binance")
                place_order(ex2, 'buy', 0.01)
                place_order(ex1, 'sell', 0.01)

if __name__ == "__main__":
    while True:
        try:
            check_arbitrage()
            time.sleep(2)
        except Exception as e:
            print("Error:", e)