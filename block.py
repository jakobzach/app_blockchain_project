class Block:
    def __init__(self):
        self.__verified_transactions = []
        self.__previous_block_hash = ""
        self.__Nonce = ""

    ## add mining method
    # mutator
    def mine_block(self, transactions, hash, nonce):
        self.__verified_transactions = transactions
        self.__previous_block_hash = hash
        self.__Nonce = nonce
    
    # accessor
    def retrieve_block(self):
        return self.__verified_transactions, self.__previous_block_hash, self.__Nonce

    def __str__(self) -> str:
        return str(self.previous_block_hash) + '\n' + str(self.Nonce) + '\n' + str(self.verified_transactions)