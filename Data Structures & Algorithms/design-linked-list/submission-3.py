class ListNode:
    def __init__(self, val: int, next: Option[ListNode]):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        while curr and index:
            index -= 1
            curr = curr.next
        if curr and not index:
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        self.head = ListNode(val, self.head)

    def addAtTail(self, val: int) -> None:
        prev = None
        curr = self.head
        while curr:
            prev = curr
            curr = curr.next
        prev.next = ListNode(val, None)

    def addAtIndex(self, index: int, val: int) -> None:
        prev = None
        curr = self.head
        while curr and index:
            index -= 1
            prev = curr
            curr = curr.next
        if prev and not index:
            prev.next = ListNode(val, curr)

    def deleteAtIndex(self, index: int) -> None:
        prev = None
        curr = self.head
        while curr and index:
            index -= 1
            prev = curr
            curr = curr.next
        if prev and curr and not index:
            prev.next = curr.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)