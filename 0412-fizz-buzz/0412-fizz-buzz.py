class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        m=[]
        for i in range(1,n+1):
             if i%5==0 and i%3==0:
                m .append("FizzBuzz") 
             elif i%3==0:
               m.append("Fizz")
               
             elif i%5==0:
               m.append("Buzz")
             else:
                m.append(str(i))
        return m


        