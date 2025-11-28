# Easy
# Reverse Linked List
# iterative pointer reversal

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Input: head = [1,2,3,4,5]       Output: [5,4,3,2,1]
# Input: head = [1,2]             Output: [2,1]
# Input: head = []                Output: []

# Edge cases        : blank, single item, duplicates, negatives
# Time Complexity   : O(n) ; each node visited exactly once
# Space complexity  : O(1) ; iterative, uses only a few pointers
# Best case         : O(1) ; if list is empty or has one node 
# Worst Case        : O(n) ; when list has n nodes, all links must be reversed
########################################################################
class ListNode():
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

def to_linked_list(head):
    dummy = curr = ListNode()
    for hd in head:
        curr.next = ListNode(hd)
        curr = curr.next
    return dummy.next

def to_list(l1):
    result = []
    while l1:
        result.append(l1.val)
        l1 = l1.next
    return result

class Solution:
    def reverseList(self, l1:ListNode)->ListNode:
        prev = None
        while l1:
            dummy = l1.next
            l1.next = prev
            prev = l1 
            l1 = dummy
        return prev

if __name__ == "__main__":
    head = list(map(int,input("enter linked list members = ").split(",")))
    l1 = to_linked_list(head)
    result = Solution().reverseList(l1)
    l2 = to_list(result)
    print(l2)