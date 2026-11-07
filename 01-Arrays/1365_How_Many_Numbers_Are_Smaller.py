# Problem: 1365. How Many Numbers Are Smaller Than the Current Number
# Topic: Arrays
# Difficulty: Easy
# Approach: Brute Force (Nested Loops)


# ==========================================
# Solution 1: Brute Force (Nested Loops)
# ==========================================

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        n = len(nums)
        a = [0] * n

        for i in range(0, n):
            x = 0

            for j in range(0, n):
                if nums[i] > nums[j]:
                    x = x + 1

            a[i] = x

        return a

# Time Complexity: O(n²)
# Space Complexity: O(n)
