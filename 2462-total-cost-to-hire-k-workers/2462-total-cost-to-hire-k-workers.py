class Solution(object):
    def totalCost(self, costs, k, candidates):
        total = 0
        hL = []
        hR = []
        if len(costs) <= (candidates * 2):
            h = []
            for i in range(len(costs)):
                heappush(h, costs[i])
            for j in range(k):
                c = heappop(h)
                total += c
            return total

        for i in range(candidates):
            heappush(hL,costs[i])
        for i in range(len(costs)-candidates, len(costs)):
            heappush(hR, costs[i])
        
        currL = candidates
        currR = len(costs) - candidates - 1
        hC = []


        for i in range(k):
            if hC:
                total += heappop(hC)
                continue
            l = heappop(hL)
            r = heappop(hR)

            if l <= r:
                heappush(hR, r)
                total += l
                heappush(hL, costs[currL])
                currL += 1
            else:
                heappush(hL, l)
                total += r
                heappush(hR, costs[currR])
                currR -= 1
            if currL > currR:
                hC = hL + hR
                heapify(hC)


            
        return total

        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        