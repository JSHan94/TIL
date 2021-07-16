# Floyd's Tortoise & Hare algorithm
# Explaination : https://fierycoding.tistory.com/45

def hasCycle(self, head):
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False
        
# 
# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         cnt = 0
#         cur = head
        
#         while cnt <= 10000:
#             if cur == None :
#                 return False
#             cnt += 1
#             cur = cur.next
            
#         return True
