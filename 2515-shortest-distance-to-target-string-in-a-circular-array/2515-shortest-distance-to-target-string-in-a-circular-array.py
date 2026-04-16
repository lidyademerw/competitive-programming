class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n=len(words)
        ans = float('inf')
        for i in range(n):
            if words[i]==target:
                dist1 = abs(i - startIndex)
                dist2 = n-dist1
                ans = min(ans, dist1, dist2)
        return ans if ans != float('inf') else -1



