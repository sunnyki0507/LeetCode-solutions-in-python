

class Trie(object):
    def __init__(self):
        # self.val = val
        self.children = {}
        self.end = False

    def insert(self, word):
        node = self.children
        last = None
        if not word:
            return
        for ch in word:
            if ch not in node:
                node[ch] = Trie()
            last = node[ch]
            node = node[ch].children
        last.end = True
        """
        :type word: str
        :rtype: None
        """       

    def search(self, word):
        node = self.children
        last = None
        for ch in word:
            if ch not in node:
                print("Hello1")
                return False
            last = node[ch]
            node = node[ch].children

        print("Hello2")
        if last.end == True:
            return True
        return False
        """
        :type word: str
        :rtype: bool
        """
        

    def startsWith(self, prefix):
        node = self.children
        for ch in prefix:
            if ch not in node:
                print("Hello3")
                return False
            node = node[ch].children
        print("Hello4")
        return True
        """
        :type prefix: str
        :rtype: bool
        """

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)