class SmallestInfiniteSet(object):

    def __init__(self):
        self.cur = 1
        self.heap = []
        # self.discarded = set()

    def popSmallest(self):
        if self.heap:
            x = self.heap[0]
            self.heap.remove(x)
            print(self.heap)
            return x
        x = self.cur
        self.cur += 1
        print(self.heap)
        return x
        """
        :rtype: int
        """
        
    def addBack(self, num):
        if num >= self.cur:
            print(self.heap)
            return
        length = len(self.heap)
        if not self.heap or self.heap[length-1] < num:
            self.heap.append(num)
            return
        prev = 0
        idx = -1
        for i in range(length):
            if self.heap[i] == num:
                print(self.heap)
                return
            if self.heap[i] > num and prev < num:
                idx = i
                print(idx)
                break
            prev = self.heap[i]
        self.heap.insert(idx,num)
        print(self.heap)
        """
        :type num: int
        :rtype: None
        """
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)