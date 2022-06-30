from matplotlib.font_manager import json_load
import transaction_pool
import transactions
import client

Vincent = client.Client()
Lia = client.Client()

pool = transaction_pool.TransactionPool()
t0 = transactions.Transaction("Genesis",Vincent.identity,float(69000))

#print(pool.retr_transaction_pool())
#pool.add_to_transaction_pool('test3')
#pool.add_to_transaction_pool(str(t0.to_dict()))

transes = pool.retr_transaction_pool()
for trans in transes:
    print("=============")
    print(trans)
    output = json_load(trans)

print(output)