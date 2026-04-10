import time

def execute_trade(exchange_buy, exchange_sell, amount, symbol, max_retries=3, retry_delay=2):
    for attempt in range(max_retries):
        try:
            # Place market buy order
            buy_order = exchange_buy.create_market_buy_order(symbol, amount)
            print(f"Buy order placed on {exchange_buy.name}: {buy_order}")

            # Wait for buy order to fill (optional, depending on exchange API)
            # You might want to poll order status here

            # Place market sell order
            sell_order = exchange_sell.create_market_sell_order(symbol, amount)
            print(f"Sell order placed on {exchange_sell.name}: {sell_order}")

            # Optionally wait for order fills or check status
            # For simplicity, assuming immediate fill

            return {
                "buy": buy_order,
                "sell": sell_order
            }
        except Exception as e:
            print(f"Attempt {attempt+1} failed: {e}")
            if attempt < max_retries - 1:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                print("Max retries reached. Trade failed.")
                return None
import asyncio

async def execute_trade(exchange_buy, exchange_sell, amount, symbol, max_retries=3, retry_delay=2):
    for attempt in range(max_retries):
        try:
            buy_order = await exchange_buy.create_market_buy_order(symbol, amount)
            print(f"Buy order placed on {exchange_buy.name}: {buy_order}")

            # Optional: await order fill confirmation here

            sell_order = await exchange_sell.create_market_sell_order(symbol, amount)
            print(f"Sell order placed on {exchange_sell.name}: {sell_order}")

            return {
                "buy": buy_order,
                "sell": sell_order
            }
        except Exception as e:
            print(f"Attempt {attempt+1} failed: {e}")
            if attempt < max_retries - 1:
                print(f"Retrying in {retry_delay} seconds...")
                await asyncio.sleep(retry_delay)
            else:
                print("Max retries reached. Trade failed.")
                return None