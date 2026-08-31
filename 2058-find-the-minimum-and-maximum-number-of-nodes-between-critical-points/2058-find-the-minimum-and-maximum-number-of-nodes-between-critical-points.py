# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head):
        prev = head
        curr = head.next

        pos = 2

        first = -1
        last = -1
        min_dist = float('inf')

        while curr and curr.next:
            nxt = curr.next

            if ((curr.val > prev.val and curr.val > nxt.val) or
                (curr.val < prev.val and curr.val < nxt.val)):

                if first == -1:
                    first = pos
                else:
                    min_dist = min(min_dist, pos - last)

                last = pos

            prev = curr
            curr = nxt
            pos += 1

        if first == -1 or first == last:
            return [-1, -1]

        return [min_dist, last - first]