class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        b={}
        for index,value in enumerate(nums):
            if value in b:
                d=index-b[value]
                if d<=k:
                    return True
            b[value] = index
        return False
            


        