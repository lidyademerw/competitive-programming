class Solution:
    def calculate(self, s: str) -> int:
        self.ind=0
        def calc():
            res=0
            nums=0
            sign=1
            while self.ind<len(s):
                char=s[self.ind]
                self.ind+=1
                if char.isdigit():
                    nums=nums*10+int(char)
                elif char=="(":
                    nums=calc()
                elif char==")":
                    res+=sign*nums
                    return res
                elif char=="+":
                    res+=sign*nums
                    nums=0
                    sign=1
                elif char=="-":
                    res+=nums*sign
                    nums=0
                    sign=-1
            res+=sign*nums
            return res
        return calc()

        