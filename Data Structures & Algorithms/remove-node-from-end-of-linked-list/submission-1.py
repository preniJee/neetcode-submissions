# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        len_n = 0
        curr = head
        while curr:
            len_n +=1
            curr = curr.next

        del_idx = len_n - n 
        if del_idx == 0 :
            return head.next
        print(len_n, del_idx)
       
        curr = head
        for i in range(len_n - 1): 
            if i == del_idx - 1:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head

            



        