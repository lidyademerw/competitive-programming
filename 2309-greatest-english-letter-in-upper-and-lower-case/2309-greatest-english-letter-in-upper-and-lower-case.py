class Solution:
    def greatestLetter(self, s: str) -> str:
        m=""
        for i in s:
            if i.lower() in s and i.upper() in s:
                m=max(m,i.upper())
        return m


        