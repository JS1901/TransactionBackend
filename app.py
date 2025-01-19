from flask import Flask, request, jsonify

app = Flask(__name__)

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
    return jsonify(transactions), 200

if __name__ == '__main__':
    app.run(debug=True)
