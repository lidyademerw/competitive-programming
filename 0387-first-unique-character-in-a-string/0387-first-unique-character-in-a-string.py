class Solution:
    def firstUniqChar(self, s: str) -> int:
        x=Counter(s)
        for i, char in enumerate(s):
            if  x[char]==1:
                return i
        
        return -1


            
        