class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        unique=10
        current=9
        avaliable=9
        for i in range(2,n+1):
            current=current*avaliable
            unique+=current
            avaliable-=1
        return unique