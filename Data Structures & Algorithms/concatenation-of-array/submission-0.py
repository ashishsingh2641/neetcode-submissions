class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [None] * (2 * len(nums))
        
        for i in range(len(nums)):
            ans[i] = nums[i]
        
        k = len(nums)
        j = len(nums)
        for i in range(k, len(ans)):
            ans[i] = nums[j - k]
            j += 1
        
        return ans