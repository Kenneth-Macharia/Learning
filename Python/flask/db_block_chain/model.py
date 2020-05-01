import os, shelve
from pymongo import MongoClient
import hashlib
import json
import requests
from time import time
from uuid import uuid4
from urllib.parse import urlparse


class BlockChainModel:

    def __init__(self, host, database_name, collection_name):
        '''
        Sets up a MongoDB connection object to the collection of interest
        Collections are similar to SQL tables and documents are similar to SQL records
        '''

        # Set up database connection
        self.client = MongoClient(host, 27017)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

        # Creating seed block
        try:
            self.get_chain().next()
        except:
            self.new_block(proof=1000, previous_hash=1, index=1)

    def new_block(self, proof, previous_hash=None, index=None):
        '''
        Create a new Block in the Blockchain
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        '''

        block = {
            'index': index or self.last_block_index() + 1,
            'timestamp': time(),
            'transactions': self.fetch_new_transaction(),
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.last_block()),
            'type': 'block'
        }

        # Append new block to the database
        self.collection.insert_one(block)
        return block

    def save_new_transaction(self, sender, recipient, amount):
        '''
        Creates a new transaction to go into the next mined Block. Temporarily persisted to a text file before the destination block is forged.

        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        '''

        tempfile = shelve.open(rf'{os.getcwd()}/temp', writeback=True)
        transactions = []

        trn = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }

        transactions.append(trn)

        if 'transactions' in list(tempfile.keys()):
            tempfile['transactions'].append(transactions)
        else:
            tempfile['transactions'] = transactions

        tempfile.close()
        return self.last_block_index() + 1

    def fetch_new_transaction(self):
        '''
        Fetches the new transaction when a new block is being .

        :return: <list> The new transaction list
        '''

        transactions = []
        tempfile = shelve.open(rf'{os.getcwd()}/temp')

        try:
            transactions = tempfile['transactions']
            del tempfile['transactions']

        except:
            tempfile.close()

        return transactions

    def last_block(self):
        '''
        Returns the last Block in the chain
        '''

        block_indices = []

        for block in self.get_chain():
            block_indices.append(block['index'])

        return self.collection.find_one({"index": max(block_indices)})

    def last_block_index(self):
        '''
        Returns the index of the last Block in the chain
        '''

        last_block = self.last_block()
        return last_block['index']

    def get_chain(self):
        '''
        Returns the entire block_chain
        '''

        return self.collection.find({"type":"block"})

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block
        :param block: <dict> Block
        :return: <str>
        """

        # dumps() deserializes json into str
        # encode() turns str to unicode
        # hexdigest() return block hash in hexadecimal digits
        # The block dictionary should be ordered, or the hashes will be inconsistent.

        del block['_id']
        block_str = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_str).hexdigest()

    def proof_of_work(self, last_proof):
        '''
        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains 4 leading zeroes
         - p is the previous proof, and p' is the new proof
        :param last_proof: <int>
        :return: <int>
        '''

        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        '''
        Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> True if correct, False if not.
        '''

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == '0000'

    def valid_chain(self, chain):
        '''
        Determines if a given blockchain is valid
        :param chain: <list> A blockchain
        :return: <bool> True if valid, False if not
        '''

        doc_list = []
        curr = self.collection.find({})

        for document in curr:
            doc_list.append(document)

        last_block = doc_list[0]
        current_index = 1

        while current_index < len(doc_list):
            block = doc_list[current_index]

            # Check that the hash of the block is correct
            if block['previous_hash'] != self.hash(last_block):
                return False

            # Check that the Proof of Work is correct
            if not self.valid_proof(last_block['proof'], block['proof']):
                return False

            last_block = block
            current_index += 1

        return True

    def register_node(self, name, address):
        '''
        Adds a new node to the list of nodes
        :param address: <str> Address of node. Eg. 'http://192.168.0.5:5000'
        :return: None
        Adds to a set to ensure idempotence - regardless of the number of times anode is added, it will appear only once.
        '''

        parsed_url = urlparse(address).netloc

        if not self.collection.find_one({"address":parsed_url}):
            node = {
                'name': name,
                'address': parsed_url,
                'type': 'node'
            }

            self.collection.insert_one(node)

    def get_nodes(self):
        '''
        Returns all nodes in the network
        '''

        return self.collection.find({"type":"node"})

    def resolve_conflicts(self):
        '''
        This is our Consensus Algorithm, it resolves conflicts
        by replacing our chain with the longest one in the network.
        :return: <bool> True if our chain was replaced, False if not
        '''

        neighbour_nodes = self.collection.find({"type":"node"})
        new_chain = None

        # We're only looking for chains longer than ours
        max_length = self.collection.count_documents({"type":"block"})

        # Grab and verify the chains from all the nodes in our network
        for node in neighbour_nodes:
            response = requests.get(f'http://{node["address"]}/chain')

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

            # Check if the length is longer and the chain is valid
            if length > max_length and self.valid_chain(chain):
                max_length = length
                new_chain = chain

        # Replace our chain if we discovered a new, valid chain longer than ours
        if new_chain:
            self.collection.delete_many({"type":"block"})

            for block in new_chain:
                self.collection.insert_one(block)

            return True

        return False