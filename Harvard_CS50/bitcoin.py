import json
import requests
import sys

digit = 0.0000
# Testing output
# amount = 38761.0833

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    # Attempt to convert the second argument to Float
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a valid number")

    # Number input must be in format for instance 0.5, 1.5 NOT 0,5 OR 1,5 ETC.!!!
    if n >= digit:
    # GET from API in JSON
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # check if the request is successful

        values = response.json()
        dig_bitcoin_usd = values["bpi"]["USD"]["rate_float"]

        # Buying BitCoins from a command line as argument: n-times
        buy =  n * dig_bitcoin_usd

        print(f"You have bought BitCoins in amount: ${buy:,.4f}")

        # print(f"Current Bitcoin exchange rate in USD: {dig_bitcoin_usd}")

        # print(json.dumps(response.json(), indent=2))  # Prints All VALUES from API

    else:
        sys.exit("Command-line argument is not a number")

except ValueError:
    print("Command-line argument is not a number")

except requests.RequestException:
    sys.exit("Bad request")

# print(f"\n${amount:,.4f}")
