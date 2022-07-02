import transactions
import client
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
import hashlib
import transaction_pool
import pickle

Jakob = client.Client()
Vincent = client.Client()
Lia = client.Client()
Costanza = client.Client()

clients = [Jakob, Vincent, Lia, Costanza]

t = transactions.Transaction(Jakob.identity, Vincent.identity, 5.0)

print(t.get_transaction_details('trunc')[0])
print(t.get_transaction_details('trunc')[1])
print(t.get_transaction_details('trunc')[2])
print(t.get_transaction_details('trunc')[3])

#print(hex(sig))

for i in clients:
    if i.identity == t.sender:
        client_obj = i

print(client_obj)

sig = t.sign_transaction(client_obj) 

print(str(t.transaction_info_collector()).encode('utf8'))

def transaction_verifier(transaction, signature):
    for i in clients:
        if i.identity == transaction.sender:
            client_obj = i

    hash = SHA256.new(str(transaction.transaction_info_collector()).encode('utf8')) 
    verifier = PKCS115_SigScheme(client_obj.get_key()[1])
    try:
        verifier.verify(hash, signature)
        print("Signature is valid.")
    except:
        print("Signature is invalid.")


transaction_verifier(t, sig)

pool = transaction_pool.TransactionPool()

pool.add_to_transaction_pool(t)

for i in pool.retr_transaction_pool():
    print(i)

#transaction_pool.TransactionPool().clear_transactions()

#t1 = transactions.Transaction(Jakob, Vincent.identity, 15.0)
#t2 = transactions.Transaction(Jakob, Costanza.identity, 6.0)
#t3 = transactions.Transaction(Costanza, Vincent.identity, 2.0)
#t4 = transactions.Transaction(Vincent, Lia.identity, 4.0)


#pool = transaction_pool.TransactionPool()

#pool.add_to_transaction_pool(t1)

#for i in pool.retr_transaction_pool():
#    i.display_transaction()

def mine(message, difficulty=1):
    assert difficulty >= 1
    prefix = '1' * difficulty
    for i in range(1000):
        digest = SHA256(str(hash(message)) + str(i))
        if digest.startswith(prefix):
            print ("after " + str(i) + " iterations found nonce: "+ digest)
            return digest

#def create_block(digest, last_block_hash, verified_transacts):


#for i in transactions_recent.retr_transaction_pool():
#    i.display_transaction()
#    signa = i.sign_transaction()
#    transaction_verifier(i, signa)



#def create_block(transactions_recent):
