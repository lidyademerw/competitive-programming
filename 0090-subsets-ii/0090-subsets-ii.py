class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=set([()])
        for num in nums:
            temp=[]
            for i in res:
                temp.append(list(i)+[num])
            for i in temp:
                res.add(tuple(i))
        return list(res)