import argparse
import sys
from bot.client import BinanceTestnetClient
from bot.Validators import validate_inputs
from bot.Logging_config import setup_logging

# Hardcoded for testnet or use .env
API_KEY = "your_testnet_api_key" #client api key
API_SECRET = "your_testnet_api_secret" # personal secret key

logger = setup_logging()

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Bot")
    parser.add_argument("--symbol", required=True, help="e.g. BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--qty", required=True, type=float)
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")

    args = parser.parse_args()

    # 1. Validate
    is_valid, error_msg = validate_inputs(args.symbol, args.side, args.type, args.qty, args.price)
    if not is_valid:
        logger.error(f"Validation Error: {error_msg}")
        sys.exit(1)

    # 2. Initialize Client
    bot = BinanceTestnetClient(API_KEY, API_SECRET)

    # 3. Place Order
    try:
        logger.info(f"Sending {args.type} {args.side} order for {args.qty} {args.symbol}...")
        
        response = bot.place_futures_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.qty,
            price=args.price
        )

        # 4. Print Summary
        print("\n--- ORDER SUCCESS ---")
        print(f"OrderID:      {response.get('orderId')}")
        print(f"Status:       {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price:    {response.get('avgPrice', 'N/A')}")
        
        logger.info(f"Order Placed Successfully: {response['orderId']}")

    except Exception as e:
        logger.error(f"API Error: {str(e)}")
        print(f"\nOrder Failed: {e}")

if __name__ == "__main__":
    main()