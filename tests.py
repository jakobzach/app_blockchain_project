from cgi import test
from numpy import block
import transaction_pool
import blockchain
import block
import client
import transactions

Jakob = client.Client()
Jakob.change_balance(69000.0)
Vincent = client.Client()
miner1 = client.Client()

last_block_hash = ""

pool = transaction_pool.TransactionPool()
#pool.clear_transactions()
testtransactions = pool.retr_transaction_pool()
print(testtransactions)

PyCoins_chain = blockchain.Blockchain()
print(PyCoins_chain.retr_blockchain()[0].retrieve_block()[0])

# if len(testtransactions) == 2:
#     new_block = block.Block()
#     new_block.mine_block(testtransactions,last_block_hash, miner1.mine(new_block))
#     PyCoins_chain.chain_block(new_block)
#     testchain = PyCoins_chain.retr_blockchain()
#     print(testchain)
#     #pool.clear_transactions()
#     miner1.change_balance(10)
#     print(miner1.retrieve_balance())
# else:
#     print(len(testtransactions))


# Pychain = blockchain.Blockchain()
# print(Pychain.retr_blockchain())

# import pickle
# test = 'test'
# with open('transactions_file', 'wb') as transactions_file:
#     pickle.dump(test, transactions_file)

# chain = blockchain.Blockchain()
# block1 = block.Block()

# chain.chain_block(block1)