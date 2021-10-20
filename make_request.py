from query_alpaca import submit_order, get_open_positions, get_account_info
from query_quiver import get_recent_orders


def make_trades():
    recent_orders = get_recent_orders()

    my_open_positions = get_open_positions()

    try:
        get_account_info()
    except Exception as e:
        print(e)
        return

    # get recent orders
    # see if any of those recent orders are selling positions that I do not own
    # check account balance and make buy requests within balance

    for order in recent_orders:
        if (order["Ticker"] not in my_open_positions) and (
            order["Transaction"].lower() in ["sell", "sale"]
        ):
            continue
        submit_order(order["Ticker"], 1, order["Transaction"])


if __name__ == "__main__":
    make_trades()
