# import all necessary external libs
from tkinter import *
from tkinter import ttk

# import all project classes
import client
import transactions
import transaction_pool
import block
import blockchain

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

    # aggregate all clients
    clients = [Jakob, Vincent, Lia, Costanza, miner1]

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

    # create widget to input the receiver's id
    receiver = StringVar()
    receiver_entry = ttk.Entry(mainframe, width=7, textvariable=receiver)
    receiver_entry.grid(column=3, row=4, sticky=(W, E))

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
    #transactions_history.set(transaction_history_list) #filter block to find Jakob's transactions

    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

    receiver_entry.focus() # the cursor will start in that field, so users don't have to click on it before starting to type
    root.bind("<Return>", calculate) # if a user presses the Return key it should call the "send" command

    root.mainloop() # necessary for everything to appear onscreen and allow users to interact with it