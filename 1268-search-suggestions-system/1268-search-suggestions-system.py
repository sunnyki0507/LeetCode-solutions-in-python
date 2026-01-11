class Solution(object):
    def suggestedProducts(self, products, searchWord):
        def dfs(node, path):
            if "~" in node:
                self.addList.append("".join(path))
            for ch, nxt in node.items():
                if ch == "~":
                    continue
                path.append(ch)
                dfs(nxt, path)
                path.pop()  
        outcome = []
        trie = {}
        first = trie
        for w in products:
            trie = first
            for i in range(len(w)):
                if w[i] not in trie:
                    trie[w[i]] = {}
                trie = trie[w[i]]
            trie["~"] = {}
        string = ""
        self.addList = []
        self.element = []
        Not = False
        for ch in searchWord:
            string += ch
            trie = first
            for i in string:
                if i not in trie:
                    Not = True
                    continue
                trie = trie[i]
                self.element.append(i)
            if Not == True:
                outcome.append([])
                Not = False
                continue
            dfs(trie, self.element)
            self.addList.sort()
            first3 = self.addList[:3]
            outcome.append(first3)
            self.addList = [] 
            self.element = []                   
        return outcome

        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        