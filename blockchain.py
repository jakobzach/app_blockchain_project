import client
import transactions
import block

# defining global variable for last_block hash which is needed for block class
last_block_hash = ""


## creating genesis block
Vincent = client.Client()

t0 = transactions.Transaction("Genesis",Vincent.identity,69000)

block0 = block.Block()
block0.previous_block_hash = None
Nonce = None

block0.verified_transactions.append(t0)
digest = hash (block0)
last_block_hash = digest

## creating the blockchain
PyCoins = []

def dump_blockchain(chain):
    print ("Number of blocks in the chain: " + str(len (chain)))
    for x in range (len(PyCoins)):
        block_temp = PyCoins[x]
        print ("block # " + str(x))
    for transaction in block_temp.verified_transactions:
        transaction.display_transaction()
        print ('--------------')
        print ('=====================================')

PyCoins.append(block0)

dump_blockchain(PyCoins)