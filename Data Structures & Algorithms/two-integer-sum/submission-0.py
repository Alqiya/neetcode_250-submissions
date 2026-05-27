class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        value = 0
        for idx, num in enumerate(nums):
            value=target-num
            if value in seen:
                return [seen[value], idx]
            seen[num] = idx   
        return 