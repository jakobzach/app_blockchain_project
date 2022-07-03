from numpy import block
import transaction_pool
import blockchain
import block
import client
import transactions

Jakob = client.Client()
Jakob.change_balance(69000.0)
Vincent = client.Client()

pool = transaction_pool.TransactionPool()
transactions = pool.retr_transaction_pool()
print(transactions[1:])



# Pychain = blockchain.Blockchain()
# print(Pychain.retr_blockchain())

# import pickle
# test = 'test'
# with open('transactions_file', 'wb') as transactions_file:
#     pickle.dump(test, transactions_file)

# chain = blockchain.Blockchain()
# block1 = block.Block()

# chain.chain_block(block1)