# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = head
        slow = head
        
        #get middle pointer
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # reverse second half
        # 1221
        # ListNode{val: 2, next: ListNode{val: 1, next: None}}
        # None

        # ListNode{val: 2, next: None}
        # None

        # ListNode{val: 1, next: None}
        # ListNode{val: 2, next: None}


        # ListNode{val: 1, next: None}
        # ListNode{val: 2, next: None}

        # ListNode{val: 1, next: ListNode{val: 2, next: None}}
        # ListNode{val: 2, next: None}

        # None
        # ListNode{val: 1, next: ListNode{val: 2, next: None}}
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
        # checking palindrome
        left, right = head, prev
        while right:
            if (left.val != right.val):
                return False
            left = left.next
            right = right.next
        return True
            