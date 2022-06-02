# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2
        
        if list1.val <= list2.val: #1
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else: #2
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
    
    
    def mergeTwoLists1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = temp = ListNode(0)
        
        while list1 != None and list2 != None:
            print(list1)
            print(list2)
            print(temp, dummy)
            if (list1.val < list2.val):
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            
            temp = temp.next
            print(list1)
            print(list2)
            print(temp, dummy)
            print("\n")
            
        print("sfdf1")
        print(list1)
        print(list2)
        print(temp, dummy)
        temp.next = list1 or list2
        print("sfdf")
        print(list1)
        print(list2)
        print(temp, dummy)
        
        return dummy.next