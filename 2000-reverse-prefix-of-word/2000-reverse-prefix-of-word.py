class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack=[]
        n=len(word)
        for i in range(n):
            stack.append(word[i])
            if word[i]==ch:
                res=""
                while len(stack)>0:
                    res+=stack.pop()
                if len(word)==len(stack):
                    return res
                else:
                    return res + word[i+1:]
        return word
            

        