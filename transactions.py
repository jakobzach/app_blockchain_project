# import libraries
import hashlib
import random
import string
import json
import binascii
import numpy as np
#import pandas as pd
#import pylab as pl
import logging
import datetime
import collections

# following imports are required by PKI (Public Key Infrastructure - to create a globally unique identification for the client)
#import Crypto import Crypto.Random
#from Crypto.Hash import SHA
#from Crypto.PublicKey import RSA
#from Crypto.Signature import PKCS1_v1_5

# define the initialization of a transaction class 
def __init__(self, sender, recipient, value):
   self.sender = sender
   self.recipient = recipient
   self.value = value
   self.time = datetime.datetime.now()

