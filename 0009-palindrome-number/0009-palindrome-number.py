class Solution:
    def isPalindrome(self, x: int) -> bool:
        m=""
        for i in str(x):
            m=i+m
        return m==str(x)

        