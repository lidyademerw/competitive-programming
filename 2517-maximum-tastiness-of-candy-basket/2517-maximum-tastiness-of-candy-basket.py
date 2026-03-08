class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        low=0
        high=price[-1]-price[0]
        x=0
        def check(mid):
            count = 1
            last=price[0]
            ind=0
            while ind < len(price) and count <k:
                if price[ind] - last >= mid:
                    count+=1
                    last=price[ind]
                ind+=1
            return count==k
        
        while low<=high:
            mid=(high+low)//2
            if check(mid):
                x=mid
                low=mid + 1
            else:
                high=mid-1
        return x


        