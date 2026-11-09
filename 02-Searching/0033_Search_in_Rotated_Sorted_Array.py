# Problem: 33. Search in Rotated Sorted Array
# Topic: Binary Search / Arrays
# Difficulty: Medium
# Approach: Modified Binary Search


# ==========================================
# Solution 1: Modified Binary Search
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

            elif nums[l] <= nums[m]:

                if nums[l] <= target and nums[m] >= target:
                    h = m - 1
                else:
                    l = m + 1

            else:

                if nums[m] <= target and nums[h] >= target:
                    l = m + 1
                else:
                    h = m - 1

        return -1

# Time Complexity: O(log n)
# Space Complexity: O(1)
