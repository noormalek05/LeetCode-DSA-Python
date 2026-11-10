# Problem: 69. Sqrt(x)
# Topic: Searching / Binary Search
# Difficulty: Easy
# Approach: Binary Search


# ==========================================
# Solution 1: Binary Search   
# ==========================================

class Solution(object):
    def mySqrt(self, x):
        low = 1
        high = x
        ans = 1

        if x == 0:
            return 0

        else:
            while low <= high:
                m = (low + high) // 2

                if m * m <= x:
                    low = m + 1
                    ans = m
                else:
                    high = m - 1

            return ans

# Time Complexity: O(log x)
# Space Complexity: O(1)
