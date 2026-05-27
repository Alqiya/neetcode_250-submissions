from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        op=Counter(nums)
        for keys,val in op.items():
            if val>1:
                return True
        return False
        

        