# Problem: 35. Search Insert Position
# Topic: Arrays / Searching
# Difficulty: Easy


# ==========================================
# Solution 1: Linear Search
# ==========================================

class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(0, len(nums)):
            if target <= nums[i]:
                return i

        return len(nums)

# Time Complexity: O(n)
# Space Complexity: O(1)


# ==========================================
# Solution 2: Append + Sorting
# ==========================================

class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i

        nums.append(target)
        nums.sort()

        return nums.index(target)

# Time Complexity: O(n log n)
# Space Complexity: O(n)


# ==========================================
# Solution 3: Binary Search
# ==========================================

class Solution(object):
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                l = mid + 1

            else:
                r = mid - 1

        return l

# Time Complexity: O(log n)
# Space Complexity: O(1)
