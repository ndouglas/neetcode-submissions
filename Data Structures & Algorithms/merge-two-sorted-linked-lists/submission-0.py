# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(-1, None)
        tail = sentinel
        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    nxt = list1.next
                    tail.next = list1
                    list1 = nxt
                else:
                    nxt = list2.next
                    tail.next = list2
                    list2 = nxt
            elif list1:
                nxt = list1.next
                tail.next = list1
                list1 = nxt
            else:
                nxt = list2.next
                tail.next = list2
                list2 = nxt
            tail = tail.next
        return sentinel.next