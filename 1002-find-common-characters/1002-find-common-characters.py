class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common=Counter(words[0])
        for i in range(1,len(words)):
            word=Counter(words[i])
            for i in common:
                common[i]=min(common[i],word[i])
        re=[]
        for i in common:
             count = common[i]
             for j in range(count):
                re.append(i)
        return re