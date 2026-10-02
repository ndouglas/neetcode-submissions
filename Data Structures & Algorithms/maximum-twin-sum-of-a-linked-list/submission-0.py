# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow is now the middle ([n/2-1])
        curr = head
        prev = None
        stop = slow.next
        while curr and curr is not stop:
            next_one = curr.next
            curr.next = prev
            prev = curr
            curr = next_one
        left = prev
        right = stop
        max_sum = left.val + right.val
        while left and right:
            max_sum = max(max_sum, left.val + right.val)
            left = left.next
            right = right.next
        return max_sum