import alpaca_trade_api as tradeapi


def submit_order(symbol, qty, buy_or_sell):
    buy_or_sell = "buy"

    api = tradeapi.REST()
    print(api)

    api.submit_order(
        symbol=symbol,
        qty=qty,
        side=buy_or_sell,
        type="market",
        time_in_force="gtc",
    )
