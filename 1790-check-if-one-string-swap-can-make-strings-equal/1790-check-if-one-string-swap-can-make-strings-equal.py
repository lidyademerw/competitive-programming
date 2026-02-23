class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        m=[]
        for i in range(len(s1)):
            if s1[i] !=s2[i]:
                m.append(i)
        if len(m)==2:
            i,j=m[1],m[1]
            return s1[i]==s2[j] and s1[j]==s2[i] or str(sorted(s1))==str(sorted(s2))
        return False