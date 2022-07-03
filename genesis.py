# import all project classes
import client
import transactions
import transaction_pool
import blockchain

# this file generates the genesis transaction

# instantiate the necessary objects
PyCoins_chain = blockchain.Blockchain()
pool = transaction_pool.TransactionPool()
Jakob = client.Client()

pool.clear_transactions()
PyCoins_chain.reset_blockchain()

first_transaction = transactions.Transaction("Genesis",Jakob.identity,float(69000))
Jakob.change_balance(float(69000))
pool.add_to_transaction_pool(first_transaction)

print(pool.retr_transaction_pool())
print(PyCoins_chain.retr_blockchain())
print(len(pool.retr_transaction_pool()))
print(len(PyCoins_chain.retr_blockchain()))