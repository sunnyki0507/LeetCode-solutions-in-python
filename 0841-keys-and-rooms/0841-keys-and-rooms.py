class Solution(object):
    def canVisitAllRooms(self, rooms):

        numOfArr = len(rooms)
        keys = [0] * numOfArr
        keys[0] = 1
        idx0 = rooms[0]
        vals = deque()
        if len(idx0) > 0:
            for i in range(len(idx0)):
                vals.append(idx0[i])
        visited = [0] * numOfArr
            
        while vals:
            idx = vals.popleft()
            if keys[idx] == 0:
                keys[idx] = 1
                tmp = rooms[idx]
                if len(rooms[idx]) > 0:
                    for j in range(len(tmp)):
                        if keys[tmp[j]] == 0:
                            vals.append(tmp[j])
        
        for i in range(numOfArr):
            if keys[i] == 0:
                return False

        return True



        # for i in range(len(idx0)):
        #     vals.append(idx0[i])
        
        # arr = []

        # while vals:
        #     while vals:
        #         idx = vals.popleft()
        #         arr.append()

        
        # for i in range(numOfArr):

        # numOfArr = len(rooms)
        # keys = [0] * numOfArr
        # for i in range(numOfArr):
        #     numKeys = rooms[i]
        #     if len(numKeys) > 0:
        #         for j in range(len(numKeys)):
        #             keys[numKeys[j]] = 1
        #     if i + 1 < numOfArr:
        #         if keys[i + 1] == 0:
        #             return False
        return True

        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        