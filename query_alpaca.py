import alpaca_trade_api as tradeapi

API = tradeapi.REST()


def submit_order(symbol, qty, buy_or_sell):
    # check if symbol is owned before trying to sell it
    # if qty is too great (ie: too expensive), reduce it to a specified amt

    if buy_or_sell.lower() not in ["purchase", "buy", "sell", "sale"]:
        print(f"SKIPPING {buy_or_sell} transaction for {symbol}")
        return

    if buy_or_sell.lower() == "purchase":
        buy_or_sell = "buy"

    if buy_or_sell.lower() == "sale":
        buy_or_sell = "sell"

    try:
        API.submit_order(
            symbol=symbol,
            qty=qty,
            side=buy_or_sell,
            type="market",
            time_in_force="gtc",
        )
        print(f"Ordered: {buy_or_sell} for {qty}-{symbol}")
    except Exception as e:
        print(f"ERROR: {e}")


def get_open_positions():
    all_positions = API.list_positions()
    open_pos_symbols = []
    for pos in all_positions:
        open_pos_symbols.append(pos.symbol)
    return open_pos_symbols


def get_account_info():
    account = API.get_account()
    if account.trading_blocked:
        raise Exception("Account is currently restricted from trading.")

    if float(account.buying_power) < 1:
        raise Exception("You're broke bitch")

    print("Account is active: running...")
    return account


# print(f"{account.buying_power} is available as buying power.")
