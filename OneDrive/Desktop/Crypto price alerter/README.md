# 🔔 Crypto Price Alerter
intern id- CITS2715

A beginner-friendly Python application that monitors live cryptocurrency prices in near real-time and alerts you immediately when the price reaches your target!

---

## 🎯 Objective

Build a real-time cryptocurrency price monitoring tool that:
- Fetches live prices every 5 seconds with timestamps
- Allows users to set custom price targets
- Sends immediate alerts when the target price is reached
- Lets users decide whether to continue monitoring or exit after each alert
- Handles errors gracefully
- Requires no coding knowledge to use

---

## ✨ Features

✅ **Near Real-Time Monitoring** - Fetches cryptocurrency prices every 5 seconds

✅ **Timestamps** - Shows the exact time of each price check for accuracy

✅ **Immediate Alerts** - Notifies you instantly when price hits your target

✅ **Continue or Exit** - After alert, choose to keep monitoring or stop

✅ **Custom Alerts** - Set target prices and choose alert when price goes above or below

✅ **Multiple Cryptocurrencies** - Monitor any crypto on CoinGecko (Bitcoin, Ethereum, Cardano, etc.)

✅ **Multiple Currencies** - Get prices in USD, INR, EUR, GBP, JPY, and more

✅ **Error Handling** - Handles network errors, invalid inputs, and API issues gracefully

✅ **Beginner-Friendly** - Clean code with comments, easy to understand and modify

✅ **Safe Exit** - Stop monitoring anytime with Ctrl+C

---

## 🛠️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| **Python 3.7+** | Programming language |
| **requests** | Making HTTP requests to the API |
| **time** | Adding delays between price checks (5 seconds) |
| **datetime** | Getting current time for each check |
| **sys** | System-level operations (exit) |

---

## 📡 API Used

**CoinGecko Free API**
- URL: `https://api.coingecko.com/api/v3`
- **Free to use** - No API key required
- **No rate limits** for basic usage (1-2 requests per second)
- Provides cryptocurrency data for thousands of coins
- The app uses the `coins/markets` endpoint for better price accuracy
- Price data is near real-time; actual exchange prices may vary slightly
- Documentation: https://docs.coingecko.com/

---

## 📁 Project Structure

```
Crypto-Price-Alerter/
│
├── main.py                 # Main application file with all functions
├── requirements.txt        # List of Python packages needed
├── README.md              # This file - project documentation
├── .gitignore             # Files to ignore when pushing to GitHub
│
└── (no additional folders needed)
```

---

## 🚀 Installation & Setup

### Step 1: Clone or Download the Project

**Option A: Using Git (Recommended)**
```bash
git clone https://github.com/YOUR_USERNAME/Crypto-Price-Alerter.git
cd Crypto-Price-Alerter
```

**Option B: Download as ZIP**
- Download the ZIP file from GitHub
- Extract it to your desired location
- Open the folder in your terminal/command prompt

### Step 2: Create a Virtual Environment (Recommended)

A virtual environment keeps your project dependencies separate from your system Python.

**On Windows (Command Prompt or PowerShell):**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux (Terminal):**
```bash
python3 -m venv venv
source venv/bin/activate
```

✅ You should see `(venv)` at the beginning of your terminal line when activated.

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs the `requests` library needed to fetch data from the API.

---

## ▶️ How to Run

### Basic Usage

```bash
python main.py
```

Then follow the on-screen prompts:

1. **Enter cryptocurrency ID** - Examples: bitcoin, ethereum, cardano, ripple, dogecoin
2. **Enter target currency** - Examples: usd, inr, eur, gbp, jpy
3. **Enter target price** - Any positive number (e.g., 50000 for Bitcoin)
4. **Choose alert type** - Enter `1` for alert when price goes ABOVE target, or `2` for BELOW

### What Happens During Monitoring

- The app checks the price every 5 seconds
- Each check shows: `[HH:MM:SS] Check #N: Current Price`
- When the target is reached, you get an immediate alert with timestamp
- You're asked whether to continue monitoring or exit

