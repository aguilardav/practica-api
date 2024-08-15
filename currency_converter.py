import requests

class CurrencyConverter:
    def __init__(self, bb9a6b2f8b06910fafba635f):
        self.api_key = bb9a6b2f8b06910fafba635f
        self.url = f"https://v6.exchangerate-api.com/v6/{bb9a6b2f8b06910fafba635f}/latest/"

    def get_exchange_rate(self, from_currency, to_currency):
        response = requests.get(self.url + from_currency)
        data = response.json()
        if response.status_code == 200:
            rates = data['conversion_rates']
            return rates.get(to_currency, None)
        else:
            print(f"Error: {data['error-type']}")
            return None