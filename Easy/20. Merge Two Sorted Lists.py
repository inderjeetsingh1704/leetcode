"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order."""


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2
        return dummy.next
                

def build_linked_list(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def main():
    sol = Solution()

    test_cases = [
        ([1, 2, 4], [1, 3, 4,5,6], [1, 1, 2, 3, 4, 4,5,6]),
        ([], [], []),
        ([], [0], [0]),
        ([5], [1, 2, 3, 4], [1, 2, 3, 4, 5]),
    ]

    for l1_vals, l2_vals, expected in test_cases:
        l1 = build_linked_list(l1_vals)
        l2 = build_linked_list(l2_vals)
        merged = sol.mergeTwoLists(l1, l2)
        result = linked_list_to_list(merged)
        print(f"List1: {l1_vals}, List2: {l2_vals} → Output: {result} (Expected: {expected})")


if __name__ == "__main__":
    main()