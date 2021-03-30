from hashlib import sha256

class BlockChain:
    def __init__(self, data = [], nonce=0):
        self.data = {
            'prehash':0,
            'data':data,  # any objects
            'nonce':nonce # Number of once
        }
        
    def hash(self):
        """ Hash the object as a string """
        return sha256(repr(self.data).encode('utf-8')).hexdigest()
    
    def get(self):
        return self.data
    
    def generate(self, data=[], nonce=0):
        buff = self.get()
        
        self.data = {
            'prehash': self.hash(),
            'data': data,
            'nonce': nonce
        }
        
        return buff


if __name__=='__main__':
    test = BlockChain(data='abc', nonce=0)
    print(f'{test.hash()}: {test.get()}')

    test.generate(data=['abc','ABC'], nonce=999)
    print(f'{test.hash()}: {test.get()}')

    test.generate(data=['abc','ABC'], nonce=-1)
    for i in range(10):
        print(f'{test.hash()}: {test.generate(data=[None]*i, nonce=i)}')