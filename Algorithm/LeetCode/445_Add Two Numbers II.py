# recursion 카테고리에 있지만 iterative하게 짠 듯

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        n1 = n2 = 0
        
        while l1 :
            n1 = n1*10 + l1.val
            l1 = l1.next
        while l2 :
            n2 = n2*10 + l2.val
            l2 = l2.next
            
        s = n1 + n2 
        dummy = cur = ListNode(0)

        for i in str(s):
            cur.next = ListNode(int(i))
            cur = cur.next
            
        return dummy.next
