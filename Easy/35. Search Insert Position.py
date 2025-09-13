"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1

        while start<=end:
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                start = start+1
            else:
                end = end-1
        return start

def main():
    sol = Solution()

    # Test cases: (nums, target, expected)
    tests = [
        ([1,3,5,6], 5, 2),
        ([1,3,5,6], 2, 1),
        ([1,3,5,6], 7, 4),
        ([1,3,5,6], 0, 0),
        ([1], 0, 0),
        ([1], 1, 0),
    ]

    for nums, target, expected in tests:
        result = sol.searchInsert(nums, target)
        print(f"Input: nums={nums}, target={target} -> Output: {result} (Expected: {expected})")


if __name__ == "__main__":
    main()