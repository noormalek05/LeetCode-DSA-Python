# Problem: 58. Length of Last Word
# Topic: Strings
# Difficulty: Easy

# ==========================================
# Solution 1: Reverse Traversal with Early Return
# ==========================================
class Solution(object):
    def lengthOfLastWord(self, s):
        c = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " " and c > 0:
                return c
            elif s[i] != " ":
                c = c + 1
        return c

# Time Complexity: O(n)
# Space Complexity: O(1)


# ==========================================
# Solution 2: Reverse Traversal with Break
# ==========================================
class Solution(object):
    def lengthOfLastWord(self, s):
        n = len(s)
        c = 0
        for i in range(n - 1, -1, -1):
            if s[i] == " ":
                if c > 0:
                    break
            else:
                c = c + 1
        return c

# Time Complexity: O(n)
# Space Complexity: O(1)
