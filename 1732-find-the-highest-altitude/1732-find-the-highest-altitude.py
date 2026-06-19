class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        x=[0]
        for i in range(len(gain)):
            y=x[i]+ gain[i]
            x.append(y)
        return max(x)


        
        