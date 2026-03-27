# Trading Bot - Binance Futures Testnet

## Setup

1. Clone repo
2. Install dependencies:
   pip install -r requirements.txt

3. Create .env file with:
   API_KEY=your_key
   API_SECRET=your_secret

## Run

### Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

### Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 60000

## Features
- Market & Limit Orders
- BUY / SELL support
- CLI-based input
- Logging system
- Error handling

## Logs
Check logs in logs/bot.log