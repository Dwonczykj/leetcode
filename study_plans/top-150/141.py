# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/description/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next: Optional[ListNode] = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        The main idea to solve the question of detecting a cycle in a singly-linked list 
        is to use the concept of two pointers: 
        a "slow" pointer that moves one step at a time and 
        a "fast" pointer that moves two steps at a time. 
        By having these two pointers traverse the list simultaneously, 
        if there is a cycle, the fast pointer will eventually catch up to the slow pointer. 
        If there is no cycle, the fast pointer will reach the end of the list.
        """
        if not head:
            return False
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
        return False

    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        seen = set()
        node = head
        while node:
            # print(node.val)
            if node in seen:
                # return node.next != node
                return True  # as this is allowed apparently
            seen.add(node)
            node = node.next
        return False


if __name__ == "__main__":
    sol = Solution()
    kwargs_list = [
        ({"head": ListNode()}, True),
    ]
    for kwargs, expected in kwargs_list:
        result = sol.hasCycle(**kwargs)
        assert result == expected
