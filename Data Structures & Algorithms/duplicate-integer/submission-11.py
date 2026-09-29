class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lenSet = len(set(nums))
        lenList = len(nums)

        if lenSet == lenList:
            return False
        return True
