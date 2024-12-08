import re
from typing import Dict, Any, List, Optional

from binary_tree_node import TreeNode


def parse_example_to_test_case(example_str: str) -> List[Dict[str, Any]]:
    """Parse a leetcode example string into multiple test cases.

    Returns a list of dictionaries, each containing input arguments and expected output
    for one test case.
    """
    # Split into individual examples
    examples = re.split(r'Example \d+:', example_str)
    # Filter out empty strings and strip whitespace
    examples = [ex.strip() for ex in examples if ex.strip()]

    test_cases = []
    for example in examples:
        # Extract input line and output line
        input_match = re.search(r'Input: (.+)', example)
        output_match = re.search(r'Output: (.+)', example)

        if not input_match or not output_match:
            raise ValueError(
                "Example string must contain 'Input:' and 'Output:' lines")

        # Parse input arguments
        input_str = input_match.group(1)
        input_pairs = [pair.strip() for pair in input_str.split(',')]

        args_dict = {}
        for pair in input_pairs:
            key, value = pair.split('=')
            key = key.strip()
            # Remove quotes and spaces from value
            value = value.strip().strip('"')
            args_dict[key] = value

        # Parse expected output
        expected_output = int(output_match.group(1))

        test_cases.append({
            "args": args_dict,
            "expected": expected_output
        })

    return test_cases


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


def fmt_node(node: ListNode, ind: int = 0, ind_max: int = 10):
    if node.next and ind < ind_max:
        return f"[{node.val}] -> {fmt_node(node.next, ind=ind+1)}"
    elif ind < ind_max:
        return f"[{node.val}]!"
    else:
        return f"[{node.val}]..."


def print_node(node: ListNode, ind: int = 0, ind_max: int = 10):
    print(fmt_node(node=node, ind=ind, ind_max=ind_max))


def ll(head: list[int]) -> Optional[ListNode]:
    if not head:
        return None
    node = ListNode(val=head[0])
    root = node
    for i in range(1, len(head)):
        node.next = ListNode(head[i])
        node = node.next
    return root


def tn(nums: list[int | None]):
    return TreeNode.init_from_list(TreeNode, nums)
