'''
    David Ewald 8/29/21
    002 Add Two Numbers: Medium

    You are given two non-empty linked lists representing two non-negative integers. 
    The digits are stored in reverse order, and each of their nodes contains a single digit. 
    Add the two numbers and return the sum as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

'''
from typing import Optional

'''
    Definition for singly-linked list.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        p = l1
        q = l2
        curr = head
        carryOver = 0
        while p or q or carryOver:
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0
            
            sum = x + y + carryOver
            carryOver = sum // 10
            sum = sum % 10
            curr.next = ListNode(sum);
            
            curr = curr.next
            p = p.next if p else None
            q = q.next if q else None
        
        return head.next
