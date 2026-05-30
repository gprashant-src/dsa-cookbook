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
            if ch not in node.child:
                node.child[ch] = Node()
            
            node = node.child[ch]
        
        node.end = True
    
    def search(self, word:str):
        node = self.root

        for ch in word:
            if ch not in node.child:
                # node.child[ch] = Node()
                return False
            
            node = node.child[ch]
        
        return node.end

    def prefix(self, word:str):
        node = self.root

        for ch in word:
            if ch not in node.child:
                # node.child[ch] = Node()
                return False
            
            node = node.child[ch]
        
        return True