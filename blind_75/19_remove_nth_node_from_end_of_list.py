from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# double pass
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # input: head of linked list, nth node from the end to remove
        # output: head of linked list where nth node from the end is removed
        # constraints:
            # The number of nodes in the list is sz.
            # 1 <= sz <= 30
            # 0 <= Node.val <= 100
            # 1 <= n <= sz
        # edge cases:
            # don't need to handle case where n is greater than the sz of the list
            # n == size or n == 1

        size = 0
        tracker1 = tracker2 = head

        while tracker1:
            size += 1
            tracker1 = tracker1.next
        
        if size == n:
            return head.next

        while tracker2:
            size -= 1
            if size == n:
                if tracker2.next:
                    tracker2.next = tracker2.next.next
                else: tracker2.next = None

            tracker2 = tracker2.next

        return head
    
# single pass
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # input: head of linked list, nth node from the end to remove
        # output: head of linked list where nth node from the end is removed
        # constraints:
            # The number of nodes in the list is sz.
            # 1 <= sz <= 30
            # 0 <= Node.val <= 100
            # 1 <= n <= sz
        # edge cases:
            # don't need to handle case where n is greater than the sz of the list
            # n == size or n == 1
        left = dummy = ListNode(0, head)
        right = head

        while n > 0:
            n -= 1
            right = right.next
        
        while right:
            left = left.next
            right = right.next
        
        if left.next:
            left.next = left.next.next
        else:
            left.next = None
        
        return dummy.next