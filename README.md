# 🚀 Binance Futures Trading Bot (Demo API)

## 📌 Overview

This project is a simplified trading bot built in Python that interacts with Binance Futures Demo API to place MARKET and LIMIT orders via CLI.

## ⚙️ Features

* Place MARKET and LIMIT orders
* Supports BUY and SELL
* CLI-based input using argparse
* Structured project architecture
* Logging of API requests and responses
* Error handling for invalid inputs and API failures

## 🛠️ Tech Stack

* Python 3
* python-binance
* argparse
* logging

## 📁 Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│
├── cli.py
├── requirements.txt
├── README.md
├── .env (not included)
├── logs/
```

## 🔐 Setup Instructions

1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/binance-trading-bot.git
cd binance-trading-bot
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Create `.env` file

```
API_KEY=your_api_key
API_SECRET=your_secret_key
```

4. Update API URL in `client.py`

```
client.FUTURES_URL = 'https://demo-fapi.binance.com/fapi'
```

## 🚀 Usage

### Market Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.003
```

### Limit Order

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.003 --price 70000
```

## 📊 Logging

Logs are stored in:

```
logs/bot.log
```

Includes:

* Order requests
* Order responses
* Error handling

## ⚠️ Notes

* Minimum order size must be ≥ 100 USDT
* Demo environment used (no real funds involved)

## 👨‍💻 Author

Aum Vipul
