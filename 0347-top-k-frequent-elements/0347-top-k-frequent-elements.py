class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m=Counter(nums).most_common(k)
        return list(dict(m).keys())

        