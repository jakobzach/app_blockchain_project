import client
import transactions

## Example 1: One transaction between two clients
Jakob = client.Client()
Vincent = client.Client()

t = transactions.Transaction(Jakob, Vincent.identity, 5.0 )
signature = t.sign_transaction() #sign this transaction using Jakob's (sender's) private key
t.display_transaction()


## Example 2: multiple transactions and clients
Jakob = client.Client()
Vincent = client.Client()
Lia = client.Client()
Costanza = client.Client()

transactions_list = [] # transaction queue to store all of the following transactions

t1 = transactions.Transaction(Jakob, Vincent.identity, 15.0 )
t1.sign_transaction() #sign this transaction using Jakob's (sender's) private key
transactions_list.append(t1) # add t1 to the transaction queue

t2 = transactions.Transaction(Jakob, Costanza.identity, 6.0 )
t2.sign_transaction()
transactions_list.append(t2) # add t2 to the transaction queue

t3 = transactions.Transaction(Costanza, Vincent.identity, 2.0 )
t3.sign_transaction()
transactions_list.append(t3) # add t3 to the transaction queue

t4 = transactions.Transaction(Vincent, Lia.identity, 4.0 )
t4.sign_transaction()
transactions_list.append(t4) # add t4 to the transaction queue

# blockchain managers may periodically like to review the contents of transaction queue
for transaction in transactions_list:
    '''iterate the transactions list and for each referenced transaction, call the display_transaction function'''
    transaction.display_transaction()
    print ('--------------')
