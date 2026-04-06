# Medium
# Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Input: head = [1,2,3,4,5], n = 2        Output: [1,2,3,5]
# Input: head = [1], n = 1                Output: []
# Input: head = [1,2], n = 1              Output: [1]

# Edge cases        : empty, single element, remove last element, remove first
# Time Complexity   : O(n)
# Space complexity  : O(1)
# Best case         : O(n) 
# Worst Case        : O(n)
########################################################################
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head:ListNode, n:int)->ListNode:
        if not head:
            return None 
        
        dummy = ListNode()
        dummy.next = head
        current = dummy 
        counter = 0

        while current.next:
            current = current.next 
            counter = counter + 1

        pos = counter - n 
        current = dummy 

        while pos > 0:
            current = current.next
            pos = pos - 1

        current.next = current.next.next

        return dummy.next