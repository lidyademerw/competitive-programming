class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        x=[]
        for i in nums:
            if len(str(i))>1:
               x+= list(str(i))

            else:
                x+=str(i)
        return list(map(int,x))