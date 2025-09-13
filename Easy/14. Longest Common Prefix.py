"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""

from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for val in strs[1:]:
            while val[:len(prefix)] != prefix:
                prefix = prefix[:-1]
            if not prefix:
                return ""
        return prefix
    
def main():
    sol = Solution()

    # Test cases
    test_cases = [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),     # no common prefix
        (["interview", "internet", "internal"], "inter"),
        (["a"], "a"),                        # single string
        (["ab", "a"], "a"),                  # one string is a prefix of another
    ]

    for strs, expected in test_cases:
        result = sol.longestCommonPrefix(strs)
        print(f"Input: {strs} → Output: '{result}' (Expected: '{expected}')")


if __name__ == "__main__":
    main()