class Solution:
    def decodeString(self, s: str) -> str:
        self.ind=0
        def decode():
            k=0
            res=""
            while self.ind<len(s):
                char=s[self.ind]
                if char.isdigit():
                    k=k*10+int(char)
                    self.ind+=1
                elif char=="[":
                    self.ind+=1
                    inside=decode()
                    res+=inside*k
                    k=0
                elif char=="]":
                    self.ind+=1
                    return res
                else:
                    res+=char
                    self.ind+=1
            return res
        return decode()
      