class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        x=[]
        phone= {
            "2":"abc", 
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        def letcomb(i,res):
            if i==len(digits):
                x.append(res)
                return
            letter=phone[digits[i]]
            for char in letter:
                letcomb(i+1,res+char)
        letcomb(0,"")
        return x
        