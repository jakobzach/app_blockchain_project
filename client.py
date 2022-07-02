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
   
   # accessor
   def get_key(self):
      return self.keyPair, self.__public_key

   @property
   def identity(self):
      return binascii.hexlify(self.__public_key.exportKey(format='DER')).decode('ascii')