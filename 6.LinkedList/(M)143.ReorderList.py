# Medium
# Reorder List
# https://leetcode.com/problems/reorder-list/description/

# You are given the head of a singly linked-list. 
# The list can be represented as:                     L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:       L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Input: head = [1,2,3,4]             Output: [1,4,2,3]
# Input: head = [1,2,3,4,5]           Output: [1,5,2,4,3]

# Edge cases        : empty, even length, odd length, 1 element, negative numbers
# Time Complexity   : O(n)
# Space complexity  : O(1).     reversing in-place and merging in-place. No extra data structures
# Best case         : O(n) — you always traverse the full list regardless of input. 
# Worst Case        : O(n) — you always traverse the full list regardless of input. 
########################################################################
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head:ListNode)->None:
        if not head or not head.next:
            return
        
        slow = head
        fast = head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow 
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev 
            prev = curr
            curr = temp

        first = head
        second = prev

        while first and second:
            next_hop = first.next
            first.next = second
            first = next_hop

            next_hop = second.next
            second.next = first 
            second = next_hop

