# Currency Exchange API

This project is a simple RESTful API built using Flask, a Python web framework. It provides endpoints to retrieve currency rates and transaction information.

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

### Prerequisites

You'll need the following software installed on your machine:

- Python 3.x
- Flask (you can install it using `pip`)

### Installation

1. Clone the repository to your local machine using Git:

`git clone https://github.com/Binkitubo/currency-exchange-api.git`

2. Navigate to the project directory:

`cd currency-exchange-api`

3. Install the required packages using `pip`:

`pip install -r requirements.txt`

### Usage

1. Start the Flask development server:

`python app.py`

2. The API will now be running locally at `http://localhost:5000/`.

3. You can use a tool like `curl` or a web browser to access the different endpoints. Here are some example endpoints:

- Get all currency rates: [http://localhost:5000/currency_rates](http://localhost:5000/currency_rates)
- Get a currency rate by code (e.g., USD): [http://localhost:5000/currency_rates/USD](http://localhost:5000/currency_rates/USD)
- Get all transactions: [http://localhost:5000/transactions](http://localhost:5000/transactions)
- Get transactions by currency (e.g., USD): [http://localhost:5000/transactions/USD](http://localhost:5000/transactions/USD)
- Get transactions by SKU and currency (e.g., T2006 and USD): [http://localhost:5000/transactions/T2006/USD](http://localhost:5000/transactions/T2006/USD)

### Customization

You can customize the data in the `transactions` and `currency_rates` lists within the `app.py` file to match your requirements.

### Contributing

Contributions are welcome! If you find any issues or want to add new features, feel free to submit a pull request.


