from mimetypes import init


class TransactionPool:
    def __init__(self) -> None:
        self.__transaction_pool = []
    
    def retr_transaction_pool(self):
        file = open('transaction_pool.txt', 'r')
        self.__transaction_pool= file.readline().rstrip('\n').split(',')
        return self.__transaction_pool

    def add_to_transaction_pool(self):
        pass