### Stopping the Script

Press **Ctrl+C** in your terminal at any time to stop monitoring safely.

---

## 📋 Example Usage

### Example 1: Monitor Bitcoin when it goes above $50,000

```
🔔 CRYPTO PRICE ALERTER - Real-Time Monitoring Setup
======================================================================

Step 1: Enter cryptocurrency ID
Examples: bitcoin, ethereum, cardano, ripple, dogecoin
Enter coin ID: bitcoin

Step 2: Enter target currency
Examples: usd, inr, eur, gbp, jpy
Enter currency: usd

Step 3: Enter target price
Enter target price: 50000

Step 4: Choose alert condition
1. Alert when price is ABOVE target
2. Alert when price is BELOW target
Enter 1 or 2: 1

🔍 Validating cryptocurrency and currency...

======================================================================
📊 MONITORING STARTED - Real-Time Price Tracking
======================================================================
Coin: BITCOIN
Target Currency: USD
Target Price: $ 50,000.00
Alert Condition: Price ABOVE target
Check Interval: Every 5 seconds

💡 Tip: Press Ctrl+C at any time to stop monitoring

----------------------------------------------------------------------
[14:32:05] Check #1: $ 47,250.50
[14:32:10] Check #2: $ 47,300.00
[14:32:15] Check #3: $ 47,350.75
[14:32:20] Check #4: $ 51,200.75 ⏰ TARGET REACHED!

🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔

🎯 ALERT! BITCOIN price has gone ABOVE!
   Target Price: $ 50,000.00
   Current Price: $ 51,200.75
   Time: 14:32:20

🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔 🔔

What would you like to do?
1. Continue monitoring
2. Exit
Enter 1 or 2: 2

👋 Thank you for using Crypto Price Alerter!
```

### Example 2: Monitor Ethereum and Continue After Alert

```
Enter coin ID: ethereum
Enter currency: usd
Enter target price: 2500
Enter 1 or 2: 1

[14:35:10] Check #1: $ 2,480.50
[14:35:15] Check #2: $ 2,495.00
[14:35:20] Check #3: $ 2,510.25 ⏰ TARGET REACHED!

🎯 ALERT! ETHEREUM price has gone ABOVE!
   Target Price: $ 2,500.00
   Current Price: $ 2,510.25
   Time: 14:35:20

What would you like to do?
1. Continue monitoring
2. Exit
Enter 1 or 2: 1

📊 Continuing to monitor...

----------------------------------------------------------------------
[14:35:25] Check #4: $ 2,512.50
[14:35:30] Check #5: $ 2,505.00
```

---

## ℹ️ Notes on Valid Coin IDs

The CoinGecko API uses specific coin IDs. Here are some popular examples:

| Cryptocurrency | Coin ID |
|---|---|
| Bitcoin | `bitcoin` |
| Ethereum | `ethereum` |
| Cardano | `cardano` |
| Ripple | `ripple` |
| Dogecoin | `dogecoin` |
| Polkadot | `polkadot` |
| Litecoin | `litecoin` |
| Chainlink | `chainlink` |
| Binance Coin | `binancecoin` |
| Solana | `solana` |

**Full list:** Visit https://api.coingecko.com/api/v3/coins/list to see all available coins.

Valid currencies include: `usd`, `inr`, `eur`, `gbp`, `jpy`, `aud`, `cad`, `sgd`, `hkd`, `nzd`, and many more.

---

## 🔧 How the Code Works (Beginner Explanation)

### Main Functions

1. **`get_current_time()`** - Gets the current time in HH:MM:SS format
   
2. **`fetch_crypto_price()`** - Talks to the CoinGecko API and gets the current price
   
3. **`get_user_input()`** - Asks the user for coin ID, currency, target price, and alert type
   
4. **`validate_crypto_exists()`** - Checks if the coin and currency are valid before starting
   
5. **`check_alert_condition()`** - Compares current price with target to see if alert should trigger
   
