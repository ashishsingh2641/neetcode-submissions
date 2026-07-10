class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        num_of_elemnt = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[num_of_elemnt] = nums[i]
                num_of_elemnt += 1
        return num_of_elemnt