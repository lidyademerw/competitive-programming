class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        for i in nums1:
            found_i = False
            next_greater = -1
            for j in nums2:
                if i==j:
                     found_i = True
                if found_i  and j>i:
                    next_greater = j
                    break
            res.append( next_greater)

        return res


        