# Problem: 1281. Subtract the Product and Sum of Digits of an Integer
# Topic: Foundations / Mathematics
# Difficulty: Easy
# Approach: Digit Extraction


# ==========================================
# Solution 1: Using While Loop
# ==========================================

class Solution(object):
    def subtractProductAndSum(self, n):
        p = 1
        s = 0

        while n > 0:
            a = n % 10
            s += a
            p = p * a
            n = n // 10

        return p - s

# Time Complexity: O(d)
# Space Complexity: O(1)
