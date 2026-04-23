from binance.client import Client
from binance.enums import *

class BinanceTestnetClient:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret, testnet=True)
        
    def place_futures_order(self, symbol, side, order_type, quantity, price=None):
        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity,
        }
        
        if order_type.upper() == "LIMIT":
            if not price:
                raise ValueError("Price is required for LIMIT orders.")
            params["price"] = price
            params["timeInForce"] = TIME_IN_FORCE_GTC

        # Execute on USDT-M Futures
        return self.client.futures_create_order(**params)