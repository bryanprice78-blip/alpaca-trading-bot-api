from flask import Flask, jsonify
from flask_cors import CORS
import alpaca_trade_api as tradeapi
import os

app = Flask(__name__)
CORS(app)

API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
BASE_URL = "https://paper-api.alpaca.markets"

api = tradeapi.REST(API_KEY, SECRET_KEY, base_url=BASE_URL)
@app.route("/api/tradingbot/latest", methods=["GET"])
def latest_data():
    try:
        position = api.get_account().cash
        clock = api.get_clock()
        return jsonify({
            "cash": position,
            "market_open": clock.is_open,
            "timestamp": clock.timestamp.isoformat()
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@app.route("/api/tradingbot/buy", methods=["GET"])
def buy():
    try:
        api.submit_order(
            symbol="AAPL",
            qty=1,
            side="buy",
            type="market",
            time_in_force="gtc"
        )
        return jsonify({"message": "Buy order submitted"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/tradingbot/sell", methods=["GET"])
def sell():
    try:
        api.submit_order(
            symbol="AAPL",
            qty=1,
            side="sell",
            type="market",
            time_in_force="gtc"
        )
        return jsonify({"message": "Sell order submitted"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)





