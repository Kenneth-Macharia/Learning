# Credit: https://hackernoon.com/learn-blockchains-by-building-one-117428612f46
import hashlib
import json
from time import time
from uuid import uuid4

class BlockChain:
    '''
    This class is responsible for managing the blockchain.
    It will store transactions and have some helper methods for adding new blocks to the chain
    '''

    def __init__(self):
        '''
        Creates an initial empty list (to store our blockchain), and another to store transactions
        '''

        self.chain = []
        self.current_transactons = []

        # Creatng genesis block
        self.new_block(proof=1000, previous_hash=1)

    def new_block(self, proof, previous_hash=None):
        '''
        Create a new Block in the Blockchain
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        '''

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactons,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]) # hash the latest
        }

        # Reset the current transaction list, in readisness for the next new block
        self.current_transactons = []

        # Append new loaded block to the list of blocks / blockchain
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        '''
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        '''

        self.current_transactons.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block
        :param block: <dict> Block
        :return: <str>
        """

        # dumps() deserializes jsoon into str
        # encode() turn turns str to unicode
        # hexdigest() return block hash in hexadecimal digits
        # The block dictionary should be ordered, or the hashes will be inconsistent.
        block_str = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_str).hexdigest()

    @property
    def last_block(self):
        '''
        Returns the last Block in the chain
        '''

        return self.chain[-1]

    def proof_of_work(self, last_proof):
        '''
        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(p*p') contains 4 leading zeroes
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
