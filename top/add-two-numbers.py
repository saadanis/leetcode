"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        place = 1
        n1 = 0
        while l1 is not None:
            n1 = n1 + l1.val * place
            place = place * 10
            l1 = l1.next

        place = 1
        n2 = 0
        while l2 is not None:
            n2 = n2 + l2.val * place
            place = place * 10
            l2 = l2.next
        
        n3 = n1 + n2
        l3 = ListNode(val = 0, next = None)

        _l3 = l3
        
        while n3 > 0:
            _l3.val = n3%10
            n3 = n3 // 10
            if n3 > 0:
                _l3.next = ListNode(val = 0, next = None)
                _l3 = _l3.next
        
        return l3