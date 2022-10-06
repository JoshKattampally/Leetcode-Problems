class Solution(object):
    def hasCycle(self, head):
        fast = slow = head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False