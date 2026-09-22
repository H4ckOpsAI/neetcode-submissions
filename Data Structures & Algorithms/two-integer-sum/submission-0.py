class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,current in enumerate(nums):
            needed = target-current
            if needed in seen:
                return [seen[needed],i]
            seen[current] = i

        