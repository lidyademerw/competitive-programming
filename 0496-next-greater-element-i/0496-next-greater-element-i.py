class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater={}
        stack=[]
        for i in nums2:
            while stack and i> stack[-1]:
                x=stack.pop()
                greater[x]=i
            stack.append(i)
            res=[]
            for j in nums1 :
                if j in greater:
                    res.append(greater[j])
                else:
                    res.append(-1)
        return res



        