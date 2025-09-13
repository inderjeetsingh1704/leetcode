"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i:len(needle)+i] == needle:
                return i
        return -1

def main():
    sol = Solution()

    # Test cases
    tests = [
        ("sadbutsad", "sad"),      # Expected 0
        ("leetcode", "leeto"),     # Expected -1
        ("hello", "ll"),           # Expected 2
        ("aaaaa", "bba"),          # Expected -1
        ("", ""),                  # Expected 0 (by convention)
    ]

    for haystack, needle in tests:
        result = sol.strStr(haystack, needle)
        print(f"Input: haystack='{haystack}', needle='{needle}' -> Output: {result}")


if __name__ == "__main__":
    main()