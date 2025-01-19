from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory storage for transactions (temporary; use a database in production)
transactions = []

# API to receive data from the Android app
@app.route('/api/transactions', methods=['POST'])
def add_transaction():
    data = request.json
    transactions.append(data)
    return jsonify({"message": "Transaction added successfully"}), 200

# API to fetch transaction data for the web portal
@app.route('/api/transactions', methods=['GET'])
def get_transactions():
    transactions = [
        {
            "date": "2025-01-19",
            "time": "06:30 PM",
            "amount": 1000,
            "utr_number": "123456789",
            "upi_id": "user@upi"
        }
    ]
    return jsonify(transactions)

if __name__ == "__main__":
    app.run(debug=True)