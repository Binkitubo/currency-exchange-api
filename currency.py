from flask import Flask, jsonify

app = Flask(__name__)

# Sample currency rates
currency_rates = [
    {"from": "EUR", "to": "USD", "rate": "1.359"},
    {"from": "CAD", "to": "EUR", "rate": "0.732"},
    {"from": "USD", "to": "EUR", "rate": "0.736"},
    {"from": "EUR", "to": "CAD", "rate": "1.366"}
]

# Sample transactions
transactions = [
    {"sku": "T2006", "amount": "10.00", "currency": "USD"},
    {"sku": "M2007", "amount": "34.57", "currency": "CAD"},
    {"sku": "R2008", "amount": "17.95", "currency": "USD"},
    {"sku": "T2006", "amount": "7.63", "currency": "EUR"},
    {"sku": "B2009", "amount": "21.23", "currency": "USD"}
]

# Helper function to convert amount from one currency to another
def convert_currency(amount, from_currency, to_currency):
    rate = 1.0

    if from_currency != to_currency:
        for cr in currency_rates:
            if cr['from'] == from_currency and cr['to'] == to_currency:
                rate = float(cr['rate'])
                break
    
    return round(float(amount) * rate, 2)

""" 
# Currency conversion test
amount_to_convert = 150.00
source_currency = 'USD'
target_currency = 'EUR'

# Call the convert_currency function
converted_amount = convert_currency(amount_to_convert, source_currency, target_currency)

# Print the result
print(f"{amount_to_convert} {source_currency} is equal to {converted_amount} {target_currency}") 
"""

@app.route('/currency-rates', methods=['GET']) 
def get_all_currency_rates(): 
    return jsonify(currency_rates)

@app.route('/currency_rates/<string:currency_code>', methods=['GET'])
def get_currency_rate(currency_code):
    for cr in currency_rates:
        if cr['from'] == currency_code or cr['to'] == currency_code:
            return jsonify(cr)
    return jsonify({"message": "Currency not found"}), 404

app.run(host='0.0.0.0')