from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample data (replace with your actual data source)
items = [
    {"id": 1, "name": "Stylish Gadget", "description": "A sleek and modern gadget."},
    {"id": 2, "name": "Elegant Decor", "description": "Beautiful piece for your home."},
    {"id": 3, "name": "Premium Accessory", "description": "A high-quality accessory to complement your style."},
]

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"message": "Item not found"}), 404

@app.route('/api/items', methods=['POST'])
def create_item():
    data = request.get_json()
    if not data or 'name' not in data or 'description' not in data:
        return jsonify({"message": "Please provide name and description"}), 400
    new_item = {
        "id": len(items) + 1,
        "name": data['name'],
        "description": data['description']
    }
    items.append(new_item)
    return jsonify(new_item), 201

if __name__ == '__main__':
    app.run(debug=True)
    @app.route("/")
def home():
    return jsonify({"message": "Backend is live and running!"})
