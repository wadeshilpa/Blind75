# Easy
# Linked List Cycle
# 2 Pointer - slow and fast

# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tails next pointer is connected to. 
# Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

# head = [3,2,0,-4], pos = 1      Output: true
# head = [1,2], pos = 0           Output: true
# head = [1], pos = -1            Output: false

# Edge cases        : empty, single node - cycle/no cycle
# Time Complexity   : O(n)          # Each node visited at most twice
# Space complexity  : O(1)          # Uses only two pointers
# Best case         : Cycle detected early (few iterations)
# Worst Case        : No cycle; traverses entire list
########################################################################
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def cycleLL(self, head:ListNode)->bool:
        slow , fast = head, head

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

            if slow == fast:
                return True
        return False
    
if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2   # cycle here

    head = n1

    print(Solution().cycleLL(head))
