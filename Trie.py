from collections import defaultdict

class node():
    def __init__(self, val = " "):
        self.val = val
        self.children = defaultdict(list)


class Trie:

    def __init__(self):
        self.root = node()
        # self.children = []
        

    def insert(self, word: str) -> None:
        # if not word: return False
        cur = self.root
        for c in word:
            # print(c)
            if len(cur.children) == 0:
                print("inserting")
                cur.children[ord(c)-97] = node(c)
            cur = cur.children[ord(c)-97]
                
                
        

    def search(self, word: str) -> bool:
        if not word: return False
        
        

    def startsWith(self, prefix: str) -> bool:
        pass
    
    



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


if __name__ == "__main__":
    t = Trie()
    t.insert("and")
    print(len(t.root.children))