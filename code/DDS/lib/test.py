

from flask import Flask, request, jsonify
from flask_cors import CORS
import hashlib
import json
import requests

app = Flask(__name__)
CORS(app)

# Simulating a simple blockchain structure
class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_data = []

        # Create the genesis block
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'transactions': self.current_data,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_data = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, data):
        self.current_data.append({
            'sender': sender,
            'recipient': recipient,
            'data': data,
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]


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