6. **`format_price()`** - Makes prices look nice with currency symbols
   
7. **`ask_continue_monitoring()`** - Asks user whether to continue or exit after an alert
   
8. **`run_price_monitor()`** - The main loop that checks price every 5 seconds with timestamps
   
9. **`main()`** - Orchestrates the whole program flow

### How It Works Step-by-Step

1. Program starts and asks for user input
2. Input is validated (cryptocurrency exists, price is positive number)
3. Program enters an infinite loop that:
   - Gets current time
   - Fetches the current price from API
   - Compares it with the target price
   - Shows the price on screen with timestamp
   - Triggers alert if condition is met
   - If alert triggered, asks user to continue or exit
   - Waits 5 seconds and repeats
4. User can press Ctrl+C to exit at any time, or choose "Exit" after an alert

---

## 🐛 Error Handling

The program handles these common errors:

| Error | What Happens |
|-------|---|
| No internet connection | Shows error message, retries automatically |
| Invalid coin ID | Asks user to check and restart |
| Invalid currency | Asks user to check and restart |
| API timeout | Shows warning, retries after 5 seconds |
| Invalid price input | Asks user to enter a valid number |
| Invalid continue/exit choice | Asks the question again |

---

## 📚 Learning Resources

**Want to understand the code better?**

- [Python Official Documentation](https://docs.python.org/3/)
- [Requests Library Guide](https://docs.python-requests.org/)
- [CoinGecko API Docs](https://docs.coingecko.com/)
- [Python DateTime](https://docs.python.org/3/library/datetime.html)
- [Python Try/Except Error Handling](https://www.w3schools.com/python/python_try_except.asp)

---

## 🚀 Future Scope / Improvements

Here are ideas to make the project more advanced (as you learn more Python):

### Easy Improvements:
- [ ] Save alert history to a text file
- [ ] Add multiple price targets at once
- [ ] Store user preferences in a config file
- [ ] Add sound alerts (using `winsound` on Windows or `pygame`)
- [ ] Show price change percentage (e.g., +2.5% from last check)

### Medium Improvements:
- [ ] Create a simple GUI using `tkinter` or `PySimpleGUI`
- [ ] Send email/SMS notifications when price hits target
- [ ] Monitor multiple cryptocurrencies simultaneously (using threading)
- [ ] Show price history (last 10 prices checked)
- [ ] Create a database to track price history

### Advanced Improvements:
- [ ] Create a web dashboard using Flask or Django
- [ ] Deploy to the cloud (Heroku, AWS, DigitalOcean)
- [ ] Add machine learning to predict price movements
- [ ] Create a mobile app version
- [ ] Add real-time WebSocket support instead of polling

---

## 📝 License

This project is open source and available under the MIT License.

---

## 🤝 Contributing

Got improvements or bug fixes? Great! Here's how to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -m "Add improvement"`)
5. Push to the branch (`git push origin feature/improvement`)
6. Open a Pull Request

---

## ❓ Troubleshooting

### Problem: "ModuleNotFoundError: No module named 'requests'"
**Solution:** Run `pip install -r requirements.txt` again

### Problem: "Invalid coin ID"
**Solution:** Visit https://api.coingecko.com/api/v3/coins/list to find the correct ID

### Problem: "ConnectionError"
**Solution:** Check your internet connection and try again

### Problem: Price checks aren't showing
**Solution:** Price updates appear every 5 seconds. Wait a moment and check your terminal!

### Problem: Alert didn't show up even though price should have hit target
**Solution:** Make sure you set the right alert type (1 for above, 2 for below). The exact price might not match due to API delays.

---

## 📧 Questions or Issues?

If you have questions:
- Check the README again (it has lots of info!)
- Read the comments in `main.py`
- Search for similar issues in GitHub Issues
- Feel free to create a new GitHub Issue with details

---

## ⭐ Show Your Support

If you found this project helpful, please give it a ⭐ on GitHub! It helps others discover the project.

---

**Happy monitoring! 🚀**

