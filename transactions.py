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
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme

# Transactions class definition
class Transaction:
    # define the initialization of a transaction class 
    def __init__(self, sender, recipient, value):
        '''client will be able to send money to somebody - client can be both a sender or a recipient of money'''
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.time = datetime.datetime.now()

    def transaction_info_collector(self):
        '''entire transaction information accessible through a single variable'''
        if self.sender == "Genesis": # Genesis block contains the first transaction initiated by the creator of the blockchain
            identity = "Genesis"
        else:
            identity = self.sender

        return {'sender': identity,
            'recipient': self.recipient,
            'value': self.value,
            'time' : self.time}

    def sign_transaction(self, client_object):
        '''sign the above dictionary object using the private key of the sender'''
        hash = SHA256.new(str(self.transaction_info_collector()).encode('utf8')) # calculate the hash of the input (the transaction in our case)
        keyPair = client_object.get_key()[0] # get the key pair
        signer = PKCS115_SigScheme(keyPair) # sign the hash 
        signature = signer.sign(hash) # sign the hash
        return signature

    def display_transaction(self):
        '''using the dictionary keys, the various values are printed on the console'''
        transaction_dict = self.transaction_info_collector() ## we should call this differently, naming a dictionary 'dict' is bad practice, becuse its a reserved word (dict() is used to initialize a dictionary for example)
        print ("sender: " + transaction_dict['sender'])
        print ('-----')
        print ("recipient: " + transaction_dict['recipient'])
        print ('-----')
        print ("value: " + str(transaction_dict['value']))
        print ('-----')
        print ("time: " + str(transaction_dict['time']))
        print ('-----')

    def trunc_identity(self, identity:str):
      first7 = identity[0:7]
      last7 = identity[-7:]
      return f'{first7}...{last7}'

    def get_transaction_details(self, length:str='full'):
        '''using the dictionary keys, the various values are printed on the console'''
        transaction_dict = self.transaction_info_collector()
        if length == 'trunc':
            sender = self.trunc_identity(transaction_dict['sender'])
            recipient = self.trunc_identity(transaction_dict['recipient'])
        else:
            sender = transaction_dict['sender']
            recipient = transaction_dict['recipient']
        value = str(transaction_dict['value'])
        time = str(transaction_dict['time'])
        return sender, recipient, value, time

    