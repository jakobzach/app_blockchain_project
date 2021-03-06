class Block:
    def __init__(self) -> None:
        '''takes no inputs and does not return anything, but instantiates a block object'''
        self.__verified_transactions = [] # list of transactions the miner verified
        self.__previous_block_hash = "" # for traceability between blocks
        self.__Nonce = "" # the miner's proof of work (in our (simplified) case serves also as the new block's hash)

    # mutator – mining method
    def mine_block(self, transactions: list, hash: str, nonce: str) -> None:
        '''takes a list of transactions, a hash string and a nonce string, does not return anything'''
        self.__verified_transactions = transactions
        self.__previous_block_hash = hash
        self.__Nonce = nonce
    
    # accessor
    def retrieve_block(self) -> list:
        '''takes no inputs and returns a list with items in this order: list of block's transactions, previous block's hash and this block's Nonce'''
        return self.__verified_transactions, self.__previous_block_hash, self.__Nonce