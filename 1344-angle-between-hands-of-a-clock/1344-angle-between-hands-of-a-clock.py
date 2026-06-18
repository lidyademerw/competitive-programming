class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        x=abs(30*hour-5.5*minutes) 
        if x < 180:
            return x
        else:
            return 360-x

        