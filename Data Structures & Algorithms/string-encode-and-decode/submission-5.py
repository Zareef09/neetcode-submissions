class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""                              # 1
        for s in strs:                           # 2
            result += str(len(s)) + "#" + s      # 3
        return result                            # 4

    def decode(self, s: str) -> List[str]:
        result = []                              # 5
        i = 0                                    # 6

        while i < len(s):                        # 7
            j = i                                # 8
            while s[j] != "#":                   # 9
                j += 1                           # 10
            length = int(s[i:j])                 # 11
            start = j + 1                        # 12
            result.append(s[start:start + length])   # 13
            i = start + length                   # 14

        return result                            # 15