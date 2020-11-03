#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        
        input_list = []
        
        while head:
            input_list.append(head.val)
            head = head.next

        for i in range(1, len(input_list)):
            num = input_list[i]

            j = i-1
            while  (j >= 0 and input_list[j] > num):
                #print(j, i, input_list)
                input_list[j+1], input_list[j] = input_list[j], num
                j -= 1
        
        head = ListNode()
        a = head
        
        for num in input_list:
            a.next = ListNode(num)
            a = a.next
            
        return head.next
    #copied
    #https://leetcode.com/problems/insertion-sort-list/solution/
    def insertionSortList(self, head: ListNode) -> ListNode:
        pseudo_head = ListNode()

        curr = head
        while curr:
            # At each iteration, we insert an element into the resulting list.
            prev_node = pseudo_head
            next_node = prev_node.next
            # find the position to insert the current node
            while next_node:
                if curr.val < next_node.val:
                    break
                prev_node = next_node
                next_node = next_node.next

            next_iter = curr.next
            # insert the current node to the new list
            curr.next = next_node
            prev_node.next = curr

            # moving on to the next iteration
            curr = next_iter

        return pseudo_head.next