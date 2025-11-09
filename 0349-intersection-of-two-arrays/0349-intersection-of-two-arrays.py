class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x=set(nums1)
        y=set(nums2)
        m=[]
        for i in x:
            for j in y:
                if i==j:
                    m.append(i)
        return(m)
        