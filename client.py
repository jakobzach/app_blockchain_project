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
      random = Crypto.Random.new().read
      self._private_key = RSA.generate(1024, random)
      self._public_key = self._private_key.publickey()
      self._signer = PKCS1_v1_5.new(self._private_key)
      self.__balance = 0

   @property
   def identity(self):
      return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')
   
   def change_balance(self, amount):
      self.__balance += amount
   
   def retrieve_balance(self):
      return self.__balance
   
   def trunc_identity(self, identity:str):
      first7 = identity[0:6]
      last7 = identity[-6:]
      return f'{first7}...{last7}'
