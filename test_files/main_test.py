from inspect import signature
from pydoc import cli
import hashlib

import client
import transactions
import block
import failed_pickle_approach.blockchain as blockchain
import failed_pickle_approach.transaction_pool as transaction_pool

# 1. instantiate blockchain

PyCoins_chain = blockchain.Blockchain()
#miner1 = miner.Miner()
# pool = transaction_pool.TransactionPool()
pool = transaction_pool.TransactionPool()
#pool.clear_transactions()
#PyCoins_chain.reset_blockchain()

# # defining global variable for last_block hash which is needed for each new block's previous_block_hash
# if len(PyCoins_chain.retr_blockchain()) > 0:
#     last_block_hash = PyCoins_chain.retr_blockchain()[-1].retrieve_block()[2] # setting the last_block_hash as the Nonce of the last Block
# else:
#   last_block_hash = ""
#   ## creating genesis block
#   t0 = transactions.Transaction("Genesis",Vincent.identity,float(69000))

last_block_hash = ""

Jakob = client.Client()
Jakob.change_balance(69000.0)
Vincent = client.Client()
Lia = client.Client()
Costanza = client.Client()
miner1 = client.Client()

clients = [Jakob, Vincent, Lia, Costanza]

new_transaction = transactions.Transaction(Jakob.identity,Vincent.identity,float(69000)) # initiate transaction
for i in clients: # identify sender
    if i.identity == new_transaction.sender:
        client_obj = i
trans_signature = new_transaction.sign_transaction(client_obj) # sign transaction
if miner1.verify_transaction(client_obj, new_transaction,trans_signature) == True:
    new_transaction.display_transaction()
    pool.add_to_transaction_pool(new_transaction)
    print('Valid transaction')
    print(len(pool.retr_transaction_pool()))
else:
    print('Invalid transaction')
if len(pool.retr_transaction_pool()) == 2:
    new_block = block.Block()
    new_block.mine_block(pool.retr_transaction_pool(),last_block_hash, miner1.mine(new_block))
    PyCoins_chain.chain_block(new_block)
    pool.clear_transactions()
    miner1.change_balance(10)
    print('transactions: '+ str(len(pool.retr_transaction_pool())) + ', miner balance: ' + str(miner1.retrieve_balance()))
else:
    print('transactions: '+ str(len(pool.retr_transaction_pool())) + ', miner balance: ' + str(miner1.retrieve_balance()))




# block0 = block.Block()
# block0.previous_block_hash = None
# Nonce = None

# block0.verified_transactions.append(t0)
# digest = hash(block0)
# last_block_hash = digest

# ## creating the blockchain
# PyCoins = []

# def dump_blockchain(chain):
#     print ("Number of blocks in the chain: " + str(len (chain)))
#     for x in range (len(PyCoins)):
#         block_temp = PyCoins[x]
#         print ("block # " + str(x))
#     for transaction in block_temp.verified_transactions:
#         transaction.display_transaction()
#         print ('--------------')
#         print ('=====================================')

# PyCoins.append(block0)


# ## adding mining functionality
# def sha256(message):
#     return hashlib.sha256(message.encode('ascii')).hexdigest()

# def mine(message, difficulty=1):
#     assert difficulty >= 1
#     prefix = '1' * difficulty
#     for i in range(100000):
#         digest = sha256(str(hash(message)) + str(i))
#         if digest.startswith(prefix):
#             print ("after " + str(i) + " iterations found nonce: "+ digest)
#             return digest
#     print('Calculation is too complex for given constraints.')

# mine("test message", 6)

# last_transaction_index = 0 #tracking number of messages already mined
# t1 = transactions.Transaction(Vincent.identity,Lia.identity,float(6900))

# ## miner creates new block
# block1 = block.Block()
# block1.verified_transactions.append(t1)
# block1.previous_block_hash = last_block_hash
# block1.Nonce = mine(block1, 2)

# digest = hash(block1)
# PyCoins.append(block1)
# last_block_hash = digest


# last_transaction_index += 1
# last_transaction_index += 1