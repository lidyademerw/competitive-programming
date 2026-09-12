class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count=[0]*10
        res=[]
        for digit in digits:
            count[digit]+=1
        for i in range(100,999,2):
            h=i//100
            t=(i//10)%10
            u=i%10
            count[h]-=1
            count[t]-=1
            count[u]-=1
            if count[h]>=0 and count[t]>=0 and count[u]>=0:
                res.append(i)
            count[h]+=1
            count[t]+=1
            count[u]+=1
        return res

        