from collections import defaultdict

class node:
    def __init__(self, val):
        self.val = val
        self.is_end = False
        self.children = {}


class Trie(object):

    def __init__(self):
        self.root = node(" ")
        

    def insert(self, word: str) -> None:
    #    if not word: return False
       cur = self.root

       for c in word:
        if(c in cur.children):
            cur = cur.children[c]
        else:
            new_node = node(c)
            cur.children[c] = new_node
            cur = new_node
        cur.is_end = True


                
                
    def search(self, word):

        cur = self.root

        for c in word:
            if(c in cur.children):
                cur = cur.children[c]
            else:
                return False
        return True



if __name__ == "__main__":
    t = Trie()
    t.insert("and")
    t.insert("anc")
    print(t.search("anc"))