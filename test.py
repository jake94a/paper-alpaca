import alpaca_trade_api as tradeapi

api = tradeapi.REST()

# Get the last 100 of our closed orders
closed_orders = api.list_orders(
    status="open", limit=100, nested=True  # show nested multi-leg orders
)

# Get only the closed orders for a particular stock
closed_aapl_orders = [o for o in closed_orders if o.symbol == "AAPL"]
print(closed_aapl_orders)
