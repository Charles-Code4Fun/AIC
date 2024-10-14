# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from lib.blockchain_lib import Blockchain

app = Flask(__name__)
CORS(app)

blockchain = Blockchain()

# Endpoint to upload data
@app.route('/upload_data', methods=['POST'])
def upload_data():
    json_data = request.get_json()
    sender = json_data.get('sender')
    data = json_data.get('data')

    # Simulating a data upload
    blockchain.new_transaction(sender, "marketplace", data)

    # Simulating proof of work
    proof = 100  # In a real scenario, this would be calculated
    blockchain.new_block(proof)

    return jsonify({
        'message': 'Data uploaded successfully',
        'block_index': blockchain.last_block['index'],
        'data': blockchain.last_block['transactions']
    }), 201

# Endpoint to get all data
@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify({
        'data': blockchain.chain
    }), 200

# Endpoint to access specific data
@app.route('/access_data/<int:block_index>', methods=['GET'])
def access_data(block_index):
    if block_index < 1 or block_index > len(blockchain.chain):
        return jsonify({'error': 'Block not found'}), 404
    
    block = blockchain.chain[block_index - 1]
    return jsonify(block), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')  # Enable HTTPS
