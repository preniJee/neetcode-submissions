# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        if not list2:
            return list1
        merged_head = ListNode()
        # if list1.val >= list2.val:
        #     merged_head.next = list1
        #     list1 = list1.next
        # else:
        #     merged_head = list2
        #     list2 = list2.next
        curr = merged_head
        while list1 or list2: 
            # print(list1.val, list2.val, merged_head.val)
            if not list1:
                curr.next = list2
                list2 = list2.next
            elif not list2:
                curr.next = list1
                list1 = list1.next
            elif list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        return merged_head.next



        

        