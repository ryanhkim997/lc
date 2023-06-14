# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# with extra space:
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # input: head of linked list
        # output: head of linked list, where list is reordered by 1, n, 2, n - 1... where n is the last node of list
        # constraints:
            # The number of nodes in the list is in the range [1, 5 * 10^4].
            # 1 <= Node.val <= 1000
        # edge cases:
            # no need to consider empty list, since we assume there is at least one node
            # single node list; value does not matter
        
        ordered_list = []
        curr = head
        dummy1 = dummy2 = ListNode()

        while curr:
            ordered_list.append(curr)
            curr = curr.next
        
        left, right = 0, len(ordered_list) - 1
        
        while left < right:
            dummy2.next = ordered_list[left]
            dummy2.next.next = ordered_list[right]

            dummy2 = dummy2.next.next
            left += 1
            right -= 1
        
        if left == right:
            dummy2.next = ordered_list[left]
            dummy2 = dummy2.next

        dummy2.next = None
        
        return dummy1.next
    
# without extra space:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        right = self.reverseList(slow.next)
        slow.next = None

        curr = head
        while right:
            next = curr.next
            curr.next = right
            right = right.next
            curr.next.next = next
            curr = next
        
        return head
            
    
    def reverseList(self, head):
        curr = head
        prev = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev