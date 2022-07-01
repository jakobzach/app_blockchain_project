import pickle # used to store and retrieve Python objects

class TransactionPool:
    def __init__(self) -> None:
        '''instantiates TransactionPool object'''
        self.__transactions = [] 
    
    def retr_transaction_pool(self):
        '''takes no arguments and returns all transaction objects in a list'''
        with open('transactions_file', 'rb') as transactions_file:
            # unpickling every object in the file, each unpickling operation unpickles just one object at a time 
            try:
                while True:
                    self.__transactions.append(pickle.load(transactions_file))
            except EOFError:
                pass
            return self.__transactions

    def add_to_transaction_pool(self, transaction: object):
        '''takes a transaction object as argument and appends it to transaction pool'''
        with open('transactions_file', 'ab+') as transactions_file:
            pickle.dump(transaction, transactions_file)