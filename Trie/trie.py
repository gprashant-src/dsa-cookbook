class Node:
    def __init__(self):
        self.child = {}
        self.end = False
    
class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        node = self.root

        for ch in word:
            idx = ord(ch) - ord("a")

            if node.child[idx] is None:
                node.child[idx] = Node()
            
            node = node.child[idx]
        
        node.end = True
    
    def search(self, word:str):
        node = self.root

        for ch in word:
            idx = ord(ch) - ord("a")

            if node.child[idx] is None:
                # node.child[idx] = Node()
                return False
            
            node = node.child[idx]
        
        return node.end

    def prefix(self, word:str):
        node = self.root

        for ch in word:
            idx = ord(ch) - ord("a")

            if node.child[idx] is None:
                # node.child[idx] = Node()
                return False
            
            node = node.child[idx]
        
        return True