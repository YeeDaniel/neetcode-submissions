class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s1 = sorted(s)
        # s2 = sorted(t)
        # if s1 == s2:
        #     return True
        # return False
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)