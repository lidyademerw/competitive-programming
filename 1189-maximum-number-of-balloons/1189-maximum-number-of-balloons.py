class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cou=Counter(text)
        balloon=Counter("balloon")
        x=len(text)
        for i in balloon:
            x=min(x,cou[i]//balloon[i])
        return x