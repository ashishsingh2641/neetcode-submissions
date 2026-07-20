class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)):
            j = 0
            if i + 1 < len(nums):
                j = i + 1
                if nums[i] == nums[j]:
                    return True
        return False