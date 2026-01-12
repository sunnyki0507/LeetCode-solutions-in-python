class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        outcome = 0
        length = len(intervals)
        intervals.sort(key=lambda x:x[1])

        end = intervals[0][1]
        for i in range(1, length):
            start = intervals[i][0]
            if end <= start:
                end = intervals[i][1]
            else:
                outcome += 1
        return outcome
            
            

                

        
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        