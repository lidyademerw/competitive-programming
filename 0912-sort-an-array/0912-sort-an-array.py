class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def mergeSort(nums):
            if len(nums)<=1:
                return nums
            mid=len(nums)//2
            left=nums[:mid]
            right=nums[mid:]
            leftSort=mergeSort(left)
            rightSort=mergeSort(right)
            return merg(leftSort, rightSort)
        def merg(left,right):
            res=[]
            i=0
            j=0
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    res.append(left[i])
                    i+=1
                else:
                    res.append(right[j])
                    j+=1
            res.extend(left[i:])
            res.extend(right[j:])
            return res
        return mergeSort(nums)
        