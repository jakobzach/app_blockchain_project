# import necessary libraries
from tkinter import *
from tkinter import ttk
import client
import transactions

Jakob = client.Client()
Vincent = client.Client()
t = transactions.Transaction(Jakob, Vincent.identity, 5.0 )
signature = t.sign_transaction()


# defining the calcualtion for the balance
def calculate(*args):
    try:
        value = float(amount.get())
        balance_change = float(balance.get())
        balance.set(int(balance_change - value))
    except ValueError:
        pass

# setting up the main application window
root = Tk()
root.title("Your crypto wallet")

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
ttk.Label(mainframe, textvariable=balance).grid(column=3, row=1, sticky=(W, E))
balance.set(int(100)) ##needs to change

# create variable to display wallet id of the sender
senderid = StringVar()
ttk.Label(mainframe, textvariable=senderid).grid(column=3, row=2, sticky=W)
senderid.set(t.senderid()) ##needs to change

# create "send" button that when pressed it performs the transaction
ttk.Button(mainframe, text="Send", command=calculate).grid(column=4, row=6, sticky=W)

# creating all remaining text labels
ttk.Label(mainframe, text="Your balance").grid(column=2, row=1, sticky=E)
ttk.Label(mainframe, text="Transaction info:").grid(column=1, row=3)
ttk.Label(mainframe, text="Send to").grid(column=2, row=4, sticky=E)
ttk.Label(mainframe, text="Pycoin amount").grid(column=2, row=5, sticky=E)


for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
receiver_entry.focus() # the cursor will start in that field, so users don't have to click on it before starting to type
root.bind("<Return>", calculate) # if a user presses the Return key it should call the "send" command



root.mainloop() # necessary for everything to appear onscreen and allow users to interact with it



