# Problem: 242. Valid Anagram
# Topic: Strings
# Difficulty: Easy

# ==========================================
# Solution 1: Hash Map / Dictionary Frequency Counter
# ==========================================
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in t:
            if i in d:
                d[i] -= 1
            else:
                return False
        for i in d:
            if d[i] != 0:
                return False
                
        return True

# Time Complexity: O(n)
# Space Complexity: O(1) (at most 26 lowercase English letters; O(k) for general Unicode characters)
