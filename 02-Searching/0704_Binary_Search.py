# Problem: 704. Binary Search
# Topic: Searching / Binary Search
# Difficulty: Easy
# Approach: Iterative Binary Search


# ==========================================
# Solution 1: Iterative Binary Search
# ==========================================

class Solution(object):
    def search(self, nums, target):
        l = 0
        n = len(nums)
        h = n - 1

        while l <= h:
            m = (l + h) // 2

            if nums[m] == target:
                return m

            elif nums[m] < target:
                l = m + 1

            else:
                h = m - 1

        return -1

# Time Complexity: O(log n)
# Space Complexity: O(1)
