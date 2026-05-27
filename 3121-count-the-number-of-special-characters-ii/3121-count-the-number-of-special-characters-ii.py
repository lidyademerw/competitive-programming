class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        x=set(word.lower())
        m=""
        for i in x:
            x=word.rfind(i.lower())
            y=word.find(i.upper())
            if x>=0 and y>=0 and x<y :
                m+=i
        return len(m)