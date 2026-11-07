# Problem: 1431. Kids With the Greatest Number of Candies
# Topic: Arrays
# Difficulty: Easy


# ==========================================
# Solution 1: Brute Force (Nested Loops)
# ==========================================

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        n = len(candies)
        a = [False] * n

        for i in range(0, n):
            for j in range(0, n):
                if candies[i] + extraCandies >= candies[j]:
                    a[i] = True
                else:
                    a[i] = False
                    break

        return a

# Time Complexity: O(n²)
# Space Complexity: O(n)


# ==========================================
# Solution 2: Using Maximum (max())
# ==========================================

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maximum = max(candies)
        array = []

        for i in candies:
            if i + extraCandies >= maximum:
                array.append(True)
            else:
                array.append(False)

        return array

# Time Complexity: O(n)
# Space Complexity: O(n)
