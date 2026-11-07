# Problem: 1. Two Sum
# Topic: Arrays
# Difficulty: Easy
# Approach: Brute Force (Nested Loops)


# ==========================================
# Solution 1: Brute Force (Nested Loops)
# ==========================================

class Solution(object):
    def twoSum(self, nums, target):
        a = [0] * 2
        n = len(nums)

        for i in range(0, n):
            for j in range(0, n):
                if i != j and target == nums[i] + nums[j]:
                    a = [i, j]
                    return a

        return a

# Time Complexity: O(n²)
# Space Complexity: O(1)
