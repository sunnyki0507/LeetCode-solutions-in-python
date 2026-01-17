class Solution(object):
    def jump(self, nums):
        count = 1
        length = len(nums)
        if length == 1:
            return 0
        add = []
        for i in range(length):
            add.append(i)
        dist = [x + y for x,y in zip(nums,add)]
        #[2,1,9,5,7,6,7,11]
        start = 0
        end = dist[0]
        reach = end
        while reach < (length-1):
            count += 1
            reach = max(dist[start:end+1])
            start = end + 1
            end = reach
        return count

            
            
        """
        :type nums: List[int]
        :rtype: int
        """