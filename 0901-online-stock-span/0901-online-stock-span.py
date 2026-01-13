class StockSpanner(object):

    def __init__(self):
        self.past = []
        self.stack = []
        self.nextB = []
        self.idx = None
        

    def next(self, price):
        self.past.append(price)
        if self.idx is None:
            self.idx = 0
        else:
            self.idx += 1
        if len(self.past) == 1:
            self.stack.append(self.idx)
            self.nextB.append(0)
            return 1
        length = len(self.past)
        self.nextB.append(0)
        while self.stack and self.past[self.stack[-1]] <= price:
            self.nextB[self.stack.pop()] = price
        self.stack.append(self.idx)
        
        # print("Hi")
        # print(self.stack)
        # print(self.nextB)
        #///////////
        # nextB.pop()
        # if 0 not in nextB:
        #     return len(nextB) + 1
        # nextB.reverse()
        # zero = nextB.index(0)
        #/////////////
        if len(self.stack) < 2:
            return len(self.nextB)
        first = self.stack[-1]
        return first - self.stack[len(self.stack) - 2]


        
        """
        :type price: int
        :rtype: int
        """
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)