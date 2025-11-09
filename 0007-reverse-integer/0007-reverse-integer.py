class Solution:
    def reverse(self, x: int) -> int:
        max_num=2**31-1
        min_num=-2**31

        m = 0
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        while x > 0:
            n = x % 10
            if m > max_num//10 or (m==max_num//10 and n>max_num%10):
             return 0
            m = n + 10 * m
            x = x // 10
        result=m*sign
        if not min_num <= result <= max_num:
                return 0 
        return result