#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head:
            return head
        
        x = head
        
        length = 0
        while x:
            length += 1
            x = x.next
        
        k = k % length
        
        first_node = ListNode()
        second_node = ListNode()
        y1 = first_node
        y2 = second_node
        
        x = head
        
        for i in range(length-k):
            y1.next = ListNode(x.val)
            y1 = y1.next
            x = x.next
        
        
        while x:
            y2.next = ListNode(x.val)
            y2 = y2.next
            x = x.next
            
        y2.next = first_node.next
        
        return second_node.next
 