class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i=1
        while i**2<=num:
            if i**2==num:
                return True
            i=i+1
        else:
            return False
        