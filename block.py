class Block:
    def __init__(self):
        self.verified_transactions = []
        self.previous_block_hash = ""
        self.Nonce = ""

    ## add mining method

    def __str__(self) -> str:
        return str(self.previous_block_hash) + '\n' + str(self.Nonce) + '\n' + str(self.verified_transactions)