def validate_inputs(symbol, side, order_type, quantity, price):
    if not symbol or len(symbol) < 5:
        return False, "Invalid Symbol (e.g., BTCUSDT)"
    if side not in ["BUY", "SELL"]:
        return False, "Side must be BUY or SELL"
    if order_type not in ["MARKET", "LIMIT"]:
        return False, "Type must be MARKET or LIMIT"
    if float(quantity) <= 0:
        return False, "Quantity must be greater than 0"
    if order_type == "LIMIT" and (not price or float(price) <= 0):
        return False, "Limit price must be greater than 0"
    return True, None