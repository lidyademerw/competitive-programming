class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res=[]
        for i in words:
            if not res  or  sorted(i)!= sorted(res[-1]):
                res.append(i)
        return res  
            
        