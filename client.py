# following imports are required by PKI
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
import binascii

## Client class definition
class Client:
   def __init__(self):
      self.keyPair = RSA.generate(bits=1024)
      self.__public_key = self.keyPair.publickey()
      self.__balance = 0
      
   @property
   def identity(self):
      return binascii.hexlify(self.__public_key.exportKey(format='DER')).decode('ascii')
   
   # accessor
   def get_key(self):
      return self.keyPair, self.__public_key
      
   def retrieve_balance(self):
      return self.__balance
   
   def change_balance(self, amount):
      self.__balance += amount