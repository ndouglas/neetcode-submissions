# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def innerReverseList(self, head: Optional[ListNode]) -> (Optional[ListNode], Optional[ListNode]):
        if not head:
            return (None, None)
        elif not head.next:
            return (head, head)
        elif not head.next.next:
            new_head = head.next
            new_head.next = head
            head.next = None
            return (new_head, head)
        else:
            new_head = head.next
            head.next = None
            (new_head, new_tail) = self.innerReverseList(new_head)
            new_tail.next = head
            return (new_head, head)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.innerReverseList(head)[0]
