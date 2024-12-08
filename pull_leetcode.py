# todo:
"""
TODO: Please write me a script that takes a url of a leetcode problem and download the problem statement and the test cases
into a python file in the study_plans/top-150 directory. The file should be named like 199.py if the problem number is 199.
The file should have the first line as the title of the problem, the second line as the link to the problem, and the third line as the problem description.

There should then be the following imports:
```python
from typing import List, Dict, Optional
from collections import deque
from pprint import pprint, pformat
```
additionally if this is a question about TreeNode containing TreeNode in the problem, then include:
```python
from typing import List, Dict, Optional
from binary_tree_node import TreeNode, tt
```
additionally if this is a question about Linked lists containing ListNode in the problem, then include:
```python
from typing import List, Dict, Optional
from test_helper import fmt_node, ListNode, print_node, ll
```
additionally if this is a question about Graphs or contains a case Sensitive class definition of ```class Node:```,then include:
```python
from test_helper import fmt_node, ListNode, print_node, ll
from typing import List, Dict, Optional
from graph import Node
```

After that, please add 2 space lines before the class Solution and the class Solution block.

Then in a __main__ block, please write the test cases as a list of kwargs in the format of the expected input of the function which would take the following format:
```python
if __name__ == "__main__":
    from pprint import pformat, pprint
    sol = Solution()
    null = None
    kwargs_list = [
        ({"kwarg"=...}, ...),
    ]
    test_number = 0
    for kwargs, expected in kwargs_list:
        test_number += 1
        print(
            "-"*30+f"\nNew Solution {test_number}.: {pformat(kwargs, indent=2)}")
        print("-"*30+f"\nNew Solution: kwargs = {kwargs}")
        result = sol.fn(root=kwargs["kwarg"])
        assert result == expected
```

unless the problem is a tree problem, in which case the test cases should be in the following format:
```python
def tn(nums: list[int | None]):
    return TreeNode.init_from_list(TreeNode, nums)


if __name__ == "__main__":
    from pprint import pformat, pprint
    sol = Solution()
    null = None
    kwargs_list = [
        ({"root"=...}, ...),
    ]
    test_number = 0
    for kwargs, expected in kwargs_list:
        test_number += 1
        print(
            "-"*30+f"\nNew Solution {test_number}.: {pformat(kwargs, indent=2)}")
        print("-"*30+f"\nNew Solution: kwargs = {kwargs}")
        result = sol.fn(root=tn(kwargs["root"]))
        assert result == expected
```
If the tree problem has a solution function that returns None, then this is a modificication of the kwargs in place, so the result should be the kwargs which is modified in place:
```python
    sol = Solution()
    null = None
    kwargs_list = [
        ({"root"=...}, ...),
    ]
    test_number = 0
    for kwargs, expected in kwargs_list:
        test_number += 1
        print(
            "-"*30+f"\nNew Solution {test_number}.: {pformat(kwargs, indent=2)}")
        result = kwargs["root"]
        sol.fn(root=result)
        assert result == expected, f"Test {test_number}. Failed 🚨.\n{
            result}\n"+("!="*15)+f"{expected}"
        print(f"Test {test_number}. Passed ✅")
```

unless the problem is a graph problem, in which case the test cases should be in the following format:
```python
if __name__ == "__main__":
    from pprint import pformat, pprint
    sol = Solution()
    null = None
    kwargs_list = [
        ({"grid": [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]], }, 1),
        ({"grid": [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]], }, 3),
        ({"grid": [
            ["1", "1", "1", "1", "0", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1"],
            ["0", "0", "1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "1", "1", "1"]], }, 2),
        ({"grid": [
            ["1", "1", "1", "1", "0", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1"],
            ["0", "0", "1", "1", "0", "0", "1"],
            ["0", "0", "0", "0", "1", "1", "1"]], }, 1),
    ]
    test_number = 0
    for kwargs, expected in kwargs_list:
        test_number += 1
        print(
            "-"*30+f"\nNew Solution {test_number}.: {pformat(kwargs, indent=2)}")
        result = sol.numIslands(**kwargs)
        assert result == expected, f"Test {test_number}. Failed 🚨.\n{
            result}\n"+("!="*15)+f"{expected}"
        print(f"Test {test_number}. Passed ✅")
```
If the graph problem has a solution function that returns None, then this is a modificication of the kwargs in place, so the result should be the kwargs which is modified in place:
```python
    sol = Solution()
    null = None
    kwargs_list = [
        ({"grid": [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]], }, 1),
    ]
    test_number = 0
    for kwargs, expected in kwargs_list:
        test_number += 1
        print(
            "-"*30+f"\nNew Solution {test_number}.: {pformat(kwargs, indent=2)}")
        result = kwargs["grid"]
        sol.numIslands(grid=result)
        assert result == expected, f"Test {test_number}. Failed 🚨.\n{
            result}\n"+("!="*15)+f"{expected}"
        print(f"Test {test_number}. Passed ✅")
```

unless the problem is a linked list problem, in which case the test cases should be in the following format:
```python
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

if __name__ == "__main__":
    from pprint import pformat, pprint
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
    test_number = 0
    for kwargs, expected in kwargs_list:
        test_number += 1
        print(
            "-"*30+f"\nNew Solution {test_number}.: {pformat(kwargs, indent=2)}")
        result = sol.run(**kwargs)
        x = ll(expected)
        assert result == x
```
If the linked list problem has a solution function that returns None, then this is a modificication of the kwargs in place, so the result should be the kwargs which is modified in place:
```python
    test_number += 1
        print(
            "-"*30+f"\nNew Solution {test_number}.: {pformat(kwargs, indent=2)}")
    result = kwargs["root"]
    sol.flatten(root=result)
    y = result
    assert y == expected
```

unless the problem is a matrix problem, in which case the test cases should be in the following format:
```python
if __name__ == "__main__":
    from pprint import pformat, pprint
    sol = Solution()
    kwargs_list = [
        ({"matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]},
         [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
    ]
    test_number = 0
    for kwargs, expected in kwargs_list:
        test_number += 1
        print(
            "-"*30+f"\nNew Solution {test_number}.: {pformat(kwargs, indent=2)}")
        result = sol.fn(**kwargs)
        assert result == expected
```
If the matrix problem has a solution function that returns None, then this is a modificication of the kwargs in place, so the result should be the kwargs which is modified in place:
```python
    test_number += 1
        print(
            "-"*30+f"\nNew Solution {test_number}.: {pformat(kwargs, indent=2)}")
    result = kwargs["matrix"]
    sol.fn(matrix=result)
    y = result
    assert y == expected
```
"""
