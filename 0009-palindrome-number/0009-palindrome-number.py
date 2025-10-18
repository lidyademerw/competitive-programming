class Solution:
    def isPalindrome(self, x: int) -> bool:
        m = ""
        for i in str(x):
            m = i + m
        if m == str(x):
            return True
        else:
            return False