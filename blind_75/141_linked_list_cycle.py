from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # input: head of linked list
        # output: boolean true if linked list is cyclical, false if not
        # constraints:
            # The number of the nodes in the list is in the range [0, 104].
            # -105 <= Node.val <= 105
            # pos is -1 or a valid index in the linked-list.
        # edge cases:
            # head is none
        
        if not head or not head.next: return False

        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False