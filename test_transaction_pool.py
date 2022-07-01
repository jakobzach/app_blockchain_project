import transaction_pool
import transactions
import client

Vincent = client.Client()
Lia = client.Client()

pool = transaction_pool.TransactionPool()
t0 = transactions.Transaction("Genesis",Vincent.identity,float(69000))

pool.add_to_transaction_pool(t0)

print(pool.retr_transaction_pool())