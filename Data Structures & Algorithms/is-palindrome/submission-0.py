class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_old = "".join([char for char in s if char.isalnum()]).casefold()
        s_new =  ""
        for i in range(len(s_old) -1, -1, -1):
            s_new += s_old[i]
            
        if s_new == s_old:
            return True
        return False
        