# Problem: 125. Valid Palindrome
# Topic: Strings
# Difficulty: Easy

# ==========================================
# Solution 1: String Filtering and Reverse Comparison
# ==========================================
class Solution(object):
    def isPalindrome(self, s):
        a = ''
        for i in s:
            if i.isalpha() or i.isdigit():
                a = a + i.lower()
        if a == a[::-1]:
            return True
            
        return False

# Time Complexity: O(n) (Note: repeated string concatenation in Python can take up to O(n^2) in the worst case)
# Space Complexity: O(n)
