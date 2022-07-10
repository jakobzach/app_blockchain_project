import pickle # used to store and retrieve Python objects

class Blockchain:
    def __init__(self) -> None:
        '''instantiates Blockchain object'''
        self.__chain = [] 
    
    def retr_blockchain(self) -> list:
        '''takes no arguments and returns all block objects in a list'''
        with open('block_chain_file', 'rb') as block_chain_file:
            # unpickling every object in the file, each unpickling operation unpickles just one object at a time 
            try:
                while True:
                    self.__chain.append(pickle.load(block_chain_file))
            except EOFError:
                pass
            return self.__chain[1:]

    def chain_block(self, block: object) -> None:
        '''takes a block object as argument and appends it to block object'''
        with open('block_chain_file', 'ab+') as block_chain_file:
            pickle.dump(block, block_chain_file)
    
    def reset_blockchain(self) -> None:
        '''takes no arguments and cleans the blockchain file'''
        with open('block_chain_file', 'wb') as block_chain_file:
            pickle.dump([], block_chain_file)