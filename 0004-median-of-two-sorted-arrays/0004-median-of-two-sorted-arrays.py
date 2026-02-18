class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        mer=nums1 + nums2
        mer.sort()
        k= len(mer)//2
        if len(mer)%2==0:
            su=mer[int(len(mer)/2)] + mer[int((len(mer)/2)-1)]
            return su/2
        else:
           return mer[k]

        