class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranknum={}
        x=sorted(arr)
        rank=1
        for i in range(len(arr)):
            if i >0 and x[i]>x[i-1]:
                rank+=1
            ranknum[x[i]]=rank
        for i in range(len(arr)):
            arr[i]=ranknum[arr[i]]
        return arr
            