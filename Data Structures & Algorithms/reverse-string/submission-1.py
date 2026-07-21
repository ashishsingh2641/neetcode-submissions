class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 1
        j = len(s)
        while i < j:
            temp = s[i - 1]
            s[i - 1] = s[j - 1]
            s[j - 1] = temp
            i += 1
            j -= 1