import json
from flask import Flask, request, jsonify
from block_chain import BlockChain
from uuid import uuid4


# The Flask Node, enabling interacting with the blockchain on the web, over HTTP requests
app = Flask(__name__)

# Generate a globally unique address for this node
node_id = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = BlockChain()


@app.route('/mine', methods=['GET'])
def mine():
    '''
    1. Calculates the Proof of Work
    2. Rewards the miner (us) by adding a transaction granting us 1 coin
    3. Forges the new Block by adding it to the chain
    '''

    # Run the proof of work algorithm to get the next proof
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # Receive a reward for finding the proof. The sender is "0" to signify that this node has mined a new coin and is initializing a reward transaction in the blockchain
    blockchain.new_transaction(sender=0, recipient=node_id, amount=1)

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

    return jsonify(response), 200


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
    index = blockchain.new_transaction(values['sender'], values['recipient'], \
        values['amount'])

    response = {'Message': f'Transaction will be added to block number {index}'}
    return jsonify(response), 201


@app.route('/chain', methods=['GET'])
def full_chain():
    '''
    Exposes the entire blockchain
    '''

    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }

    return jsonify(response), 200

@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    '''
    Accepts a list of new nodes in the from of urls
    '''

    values = request.get_json()
    nodes = values.get('nodes')

    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400

    for node in nodes:
        blockchain.register_node(node)

    response = {
        'message': 'New nodes have been added',
        'total_nodes': list(blockchain.nodes)
    }

    return jsonify(response), 201

@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()

    if replaced:
        response = {
            'message': 'Our chain was replaced',
            'new_chain': blockchain.chain
        }

    else:
        response = {
            'message': 'Our chain is King',
            'chain': blockchain.chain
        }

    return jsonify(response), 200


if __name__ == "__main__":
    '''
    Usage:  1. Set app env variable: $ export FLASK_APP= <app name>
            2. Set the run environment to develpoment: $ export FLASK_ENV=development
            3. Set port: $ export FLASK_RUN_PORT= <desired port> (especially for multi-processes) other skip this step to run on default port 3000
            4. Run app: $ python app.py

            (NB) All above can be run as a single command:
            $ FLASK_APP=app FLASK_RUN_PORT=5000 FLASK_ENV=development flask run
    '''
    app.run(debug=True)
