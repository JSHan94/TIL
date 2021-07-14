# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = -999
        cur = head
        a = new_head = None
        while cur != None:
            if prev != cur.val :
                if new_head == None:
                    a = new_head = ListNode()
                else : 
                    new_head.next = ListNode()
                    new_head = new_head.next
                new_head.val = cur.val
                    
            prev = cur.val           
            cur = cur.next
        return a
