from xmlrpc.client import Boolean
from Crypto.Hash import SHA256
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme

class Miner:
    def __init__(self) -> None:
        pass

    def verify_transaction(client: object, transaction: object, signature: str) -> Boolean:

        # testing for equality the hash provided by the sender against the hash generated by the miner using sender’s public key
        hash = SHA256.new(str(transaction.transaction_info_collector()).encode('utf8')) 
        verifier = PKCS115_SigScheme(client.get_key()[1])

        try:
            verifier.verify(hash, signature)
            print("Signature is valid.")
            #if 
            return True
        except:
            print("Signature is invalid.")
            return False

    def mine(message, difficulty=1):
        assert difficulty >= 1
        prefix = '1' * difficulty
        for i in range(1000):
            digest = SHA256(str(hash(message)) + str(i))
            if digest.startswith(prefix):
                print ("after " + str(i) + " iterations found nonce: "+ digest)
                return digest