class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count=dict()
        for i in nums:
            if i not in count.keys():
                count[i]=1
            else:
                return True
        return False
        


        