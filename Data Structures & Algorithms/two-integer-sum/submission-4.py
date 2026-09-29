class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}                               # number -> its index

        for i, num in enumerate(nums):          # i = index, num = value
            difference = target - num           # the number I'd need to pair with this one
            if difference in seen:              # have I already seen that number?
                return [seen[difference], i]    # its index first (smaller), then mine
            seen[num] = i                       # remember this number's index

        return []                               # problem guarantees a pair, so this never runs