"""
Crypto Price Alerter
A beginner-friendly Python application that monitors cryptocurrency prices
and alerts users when a target price is reached with real-time updates.
"""

import requests
import time
import sys
from datetime import datetime


def get_current_time():
    """
    Get the current time in a readable format.
    
    Returns:
        str: Current time as "HH:MM:SS"
    """
    return datetime.now().strftime("%H:%M:%S")


def fetch_price_from_markets(coin_id, vs_currency):
    """
    Fetch current price from the CoinGecko markets endpoint.
    """
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": vs_currency,
        "ids": coin_id,
        "order": "market_cap_desc",
        "per_page": 1,
        "page": 1,
        "sparkline": "false"
    }
    headers = {
        "Accept": "application/json",
        "User-Agent": "Crypto Price Alerter/1.0"
    }

    response = requests.get(url, params=params, headers=headers, timeout=5)
    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list) and len(data) > 0:
            current_price = data[0].get("current_price")
            if current_price is not None:
                return float(current_price)
        return None

    if response.status_code == 429:
        raise ValueError("rate_limit")
    if response.status_code in (502, 503, 504):
        raise ValueError("server_error")

    raise ValueError(f"status_{response.status_code}")


def fetch_price_from_simple(coin_id, vs_currency):
    """
    Fetch current price from the CoinGecko simple price endpoint.
    """
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": coin_id,
        "vs_currencies": vs_currency,
        "include_last_updated_at": "true"
    }
    headers = {
        "Accept": "application/json",
        "User-Agent": "Crypto Price Alerter/1.0"
    }

    response = requests.get(url, params=params, headers=headers, timeout=5)
    if response.status_code == 200:
        data = response.json()
        price = data.get(coin_id, {}).get(vs_currency)
        if price is not None:
            return float(price)
        return None

    if response.status_code == 429:
        raise ValueError("rate_limit")
    if response.status_code in (502, 503, 504):
        raise ValueError("server_error")

    raise ValueError(f"status_{response.status_code}")


