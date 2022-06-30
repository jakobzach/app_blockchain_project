import client
import transactions
import block
import hashlib

# defining global variable for last_block hash which is needed for block class
last_block_hash = ""


## creating genesis block
Vincent = client.Client()

t0 = transactions.Transaction("Genesis",Vincent.identity,float(69000))

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


## adding mining functionality
def sha256(message):
    return hashlib.sha256(message.encode('ascii')).hexdigest()

def mine(message, difficulty=1):
    assert difficulty >= 1
    prefix = '1' * difficulty
    for i in range(100000):
        digest = sha256(str(hash(message)) + str(i))
        if digest.startswith(prefix):
            print ("after " + str(i) + " iterations found nonce: "+ digest)
            return digest
    print('Calculation is too complex for given constraints.')

mine("test message", 6)

last_transaction_index = 0 #tracking number of messages already mined

## miner creates new block
block1 = block.Block()

## need to have a class for an open transactions pool?


