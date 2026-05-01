class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res=[]
        x=set()
        for i in nums:
            if i in x:
                res.append(i)
            else:
                x.add(i)
            
        for j in range(1,len(nums)+1):
            if j not in nums:
                 res.append(j)
                 
        return list(res)


         
               
    


            

            
        