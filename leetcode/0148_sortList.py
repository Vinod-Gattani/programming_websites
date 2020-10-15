#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
          
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+= 1
            else: 
                arr[k] = R[j] 
                j+= 1
            k+= 1
          
        while i < len(L): 
            arr[k] = L[i] 
            i+= 1
            k+= 1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+= 1
            k+= 1

class Solution:
        
    def sortList(self, head: ListNode) -> ListNode:
        
        head_l = []
        
        while head:
            head_l.append(head.val)
            head = head.next
            
        mergeSort(head_l)
        
        result = ListNode()
        a = result
        
        for i in head_l:
            a.next = ListNode(i)
            a = a.next
            
        return result.next
        