class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sortNums = sorted(nums)
        for i in range(0, len(sortNums) - 1):
            if sortNums[i] == sortNums[i+1]:
                return True
        return False