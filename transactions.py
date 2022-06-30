# import libraries
import hashlib
import random
import string
import json
import binascii
import numpy as np
import pandas as pd
#import pylab as pl
import matplotlib
import matplotlib.pyplot as plt
import logging
import datetime
import collections

# following imports are required by PKI (Public Key Infrastructure - to create a globally unique identification for the client)
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

# Transactions class definition
class Transaction:
    # define the initialization of a transaction class 
    def __init__(self, sender, recipient, value):
        '''client will be able to send money to somebody - client can be both a sender or a recipient of money'''
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.time = datetime.datetime.now()

    def to_dict(self):
        '''entire transaction information accessible through a single variable'''
        if self.sender == "Genesis": # Genesis block contains the first transaction initiated by the creator of the blockchain
            identity = "Genesis"
        else:
            identity = self.sender.identity

        return collections.OrderedDict({
            'sender': identity,
            'recipient': self.recipient,
            'value': self.value,
            'time' : self.time})

    def sign_transaction(self):
        '''sign the above dictionary object using the private key of the sender'''
        private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key) # use the built-in PKI with SHA algorithm
        h = SHA.new(str(self.to_dict()).encode('utf8')) # use the built-in PKI with SHA algorithm
        return binascii.hexlify(signer.sign(h)).decode('ascii') # decode to get the ASCII representation for printing and storing it in our blockchain

    def display_transaction(self):
        '''using the dictionary keys, the various values are printed on the console'''
        dict = self.to_dict()
        print ("sender: " + dict['sender'])
        print ('-----')
        print ("recipient: " + dict['recipient'])
        print ('-----')
        print ("value: " + str(dict['value']))
        print ('-----')
        print ("time: " + str(dict['time']))
        print ('-----')

    def senderid(self):
        dict = self.to_dict()
        print (dict['sender'])