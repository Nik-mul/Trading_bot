** Trading Bot (Testnet)**
This is a modular Python-based CLI application built for the Primetrade.ai application task. It allows users to place Market and Limit orders on the Binance Futures Testnet (USDT-M).

**🚀 Features**

1 Modular Architecture: Separated concerns between API logic, validation, and CLI entry point.

2 Safety First: Input validation for symbols, sides, and quantities before hitting the API.

3 Logging: All requests, responses, and errors are logged to bot_activity.log.

4 Testnet Ready: Pre-configured to communicate with the Binance Futures Testnet environment.

🛠️ Setup Instructions
1. Prerequisites
Python 3.8 or higher.

A Binance Futures Testnet account (and API keys).

2. Installation
Clone the repository and install the required dependencies:

Bash
git clone <your-repo-url>
cd trading_bot
"**pip install -r requirements.txt**"

3. Configuration
Open cli.py and replace the placeholder API credentials with your Testnet keys:

Python
API_KEY = "your_actual_testnet_key"
API_SECRET = "your_actual_testnet_secret"

📈 Usage Examples
Place a Market BUY Order
Bash
**python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.002**

Place a Limit SELL Order
Bash
**python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.001 --price 70000

📁 Project Structure**

bot/client.py: Wrapper for the Binance API using python-binance.

bot/validators.py: Logic to ensure user input matches exchange requirements.

bot/logging_config.py: Centralized logging setup.

cli.py: The main entry point using argparse.

bot_activity.log: Generated file containing the history of all orders.
