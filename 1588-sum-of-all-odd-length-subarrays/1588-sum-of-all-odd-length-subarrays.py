class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        m=len(arr)
        sumx=0
        for i in range(1,m+1,2):
            for j in range(m-i +1):
                subarray=arr[j: j + i]
                sumx+= sum(subarray)
        return sumx

           