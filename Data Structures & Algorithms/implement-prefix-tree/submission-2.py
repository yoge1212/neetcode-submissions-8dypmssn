class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfWord = False
         
class PrefixTree:
    #my thought process for this is to have a hashtable 
    #each key in this hashtable would be some kind of prefix
    #and its values would be a list words that begin with this prefix
    #that way we can efficently locate a list of words that potentially start with a prefix
    #and search would function the same way we take the word we are searching for get its prefix
    #look thorgh the hashmap for that prefix and its list of words to see if there are any matches

    def __init__(self):
        self.root = TrieNode()
        

        

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]
        
        curr.endOfWord = True


    def search(self, word: str) -> bool:

        curr = self.root

        for c in word:
            if c not in curr.children:
                return False

            curr = curr.children[c]
        
        return curr.endOfWord

        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return True

        
        