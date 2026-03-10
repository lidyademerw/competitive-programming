class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g1=0
        s1=0
        count=0
        while s1 < len(s) and g1< len(g):
            if s[s1]>=g[g1]:
                count+=1
                g1+=1
            s1+=1
                
        return count


        