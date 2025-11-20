class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m=Counter(nums1)
        result=[]
        for i in nums2:
            if m[i]>0:
                result.append(i)
                m[i]-=1
        return result
        