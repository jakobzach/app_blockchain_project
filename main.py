# import all necessary external libs
from distutils.command.build import build
from tkinter import *
from tkinter import ttk
from xmlrpc.client import boolean

from numpy import identity

# import all project classes
import client
import transactions
import block

# imports from the pickle approach that failed, for more see wallet copy.py in failed_pickle_approach
# from genesis import PyCoins_chain
# import transaction_pool
# import blockchain


def build_transaction_history(blocks: list) -> list:
    '''takes a list of block objects and returns a list of all transaction details'''
    transaction_history_list = []
    for item in blocks: # iterate through all blocks
        for record in item.retrieve_block()[0]: # iterate through all transactions of a block
            # in a real wallet implementation, we would filter the transactions that contain the wallet holder's ID here
            transaction_info = record.get_transaction_details('trunc')
            transaction_history_list.append(transaction_info)

    return transaction_history_list

def get_last_block_hash(blocks: list) -> str:
    '''takes a list of block objects and returns a string with the last block's hash'''
    return blocks[-1][2]

def trigger_transaction(recipient, amount, pool, last_block_hash, clients) -> None:
    '''takes recipient id string, amount as float, pool list of transactions, last_block_hash string and list of clients, returns nothing'''
    try:
        new_transaction_1 = transactions.Transaction(Jakob.identity,recipient.get(),float(amount.get())) # initiate transaction, not possible to store SHA in pickle, therefore storing just ID
        
        # identify sender using the sender's identity
        for i in clients: 
            if i.get_key()[1] == Jakob.get_key()[1]:
                sender_obj = i
        # identify client using the sender's identity
        for i in clients:
            if str(i.identity) == str(new_transaction_1.transaction_info_collector()['recipient']):
                recipient_obj = i

        trans_signature = new_transaction_1.sign_transaction(sender_obj) # sign transaction

        if miner1.verify_transaction(sender_obj, new_transaction_1,trans_signature) == True:
            recipient_obj.change_balance(float(amount.get())) # should actually only be done once the block is mined
            sender_obj.change_balance(float(amount.get())*-1) # update sender's balance
            pool.append(new_transaction_1) # add to list of transactions
            balance.set(Jakob.retrieve_balance()) # update GUI with new balance
            print('Valid transaction')
            print('Transaction count: '+ str(len(pool)))
        else:
            print('Invalid transaction')
        if len(pool)% 2 == 0: # transactions count per block is 2
            new_block = block.Block() # create a new block
            new_block.mine_block(pool[-2:],last_block_hash, miner1.mine(new_block)) # mine the new block
            # in a real application, miners would compete on who is first to solve the proof of work first with transactions from a pool
            PyCoins_chain.append(new_block) # add new block to chain
            miner1.change_balance(10) # reward miner for mining
            transactions_history.set(build_transaction_history(PyCoins_chain))
            last_block_hash = new_block.retrieve_block()[2] # update last_block_hash constant
            for i in clients:
                print('Balance of client ' + i.trunc_identity() + ': ' + str(i.retrieve_balance()))
        else:
            print('Transaction recorded. Not completed yet.')
    except ValueError:
        print('Input incorrect. Please add a PyCoin amount to the transaction.')
        pass
    except UnboundLocalError:
        print('Input incorrect. Please add a correct recipient ID to send PyCoins to.')



if __name__ == "__main__":
    # instantiate the necessary objects
    PyCoins_chain = []
    pool = []
    Jakob = client.Client()
    Vincent = client.Client()
    Lia = client.Client()
    Costanza = client.Client()
    miner1 = client.Client()

    # aggregate all clients
    clients = [Jakob, Vincent, Lia, Costanza, miner1]
    print('Client IDs:')
    for i in clients:
        if i.get_key()[1] != Jakob.get_key()[1]:
            print(i.identity) # print all other client ids, to have them as input to GUI

    # Genesis transaction
    first_transaction = transactions.Transaction("Genesis",Jakob.identity,float(69000))
    Jakob.change_balance(float(69000))
    pool.append(first_transaction)

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
    ttk.Button(mainframe, text="Send", command=lambda: trigger_transaction(recipient, amount, pool, last_block_hash, clients)).grid(column=5, row=6, sticky=W)

    # creating all remaining text labels
    ttk.Label(mainframe, text="Your balance").grid(column=2, row=1, sticky=E)
    ttk.Label(mainframe, text="Wallet id:").grid(column=2, row=2)
    ttk.Label(mainframe, text="Transaction info:").grid(column=1, row=3)
    ttk.Label(mainframe, text="Send to").grid(column=2, row=4, sticky=E)
    ttk.Label(mainframe, text="PyCoin amount").grid(column=2, row=5, sticky=E)
    ttk.Label(mainframe, text="Transaction history:").grid(column=1, row=7)

    # create a listbox for transactions history
    transactions_history = StringVar()
    listbox = Listbox(mainframe, listvariable=transactions_history).grid(column=2, columnspan=3, row=8, sticky=(W, E))
    transactions_history.set(build_transaction_history(PyCoins_chain))


    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

    recipient_entry.focus() # the cursor will start in that field, so users don't have to click on it before starting to type
    root.bind("<Return>", trigger_transaction) # if a user presses the Return key it should call the "send" command

    root.mainloop() # necessary for everything to appear onscreen and allow users to interact with it