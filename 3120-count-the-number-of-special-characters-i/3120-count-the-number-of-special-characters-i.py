class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        n=set(word.lower())
        m=""
        for i in n:
            if i.lower() in word and  i.upper() in word:
                m+=i
            
        return len(m)

        