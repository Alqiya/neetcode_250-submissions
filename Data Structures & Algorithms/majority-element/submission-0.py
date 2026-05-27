from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        strings = Counter(nums)
        for i in nums:
            if strings[i] >= len(nums)/2:
                return i
        return
        