class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cou=Counter(text)
        return min(
            cou['b'],
            cou['a'],
            cou['l'] // 2,
            cou['o'] // 2,
            cou['n']
        )