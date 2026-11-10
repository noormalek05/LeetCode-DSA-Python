# Problem: 268. Missing Number
# Topic: Arrays / Mathematics
# Difficulty: Easy
# Approach: Mathematical Formula


# ==========================================
# Solution 1: Sum Formula
# ==========================================

class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)

        total_sum = (n * (n + 1)) // 2
        s = 0

        for i in range(0, len(nums)):
            s = s + nums[i]

        a = total_sum - s

        return a

# Time Complexity: O(n)
# Space Complexity: O(1)
