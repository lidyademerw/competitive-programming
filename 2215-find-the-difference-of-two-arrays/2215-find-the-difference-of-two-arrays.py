class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        x1= set(nums1)
        x2=set(nums2)
        return [ list(x1-x2),list(x2-x1)]
       
        