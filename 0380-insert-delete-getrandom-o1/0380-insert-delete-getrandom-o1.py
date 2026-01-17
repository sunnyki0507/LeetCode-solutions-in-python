class RandomizedSet(object):

    def __init__(self):
        self.random = []
        

    def insert(self, val):
        if val not in self.random:
            self.random.append(val)
            return True
        else:
            return False
        """
        :type val: int
        :rtype: bool
        """
        
    def remove(self, val):
        if val not in self.random:
            return False
        else:
            self.random.remove(val)
            # idx = self.random.index(val)
            # self.random.pop(idx)
            return True

        """
        :type val: int
        :rtype: bool
        """
        

    def getRandom(self):
        return random.choice(self.random)
        """
        :rtype: int
        """
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()