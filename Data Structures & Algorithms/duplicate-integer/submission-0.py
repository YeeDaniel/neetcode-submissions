class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setNum = set(nums)
        if len(setNum) < len(nums):
            return True
        return False