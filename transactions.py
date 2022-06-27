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
import crypto
import crypto.Random
from crypto.Hash import SHA
from crypto.PublicKey import RSA
from crypto.Signature import PKCS1_v1_5

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

# sign this dictionary object using the private key of the sender
def sign_transaction(self):
    private_key = self.sender._private_key
    signer = PKCS1_v1_5.new(private_key) # use the built-in PKI with SHA algorithm
    h = SHA.new(str(self.to_dict()).encode('utf8')) # use the built-in PKI with SHA algorithm
    return binascii.hexlify(signer.sign(h)).decode('ascii') # decode to get the ASCII representation for printing and storing it in our blockchain

