from mimetypes import init
import json


class TransactionPool:
    def __init__(self) -> None:
        self.__transaction_pool = []
    
    def retr_transaction_pool(self):
        file = open('transaction_pool.txt', 'r')
        for line in file.readlines():
            self.__transaction_pool.append(line.rstrip('\n'))
            #file.read().split('\n')
        file.close()
        return self.__transaction_pool

    def add_to_transaction_pool(self, transaction):
        file = open('transaction_pool.txt','a')
        #self.__transaction_pool.append(transaction)
        #print(self.__transaction_pool)
        file.write(transaction+'\n')
        file.close()