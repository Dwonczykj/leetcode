# 92. Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/description/?envType=study-plan-v2&envId=top-interview-150
# https://leetcode.com/problems/reverse-linked-list-ii/solutions/5418381/video-simple-solution

# Definition for singly-linked list.
from typing import Optional
from test_helper import fmt_node, ListNode, print_node, ll


class Solution:
    def run(self, head: list[int], left: int, right: int):
        fn = self.reverseBetween
        if not head:
            return fn(head=None, left=left, right=right)
        _head = ListNode(val=head[0])
        if len(head) == 1:
            return fn(head=_head, left=left, right=right)
        node = _head
        for i in range(1, len(head)):
            node.next = ListNode(head[i])
            node = node.next
        return fn(head=_head, left=left, right=right)

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # edge cases
        if not head or left == right:
            return head
        # dummy will be the node before root that we can use to ensure we dont have None exception
        # as we can then return dummy.next regardless of whether head is set or not.

        dummy = ListNode(0, head)
        print_node(head)
        prev = dummy
        # pos_prev = 0

        # Sets prev to the one before left which will stay fixed here.
        for _ in range(left - 1):
            prev = prev.next
            # pos_prev += 1
            # print(f"prev at position: ({pos_prev}) with val: [{prev.val}]")

        # Set cur to left
        cur = prev.next
        # cur will increase with every loop iteration
        # simply due to the fact that each loop inserts the node `temp`
        # between `prev` and *left* and then
        # `temp` is always set to cur.next

        # Now we have prev and cur set ready to loop
        # In the loop we first need to:
        # First save next node which we will break link to
        # Second break next link and assign to prev
        # Incremement / update prev first as current depends on it
        # Finally increment / update cur

        for _ in range(right - left):
            temp = cur.next
            print(f"[prev],[cur],[temp] = [{
                  prev.val}],[{cur.val}],[{temp.val}]")
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp
            print_node(dummy.next)

        return dummy.next


if __name__ == "__main__":
    sol = Solution()
    kwargs_list = [
        ({"head": [1, 2, 3, 4, 5, 6], "left": 2,
         "right": 5}, [1, 5, 4, 3, 2, 6]),
        ({"head": [1, 2, 3, 4, 5], "left": 2, "right": 4}, [1, 4, 3, 2, 5]),
        ({"head": [1, 2, 3, 4, 5], "left": 3, "right": 3}, [1, 2, 3, 4, 5]),
        ({"head": [1, 2], "left": 1, "right": 1}, [1, 2]),
        ({"head": [1], "left": 1, "right": 1}, [1]),
        ({"head": [1, 3, 5], "left": 3, "right": 3}, [1, 3, 5]),
        ({"head": [1, 3, 5], "left": 2, "right": 3}, [1, 5, 3]),
        ({"head": [], "left": 2, "right": 3}, []),
    ]
    for kwargs, expected in kwargs_list:
        print("-"*30+"\nNew Solution:")
        result = sol.run(**kwargs)
        x = ll(expected)
        assert result == x
