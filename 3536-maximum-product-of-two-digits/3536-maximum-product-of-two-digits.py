class Solution:
    def maxProduct(self, n: int) -> int:
        my_list = [int(i) for i in str(n)]
        two_largest = heapq.nlargest(2, my_list )
        max1, max2 = two_largest
        result = max1 * max2
        return result
        