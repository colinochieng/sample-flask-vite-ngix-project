from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory product store
products = []

@app.route('/products', methods=['GET'])
def get_products():
    """Return the list of products"""
    return jsonify(products), 200

@app.route('/products', methods=['POST'])
def add_product():
    """Add a new product"""
    data = request.json
    if not data.get('name') or not data.get('price'):
        return jsonify({'error': 'Name and Price are required'}), 400
    
    product = {
        'id': len(products) + 1,
        'name': data['name'],
        'price': data['price']
    }
    products.append(product)
    return jsonify(product), 201

if __name__ == '__main__':
    app.run(debug=True)
