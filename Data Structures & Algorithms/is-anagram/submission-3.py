class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):              # different lengths can't be anagrams
            return False

        count_s = {}
        for ch in s:
            count_s[ch] = count_s.get(ch, 0) + 1

        count_t = {}                      # separate dict for t
        for ch in t:
            count_t[ch] = count_t.get(ch, 0) + 1

        return count_s == count_t         # same letters, same counts → True