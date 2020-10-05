

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        carry_over = 0
        result_node = ListNode()
        curr = result_node
        
        while l1 or l2 :
            l1_val = 0 if l1 is None else l1.val
            l2_val = 0 if l2 is None else l2.val
            
            l1 = l1 if l1 is None else l1.next
            l2 = l2 if l2 is None else l2.next
            
            val = l1_val + l2_val
            
            val = val + 1 if carry_over else val
                
            carry_over = val // 10
            curr.next = ListNode(val%10)
            curr = curr.next
            
        
        if carry_over:
            curr.next = ListNode(1)
            
        return result_node.next
            
if __name__ == "__main__":
    l1 = [9,9,9,9,9,9,9]
    l2=[9,9,9,9]
    print(Solution().addTwoNumbers(l1, l2))
    print(f"Correct Answer is: [8,9,9,9,0,0,0,1]")