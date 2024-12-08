from __future__ import annotations
from typing import Generic, TypeVar, List, Optional, DefaultDict
from collections import defaultdict, deque

T = TypeVar('T')


class Node:
    def __init__(self, val: int = 0, neighbors: list[Node] = []):
        self.val: int = val
        self.neighbors: list[Node] = neighbors if neighbors is not None else []

    def __repr__(self):
        return f"Node[{self.val}]"

    @classmethod
    def init_from_list(cls, adjacent_vals: list[list[int]]) -> Node:
        """
        adjacent_vals is a list of neighbours, so each item contains a list containing the neighbours vals that that node in that index is adjacent to. i.e. [[2,4],[1,3],[2,4],[1,3]]
        """
        if not adjacent_vals:
            return None
        minuser = min([j for i in adjacent_vals for j in i])
        nodes = {
            i: Node(val=i, neighbors=[])
            for i in range(minuser, len(adjacent_vals)+minuser)
        }
        for i in range(minuser, len(adjacent_vals)+minuser):
            node = nodes[i]
            node.neighbors = [nodes[j] for j in adjacent_vals[i-minuser]]
        return nodes[minuser]

    def to_adjacency_list(self) -> list[list[int]]:
        if not self.neighbors:
            return [[]]
        lu: dict[int, list[int]] = {}
        q = deque([(self.val, self.neighbors)])
        while q:
            cur_val, cur_nbrs = q.popleft()
            lu[cur_val] = [n.val for n in cur_nbrs]
            for nbr in cur_nbrs:
                if nbr.val not in lu:
                    q.append((nbr.val, nbr.neighbors))
        max_val = max(lu.keys())
        result: list[list[int]] = list(range(len(lu)))
        minuser = min(lu.keys())
        for val in lu.keys():
            result[val-minuser] = lu[val]
        return result


# This class represents a graph data structure.
class Graph():
    def __init__(self, data: Optional[DefaultDict[T, List[T]]] = None) -> None:
        """
        This Python function initializes an object with optional data in the form of a defaultdict
        mapping keys to lists.

        :param data: The `data` parameter in the `__init__` method is a dictionary with keys of type `T`
        and values of type `List[T]`. It is an optional parameter that defaults to `None` if not
        provided. If `data` is not provided, a default dictionary with keys
        :type data: Optional[DefaultDict[T, List[T]]]
        """
        self.data: DefaultDict[T, List[T]
                               ] = data if data else defaultdict(list)

    def __getitem__(self, index: T) -> List[T]:
        return self.data[index]

    def __setitem__(self, index: T, value: List[T]):
        self.data[index] = value

    def __str__(self):
        result = []
        for key, values in self.data.items():
            values_str = ', '.join(map(str, values))
            result.append(f'{key}: [{values_str}]')
        return '\n'.join(result)
