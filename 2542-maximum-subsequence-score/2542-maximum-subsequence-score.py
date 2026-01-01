class Solution(object):
    def maxScore(self, nums1, nums2, k):
        h = []
        total = result = 0

        for a,b in sorted(list(zip(nums1, nums2)), key = lambda ab: -ab[1]):
            heappush(h, a)
            total += a
            if len(h) > k:
                total -= heappop(h)
            if len(h) == k:
                result = max(result, total * b)
        return result

                

        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        