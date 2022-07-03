import pickle # used to store and retrieve Python objects

class Blockchain:
    def __init__(self) -> None:
        '''instantiates Blockchain object'''
        self.__chain = [] 
    
    def retr_blockchain(self) -> list:
        '''takes no arguments and returns all block objects in a list'''
        with open('blockchain_file', 'rb') as blockchain_file:
            # unpickling every object in the file, each unpickling operation unpickles just one object at a time 
            try:
                while True:
                    self.__chain.append(pickle.load(blockchain_file))
            except EOFError:
                pass
            return self.__chain

    def chain_block(self, block: object) -> None:
        '''takes a block object as argument and appends it to block object'''
        with open('blockchain_file', 'ab+') as blockchain_file:
            pickle.dump(block, blockchain_file)
    
    def reset_blockchain(self) -> None:
        '''takes no arguments and cleans the blockchain file'''
        with open('blockchain_file', 'wb') as blockchain_file:
            pickle.dump([], blockchain_file)