"""
get transaction data from quiver
filter by transactions that happened today
"""

import requests
from datetime import date, datetime, timedelta

from api import submit_order

TODAY = datetime.today()

api_token = ""

headers = {
    "Authorization": f"Token {api_token}",
    "accept": "application/json",
}
API_URL = "https://api.quiverquant.com/beta/live/senatetrading"

res = requests.get(API_URL, headers=headers).json()

recent_orders = []
for t in res:
    if datetime.strptime(t["Date"], "%Y-%m-%d") > (TODAY - timedelta(days=30)):
        recent_orders.append(t)

print(recent_orders)

"""
Ticker:
Date:
Person:
Transaction:
Amount:
"""

submit_order(res[0]["Ticker"], 1, res[0]["Transaction"])
