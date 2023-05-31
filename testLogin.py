# Nelson Dane
# Script to check auto rsa logins
# Run this to make sure the accounts successfully log in

# Custom API libraries
from allyAPI import *
from fidelityAPI import *
from robinhoodAPI import *
from schwabAPI import *
from seleniumAPI import *
from tastyAPI import *
from tradierAPI import *

# Initialize .env file
load_dotenv()

# Check for environment variables
# Discord
if os.environ.get("DISCORD_TOKEN") is None:
    print("Discord token not found")
else:
    print(f"Discord token found {os.environ.get('DISCORD_TOKEN')}")
if os.environ.get("DISCORD_CHANNEL") is None:
    print("Discord channel not found")
else:
    print(f"Discord channel found {os.environ.get('DISCORD_CHANNEL')}")
# Ally
if os.environ.get("ALLY_CONSUMER_KEY") is None:
    print("Ally consumer key not found")
else:
    print(f"Ally consumer key found {os.environ.get('ALLY_CONSUMER_KEY')}")
if os.environ.get("ALLY_CONSUMER_SECRET") is None:
    print("Ally consumer secret not found")
else:
    print(f"Ally consumer secret found {os.environ.get('ALLY_CONSUMER_SECRET')}")
if os.environ.get("ALLY_OAUTH_TOKEN") is None:
    print("Ally oauth token not found")
else:
    print(f"Ally oauth token found {os.environ.get('ALLY_OAUTH_TOKEN')}")
if os.environ.get("ALLY_OAUTH_SECRET") is None:
    print("Ally oauth secret not found")
else:
    print(f"Ally oauth secret found {os.environ.get('ALLY_OAUTH_SECRET')}")
# Fidelity
if os.environ.get("FIDELITY_USERNAME") is None:
    print("Fidelity username not found")
else:
    print(f"Fidelity username found {os.environ.get('FIDELITY_USERNAME')}")
if os.environ.get("FIDELITY_PASSWORD") is None:
    print("Fidelity password not found")
else:
    print(f"Fidelity password found {os.environ.get('FIDELITY_PASSWORD')}")
# Robinhood
if os.environ.get("ROBINHOOD_USERNAME") is None:
    print("Robinhood username not found")
else:
    print(f"Robinhood username found {os.environ.get('ROBINHOOD_USERNAME')}")
if os.environ.get("ROBINHOOD_PASSWORD") is None:
    print("Robinhood password not found")
else:
    print(f"Robinhood password found {os.environ.get('ROBINHOOD_PASSWORD')}")
if os.environ.get("ROBINHOOD_TOTP") is None:
    print("Robinhood totp not found")
else:
    print(f"Robinhood totp found {os.environ.get('ROBINHOOD_TOTP')}")
# Schwab
if os.environ.get("SCHWAB_USERNAME") is None:
    print("Schwab username not found")
else:
    print(f"Schwab username found {os.environ.get('SCHWAB_USERNAME')}")
if os.environ.get("SCHWAB_PASSWORD") is None:
    print("Schwab password not found")
else:
    print(f"Schwab password found {os.environ.get('SCHWAB_PASSWORD')}")
if os.environ.get("SCHWAB_TOTP_SECRET") is None:
    print("Schwab totp secret not found")
else:
    print(f"Schwab totp secret found {os.environ.get('SCHWAB_TOTP_SECRET')}")
# Tradier
if os.environ.get("TRADIER_TOKEN") is None:
    print("Tradier token not found")
else:
    print(f"Tradier token found {os.environ.get('TRADIER_TOKEN')}")
# Tastytrade
if os.environ.get("TASTYTRADE_USERNAME") is None:
    print("Tastytrade username not found")
else:
    print(f"Tastytrade username found {os.environ.get('TASTYTRADE_USERNAME')}")
if os.environ.get("TASTYTRADE_PASSWORD") is None:
    print("Tastytrade password not found")
else:
    print(f"Tastytrade password found {os.environ.get('TASTYTRADE_PASSWORD')}")

# Check each account
print("==========================================================")
print("Checking Accounts...")
print("==========================================================")
print()
ally_init()
print()
fidelity_init()
print()
robinhood_init()
print()
schwab_init()
print()
tradier_init()
print()
tastytrade_init()
# Print results
print("==========================================================")
print("All checks complete")
print("==========================================================")
print()
