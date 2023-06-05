import sys
import requests

def checkifvalid():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    elif not isinstance(float(sys.argv[1]), float):
        sys.exit("Command-line argument is not a number")

def main():
    checkifvalid()
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        usd_rate = float(data["bpi"]["USD"]["rate_float"])
        input_value = float(sys.argv[1])
        result = usd_rate * input_value
        print(f"${result:,.4f}")
    except requests.RequestException as e:
        sys.exit(f"Error occurred during API request: {e}")
    except ValueError as e:
        sys.exit(f"Error occurred while parsing JSON response: {e}")

if __name__ == "__main__":
    main()
