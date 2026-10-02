class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = {}

        for number in nums:
            frequent[number] = frequent.get(number, 0) + 1

        ranked = sorted(frequent.items(), key=lambda p: (-p[1], p[0]))

        return [p[0] for p in ranked[:k]]



        