class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for current in nums:
                if current in seen:
                    return True
                seen.add(current)
        return False