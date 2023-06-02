from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # input: two sorted lists, list1 and list2
        # output: one list which has both lists spliced together
        # constraints:
            # The number of nodes in both lists is in the range [0, 50].
            # -100 <= Node.val <= 100
            # Both list1 and list2 are sorted in non-decreasing order.
        # edge cases:
            # empty list
            # 
        
        curr1, curr2 = list1, list2
        result = dummy = ListNode()

        if not curr1:
            return curr2
        if not curr2:
            return curr1

        while curr1 or curr2:
            if not curr1:
                dummy.next = curr2
                break
            if not curr2:
                dummy.next = curr1
                break

            if curr1.val < curr2.val:
                dummy.next = curr1
                curr1 = curr1.next
            else:
                dummy.next = curr2
                curr2 = curr2.next

            dummy = dummy.next


        return result.next