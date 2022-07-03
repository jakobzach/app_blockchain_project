# import all necessary external libs
from distutils.command.build import build
from tkinter import *
from tkinter import ttk
from xmlrpc.client import boolean

# import all project classes
import client
import transactions
import transaction_pool
import block
import blockchain

def build_transaction_history(blocks: list) -> list:
    '''takes a list of block objects and returns a list of all transaction details'''
    transaction_history_list = []
    for item in blocks: # iterate through all blocks
        for record in item.retrieve_block()[0]: # iterate through all transactions of a block
            transaction_info = record.get_transaction_details('trunc')
            # filter block to find Jakob's transactions?
            transaction_history_list.append(transaction_info)

    return transaction_history_list

def get_last_block_hash(blocks: list) -> str:
    '''takes a list of block objects and returns a string with the last block's hash'''
    return blocks[-1][2]

def trigger_transaction(sender: str, recipient: str, amount: float) -> boolean:
    # aggregate all clients
    clients = [Jakob, Vincent, Lia, Costanza, miner1]

    new_transaction = transactions.Transaction(Jakob.identity,Vincent.identity,float(69000)) # initiate transaction
    
    # identify sender using the sender's identity
    for i in clients: 
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
        return True
    else:
        print('transactions: '+ str(len(pool.retr_transaction_pool())) + ', miner balance: ' + str(miner1.retrieve_balance()))
        return False



# defining the calcualtion for the balance
def calculate(*args):
    try:
        value = float(amount.get())
        Jakob.change_balance(-value)
        balance.set(int(Jakob.retrieve_balance()))
    except ValueError:
        pass

if __name__ == "__main__":
    # instantiate the necessary objects
    PyCoins_chain = blockchain.Blockchain()
    pool = transaction_pool.TransactionPool()
    Jakob = client.Client()
    Vincent = client.Client()
    Lia = client.Client()
    Costanza = client.Client()
    miner1 = client.Client()

    # defining global variable for last_block hash which is needed for first block's previous_block_hash
    last_block_hash = ""

    # setting up the main application window
    root = Tk()
    root.title("Jakob's crypto wallet")

    # creating a frame widget to hold the content of the interface
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # create widget to input the number for the amount we want to transfer
    amount = StringVar()
    amount_entry = ttk.Entry(mainframe, width=7, textvariable=amount)
    amount_entry.grid(column=3, row=5, sticky=(W, E))

    # create widget to input the recipient's id
    recipient = StringVar()
    recipient_entry = ttk.Entry(mainframe, width=7, textvariable=recipient)
    recipient_entry.grid(column=3, row=4, sticky=(W, E))

    # create widget that displays the resulting amount in the wallet after the transaction is made 
    balance = StringVar()
    balance.set(Jakob.retrieve_balance())
    ttk.Label(mainframe, textvariable=balance).grid(column=3, row=1, sticky=(W, E))

    # create variable to display wallet id of the wallet owner
    wallet_owner = StringVar()
    wallet_owner.set(Jakob.trunc_identity())
    ttk.Label(mainframe, textvariable=wallet_owner).grid(column=3, row=2, sticky=W)

    # create "send" button that when pressed it performs the transaction
    ttk.Button(mainframe, text="Send", command=calculate).grid(column=5, row=6, sticky=W)

    # creating all remaining text labels
    ttk.Label(mainframe, text="Your balance").grid(column=2, row=1, sticky=E)
    ttk.Label(mainframe, text="Wallet id:").grid(column=2, row=2)
    ttk.Label(mainframe, text="Transaction info:").grid(column=1, row=3)
    ttk.Label(mainframe, text="Send to").grid(column=2, row=4, sticky=E)
    ttk.Label(mainframe, text="PyCoin amount").grid(column=2, row=5, sticky=E)
    ttk.Label(mainframe, text="Transaction histroy:").grid(column=1, row=7)

    # create a listbox for transactions history
    transactions_history = StringVar()
    listbox = Listbox(mainframe, listvariable=transactions_history).grid(column=2, columnspan=3, row=8, sticky=(W, E))
    transactions_history.set(build_transaction_history(PyCoins_chain.retr_blockchain()))

    # record a new transaction
    if trigger_transaction(Jakob.identity,recipient,float(amount)) == True:
        transactions_history.set(build_transaction_history(PyCoins_chain.retr_blockchain()))

    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

    recipient_entry.focus() # the cursor will start in that field, so users don't have to click on it before starting to type
    root.bind("<Return>", calculate) # if a user presses the Return key it should call the "send" command

    root.mainloop() # necessary for everything to appear onscreen and allow users to interact with it