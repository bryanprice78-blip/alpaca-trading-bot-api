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
