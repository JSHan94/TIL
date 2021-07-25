
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0 
        head = cur = ListNode(0)
        
        while l1 or l2 or carry:
            v1,v2 =0,0
            if l1 :
                v1 = l1.val
                l1 = l1.next
            if l2 :
                v2 = l2.val
                l2 = l2.next
                
            carry, res = divmod(v1+v2+carry,10)
            
            cur.next = ListNode(res)
            cur = cur.next

        return head.next