def fetch_crypto_price(coin_id, vs_currency):
    """
    Fetch the current price of a cryptocurrency from CoinGecko API.

    Args:
        coin_id (str): The ID of the cryptocurrency (e.g., 'bitcoin', 'ethereum')
        vs_currency (str): The target currency (e.g., 'usd', 'inr')

    Returns:
        float: The current price of the cryptocurrency, or None if API call fails
    """
    try:
        try:
            return fetch_price_from_markets(coin_id, vs_currency)
        except ValueError as api_error:
            error_code = str(api_error)
            if error_code == "rate_limit":
                print("❌ API Error: Too many requests on markets endpoint. Falling back to simple price endpoint.")
            elif error_code == "server_error":
                print("❌ API Error: CoinGecko markets endpoint is unavailable. Trying simple price endpoint.")
            else:
                print(f"❌ API Error: markets endpoint returned {error_code}. Trying simple price endpoint.")
            return fetch_price_from_simple(coin_id, vs_currency)

    except requests.exceptions.Timeout:
        print("❌ Error: API request timed out. Check your internet connection.")
        return None
    except requests.exceptions.ConnectionError:
        print("❌ Error: Unable to connect to the internet.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
        return None
    except ValueError as e:
        if str(e) == "rate_limit":
            print("❌ API Error: Too many requests. Please wait a moment and try again.")
            return None
        if str(e) == "server_error":
            print("❌ API Error: CoinGecko is temporarily unavailable. Try again in a few seconds.")
            return None
        print(f"❌ API Error: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error while fetching price: {e}")
        return None


def get_user_input():
    """
    Get and validate user input for crypto monitoring setup.
    
    Returns:
        tuple: (coin_id, vs_currency, target_price, alert_type) or None if input is invalid
    """
    print("\n" + "="*70)
    print("🔔 CRYPTO PRICE ALERTER - Real-Time Monitoring Setup")
    print("="*70 + "\n")
    
    # Step 1: Get cryptocurrency ID
    print("Step 1: Enter cryptocurrency ID")
    print("Examples: bitcoin, ethereum, cardano, ripple, dogecoin")
    coin_id = input("Enter coin ID: ").strip().lower()
    
    if not coin_id:
        print("❌ Coin ID cannot be empty!")
        return None
    
    # Step 2: Get target currency
    print("\nStep 2: Enter target currency")
    print("Examples: usd, inr, eur, gbp, jpy")
    vs_currency = input("Enter currency: ").strip().lower()
    
    if not vs_currency:
        print("❌ Currency cannot be empty!")
        return None
    
    # Step 3: Get target price
    print("\nStep 3: Enter target price")
    try:
        target_price = float(input("Enter target price: "))
        if target_price < 0:
            print("❌ Price cannot be negative!")
            return None
    except ValueError:
        print("❌ Invalid price! Please enter a number.")
        return None
    
    # Step 4: Get alert type (above or below)
    print("\nStep 4: Choose alert condition")
    print("1. Alert when price is ABOVE target")
    print("2. Alert when price is BELOW target")
    
    alert_choice = input("Enter 1 or 2: ").strip()
    
    if alert_choice == "1":
        alert_type = "above"
    elif alert_choice == "2":
        alert_type = "below"
    else:
        print("❌ Invalid choice! Please enter 1 or 2.")
        return None
    
    return (coin_id, vs_currency, target_price, alert_type)



def validate_crypto_exists(coin_id, vs_currency):
    """
    Verify that the entered cryptocurrency exists on CoinGecko.
    
    Args:
        coin_id (str): The cryptocurrency ID to validate
        vs_currency (str): The currency to validate
    
    Returns:
        bool: True if the crypto exists, False otherwise
    """
    price = fetch_crypto_price(coin_id, vs_currency)
    
    if price is None:
        print(f"❌ Could not find cryptocurrency '{coin_id}' or currency '{vs_currency}'.")
        print("   Please check the coin ID and currency are valid.")
        return False
    
    return True


def check_alert_condition(current_price, target_price, alert_type):
    """
    Check if the current price meets the alert condition.
    
    Args:
        current_price (float): The current price of the cryptocurrency
        target_price (float): The target price set by the user
        alert_type (str): Either 'above' or 'below'
    
    Returns:
        bool: True if the alert condition is met, False otherwise
    """
    if alert_type == "above":
        return current_price >= target_price
    else:  # alert_type == "below"
        return current_price <= target_price


def format_price(price, currency):
    """
    Format price for nice display.
    
    Args:
        price (float): The price to format
        currency (str): The currency symbol or code
    
    Returns:
        str: Formatted price string
    """
    currency_symbols = {
        "usd": "$",
        "inr": "₹",
        "eur": "€",
        "gbp": "£",
        "jpy": "¥"
    }
    
    symbol = currency_symbols.get(currency.lower(), currency.upper())
    return f"{symbol} {price:,.2f}"


def ask_continue_monitoring():
    """
    Ask user if they want to continue monitoring after an alert.
    
    Returns:
        bool: True if user wants to continue, False if they want to exit
    """
    print("\nWhat would you like to do?")
    print("1. Continue monitoring")
    print("2. Exit")
    
    choice = input("Enter 1 or 2: ").strip()
    
    if choice == "1":
        return True
    elif choice == "2":
        return False
    else:
        print("❌ Invalid choice! Please enter 1 or 2.")
        return ask_continue_monitoring()  # Ask again if invalid input



def run_price_monitor(coin_id, vs_currency, target_price, alert_type):
    """
    Main loop that continuously monitors the crypto price and checks for alerts.
    Checks every 5 seconds and displays timestamps.
    
    Args:
        coin_id (str): The cryptocurrency ID
        vs_currency (str): The target currency
        target_price (float): The target price
        alert_type (str): Either 'above' or 'below'
    """
    print("\n" + "="*70)
    print("📊 MONITORING STARTED - Real-Time Price Tracking")
    print("="*70)
    print(f"Coin: {coin_id.upper()}")
    print(f"Target Currency: {vs_currency.upper()}")
    print(f"Target Price: {format_price(target_price, vs_currency)}")
    print(f"Alert Condition: Price {alert_type.upper()} target")
    print(f"Check Interval: Every 5 seconds")
    print("\n💡 Tip: Press Ctrl+C at any time to stop monitoring\n")
    print("-"*70)
    
    check_count = 0
    sleep_seconds = 5
    
    try:
        while True:
            # Fetch current price
            current_price = fetch_crypto_price(coin_id, vs_currency)
            
            if current_price is not None:
                check_count += 1
                current_time = get_current_time()
                formatted_price = format_price(current_price, vs_currency)
                
                # Display current check with timestamp
                print(f"[{current_time}] Check #{check_count}: {formatted_price}", end="")
                
                # Check if alert condition is met
                if check_alert_condition(current_price, target_price, alert_type):
                    print(" ⏰ TARGET REACHED!")
                    
                    # Show alert message
                    print("\n" + "🔔 "*25)
                    print(f"\n🎯 ALERT! {coin_id.upper()} price has gone {alert_type.upper()}!")
                    print(f"   Target Price: {format_price(target_price, vs_currency)}")
                    print(f"   Current Price: {formatted_price}")
                    print(f"   Time: {current_time}")
                    print("\n" + "🔔 "*25 + "\n")
                    
                    # Ask if user wants to continue or exit
                    if not ask_continue_monitoring():
                        print("\n👋 Thank you for using Crypto Price Alerter!")
                        sys.exit(0)
                    else:
                        print("\n📊 Continuing to monitor...\n")
                        print("-"*70)
                else:
                    print()  # New line for clean output

                # Reset retry delay after a successful fetch
                sleep_seconds = 5
            else:
                current_time = get_current_time()
                print(f"[{current_time}] ⚠️  Could not fetch price. Retrying in {sleep_seconds} seconds...")
                time.sleep(sleep_seconds)
                sleep_seconds = min(60, sleep_seconds * 2)
                continue
            
            # Wait before the next normal check
            time.sleep(sleep_seconds)
            
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\n\n" + "="*70)
        print("👋 Monitoring stopped by user")
        print("="*70)
        sys.exit(0)


def main():
    """
    Main function that orchestrates the entire application flow.
    """
    try:
        # Get user input
        user_input = get_user_input()
        
        if user_input is None:
            print("\n❌ Setup failed. Please restart and try again.")
            sys.exit(1)
        
        coin_id, vs_currency, target_price, alert_type = user_input
        
        # Validate that the cryptocurrency exists
        print("\n🔍 Validating cryptocurrency and currency...")
        if not validate_crypto_exists(coin_id, vs_currency):
            sys.exit(1)
        
        # Start monitoring
        run_price_monitor(coin_id, vs_currency, target_price, alert_type)
        
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        sys.exit(1)


# Entry point of the script
if __name__ == "__main__":
    main()
