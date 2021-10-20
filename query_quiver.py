"""
get transaction data from quiver
filter by transactions that happened today
"""

import requests
import os
from datetime import date, datetime, timedelta


# url_codes = [{"CONGRESS": "congresstrading"}, {"CONTRACTS": "govcontractsall"}]

TODAY = datetime.today()
QUIVER_API_TOKEN = os.environ["QUIVER_API_TOKEN"]
QUIVER_API_URL = f"https://api.quiverquant.com/beta/live/congresstrading"
HEADERS = {
    "Authorization": f"Token {QUIVER_API_TOKEN}",
    "accept": "application/json",
}


def get_recent_orders():
    res = requests.get(QUIVER_API_URL, headers=HEADERS).json()

    recent_orders = []
    for t in res:
        if datetime.strptime(t["ReportDate"], "%Y-%m-%d") > (
            TODAY - timedelta(days=30)
        ):
            recent_orders.append(t)
    return recent_orders


"""
Ticker:
Date:
Person:
Transaction:
Amount:
"""
