class ListNode:

    def __init__(self, val: str, prev: Option[ListNode], next: Option[ListNode]):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = ListNode(homepage, None, None)

    def visit(self, url: str) -> None:
        prev = self.curr
        self.curr = ListNode(url, prev, None)
        if self.curr.prev:
            self.curr.prev.next = self.curr

    def back(self, steps: int) -> str:
        while steps and self.curr.prev:
            steps -= 1
            self.curr = self.curr.prev
        return self.curr.val        

    def forward(self, steps: int) -> str:
        while steps and self.curr.next:
            steps -= 1
            self.curr = self.curr.next
        return self.curr.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)