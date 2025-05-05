class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        new_s = ""
        new_t = ""

        for idx in range(len(s)):
            if s[idx] == "#":
                new_s = new_s[:-1]
            else:
                new_s += s[idx]
        
        for idx in range(len(t)):
            if t[idx] == "#":
                new_t = new_t[:-1]
            else:
                new_t += t[idx]

        return new_s == new_t