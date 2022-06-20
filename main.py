from flask import Flask, render_template
import requests
import datetime

app = Flask(__name__)
url = "https://api.coingecko.com/api/v3/coins"


def update_crypto_data():
    crypto_data = {}
    response = requests.get(url)
    top50_data = response.json()
    for coin in top50_data:
        coin_name = coin["name"]
        coin_symbol = coin["symbol"]
        coin_rank = coin["market_data"]["market_cap_rank"]
        current_price = coin["market_data"]["current_price"]["usd"]
        crypto_data[coin_name] = {"symbol": coin_symbol, "rank": coin_rank, "price": current_price}

    return crypto_data


@app.route("/")
def home():
    time = datetime.datetime.now().strftime("%D %H:%M:%S")
    data = update_crypto_data()
    return render_template("index.html", data=data, time=time)


if __name__ == '__main__':
    app.run(debug=True)
