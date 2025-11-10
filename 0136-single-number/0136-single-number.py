class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        x=set()
        for item in nums:
            if item in x :
                x.remove(item)
            else:
                x.add(item)
        return x.pop()
        
        