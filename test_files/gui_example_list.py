from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

# create the root window
root = Tk()
root.title('Listbox')

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# create a list box
langs = ('Java', 'C#', 'C', 'C++', 'Python',
        'Go', 'JavaScript', 'PHP', 'Swift')

langs_var = StringVar(value=langs)

listbox = Listbox(mainframe,listvariable=langs_var,selectmode='extended')

listbox.grid(column=2,row=4)

root.mainloop()
