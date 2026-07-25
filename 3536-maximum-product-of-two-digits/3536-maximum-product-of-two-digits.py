class Solution:
    def maxProduct(self, n: int) -> int:
        my_list = [int(i) for i in str(n)]
        my_list.sort()
        result=my_list[len(my_list)-1] * my_list[len(my_list)-2]
        return result
       
        