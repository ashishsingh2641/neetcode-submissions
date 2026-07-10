class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_value = arr[len(arr) - 1]
        temp = 0
        arr[len(arr) - 1] = -1
        for val in range(len(arr) - 1, 0, -1):
            temp = arr[val -1]
            arr[val - 1] = max(right_value, arr[val])
            right_value = temp
        
        return arr