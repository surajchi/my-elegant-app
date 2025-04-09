from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__, static_folder='../frontend', static_url_path='/')
CORS(app)

# Sample data (replace with DB later)
trades = [
    {"id": 1, "symbol": "XAUUSD", "profit": 45.2, "note": "Scalped gold"},
    {"id": 2, "symbol": "EURUSD", "profit": -20.5, "note": "Bad entry"},
]

# Serve frontend
@app.route('/')
def serve_index():
    return app.send_static_file('index.html')

# Serve JS/CSS if needed
@app.route('/<path:path>')
def serve_static(path):
    return app.send_static_file(path)

# API: Get all trades
@app.route('/api/trades', methods=['GET'])
def get_trades():
    return jsonify(trades)

# API: Add a new trade
@app.route('/api/trades', methods=['POST'])
def add_trade():
    data = request.get_json()
    new_trade = {
        "id": len(trades) + 1,
        "symbol": data.get("symbol"),
        "profit": data.get("profit"),
        "note": data.get("note")
    }
    trades.append(new_trade)
    return jsonify(new_trade), 201

# API: Export trades
@app.route('/api/export', methods=['GET'])
def export_trades():
    return jsonify({"message": "Exporting to CSV coming soon!"})

if __name__ == '__main__':
    app.run(debug=True)

