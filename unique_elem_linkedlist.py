# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        temp = head
        freq = {}
        
        
        while temp:
            freq[temp.val] = freq.get(temp.val,0)+1
            temp= temp.next
        
        temp = ListNode(None)
        result = temp
        curr = head
        while curr:
            if freq.get(curr.val)==1:
                result.next = curr
                result = result.next
            curr = curr.next
        result.next = None
        return temp.next
