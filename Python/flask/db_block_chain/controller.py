import json
from flask import Flask, request, jsonify
from uuid import uuid4
from .model import BlockChainModel


# Initialize the flask app
app = Flask(__name__)

# Initialize the back-end
blockchain = BlockChainModel('localhost', 'db_block_chain', 'col_default')

# Generate a globally unique address for this node
node_id = str(uuid4()).replace('-', '')

# The node endpoints
@app.route('/mine', methods=['POST'])
def mine():
    '''
    1. Calculates the Proof of Work
    2. Rewards the miner (us) by adding a transaction granting us 1 coin
    3. Forges the new Block by adding it to the chain
    '''

    # Run the proof of work algorithm to get the next proof
    last_block = blockchain.last_block()
    last_proof = last_block['proof']

    # Calculate the proof for the new block
    proof = blockchain.proof_of_work(last_proof)

    # Receive a reward for calculating the proof.
    # The sender is "0" to signify that this node has mined a new coin and is initializing a reward transaction in the blockchain.
    blockchain.save_new_transaction(sender=0, recipient=node_id, amount=1)

    # Forge the new Block by adding it to the chain
    previous_hash = blockchain.hash(last_block)
    new_block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': 'New Block Forged',
        'index': new_block['index'],
        'transactions': new_block['transactions'],
        'proof': new_block['proof'],
        'previous_hash': new_block['previous_hash']
    }

    return jsonify(response), 201

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    '''
    Create a new transaction for the request data to be added to the blockchain
    '''

    values = request.get_json()

    # Check that the required fields are in the POST'ed data`
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return "Missing values", 400

    # Else create a new transaction
    index = blockchain.save_new_transaction(values['sender'], values['recipient'], \
        values['amount'])

    response = {'Message': f'Transaction will be added to block number {index}'}

    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    '''
    Exposes the entire blockchain
    '''

    doc_List = []

    for document in blockchain.get_chain():
        del document['_id']
        doc_List.append(document)

    response = {
        'chain': doc_List,
        'length': len(doc_List)
    }

    return jsonify(response), 200

@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    '''
    Accepts a list of new nodes in the from of urls
    '''

    values = request.get_json()
    nodes = values.get('nodes')

    if not nodes:
        return "Error: Please supply a valid list of nodes", 400

    for node in nodes:
        blockchain.register_node(node['name'], node['address'])

    node_list = []

    for node in blockchain.get_nodes():
        del node['_id']
        node_list.append(node)

    response = {
        'message': 'New nodes have been added',
        'all_nodes': node_list
    }

    return jsonify(response), 201

@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()
    chain = []

    for block in blockchain.get_chain():
        del block['_id']
        chain.append(block)

    if replaced:
        response = {
            'message': 'Our chain was replaced',
            'new_chain': chain
        }

    else:
        response = {
            'message': 'Our chain is King',
            'chain': chain
        }

    return jsonify(response), 200