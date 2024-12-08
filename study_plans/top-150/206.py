# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/description/
# https://youtu.be/9TsQmdRAxT8

# Definition for singly-linked list.
from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next

    def __repr__(self):
        return f"[{self.val}]" if self.next else f"[{self.val}]!"

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, ListNode):
            return False
        if self.val != value.val:
            return False
        if not self.next and not value.next:
            return True
        return self.next.__eq__(value.next)


def ll(head: list[int]) -> Optional[ListNode]:
    if not head:
        return None
    node = ListNode(val=head[0])
    root = node
    for i in range(1, len(head)):
        node.next = ListNode(head[i])
        node = node.next
    return root


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None
        while head:
            temp = head.next  # save the next link that we will remove
            print(
                f"Reassign [{head}] -> [{head.next}] to [{head}] -> [{node}]")
            head.next = node  # relink backwards
            node = head
            head = temp
        return node

    def run(self, head: list[int]):
        return self.reverseList(head=ll(head=head))
        # if not head:
        #     return self.reverseList(head=None)
        # _head = ListNode(val=head[0])
        # if len(head) == 1:
        #     return self.reverseList(head=_head)
        # node = _head
        # for i in range(1, len(head)):
        #     node.next = ListNode(head[i])
        #     node = node.next
        # return self.reverseList(head=_head)


if __name__ == "__main__":
    sol = Solution()
    kwargs_list = [
        ({"head": [1]}, [1]),
        ({"head": [1, 2, 3, 4, 5]}, [5, 4, 3, 2, 1]),
    ]
    for kwargs, expected in kwargs_list:
        result = sol.run(**kwargs)
        assert result == ll(expected)
