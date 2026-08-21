class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackt=[]
        stacks=[]
        for i in s:
            if i !="#":
                stacks.append(i)
            else:
                if len(stacks)==0:
                    continue
                stacks.pop()

        for j in t:
            if j!="#":
                stackt.append(j)
            else:
                if len(stackt)==0:
                    continue
                stackt.pop()
        
        return stackt==stacks
            

            
   


      
        