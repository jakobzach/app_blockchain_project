# import libraries
import datetime

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
    def __init__(self, sender: str, recipient: str, value: float) -> None:
        '''takes client identities as strings for sender and recipient and a value as float, does not return anything, instantiates a transaction object'''
        # client will be able to send money to somebody - client can be both a sender or a recipient of money
        self.__sender = sender
        self.__recipient = recipient
        self.__value = value
        self.__time = datetime.datetime.now()

    def transaction_info_collector(self) -> dict:
        '''takes no inputs, returns a dict with all transaction info'''
        # entire transaction information accessible through a single variable
        if self.sender == "Genesis": # Genesis block contains the first transaction initiated by the creator of the blockchain
            identity = "Genesis"
        else:
            identity = self.__sender

        return {'sender': identity,
            'recipient': self.__recipient,
            'value': self.__value,
            'time' : self.__time}

    def sign_transaction(self, client_object: object) -> str:
        '''takes client object as input, returns a signature string'''
        # sign the above dictionary object using the private key of the sender
        hash = SHA256.new(str(self.transaction_info_collector()).encode('utf8')) # calculate the hash of the input (the transaction in our case)
        keyPair = client_object.get_key()[0] # get the key pair
        signer = PKCS115_SigScheme(keyPair) # sign the hash 
        signature = signer.sign(hash) # sign the hash
        return signature

    def display_transaction(self) -> None:
        '''takes no input, prints transaction details, no return'''
        # using the dictionary keys, the various values are printed on the console
        transaction_dict = self.transaction_info_collector()

        print ("sender: " + transaction_dict['sender'])
        print ('-----')
        print ("recipient: " + transaction_dict['recipient'])
        print ('-----')
        print ("value: " + str(transaction_dict['value']))
        print ('-----')
        print ("time: " + str(transaction_dict['time']))
        print ('-----')

    def trunc_identity(self, identity:str) -> str:
        '''takes no inputs, returns a string with the truncated id'''
        first7 = identity[0:7]
        last7 = identity[-7:]
        return f'{first7}...{last7}'

    def get_transaction_details(self, length:str='full') -> list:
        '''takes 'trunc' or 'full' as length input, returns list of items in this order: sender id, recipient id, value, timestamp'''
        transaction_dict = self.transaction_info_collector()
        if length == 'trunc': # checking for desired length of ids
            sender = self.trunc_identity(transaction_dict['sender'])
            recipient = self.trunc_identity(transaction_dict['recipient'])
        else:
            sender = transaction_dict['sender']
            recipient = transaction_dict['recipient']
        value = str(transaction_dict['value'])
        time = str(transaction_dict['time'])
        return sender, recipient, value, time

    