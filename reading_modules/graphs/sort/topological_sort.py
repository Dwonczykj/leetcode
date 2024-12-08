#  https://www.geeksforgeeks.org/topological-sorting/


'''
```md
## ****Algorithm for Topological Sorting using DFS:****

Here’s a step-by-step algorithm for topological sorting using Depth First Search (DFS):

-   Create a graph with ****n**** vertices and ****m****\-directed edges.
-   Initialize a stack and a visited array of size ****n****.
-   For each unvisited vertex in the graph, do the following:
    -   Call the DFS function with the vertex as the parameter.
    -   In the DFS function, mark the vertex as visited and recursively call the DFS function for all unvisited neighbors of the vertex.
    -   Once all the neighbors have been visited, push the vertex onto the stack.
-   After all, vertices have been visited, pop elements from the stack and append them to the output list until the stack is empty.
-   The resulting list is the topologically sorted order of the graph.

## Illustration Topological Sorting Algorithm:

Below image is an illustration of the above approach:

![Topological-sorting](https://media.geeksforgeeks.org/wp-content/uploads/20230914164620/Topological-sorting.png)

Overall workflow of topological sorting
```
'''

'''
Steps:
Step 1:

We start DFS from node 0 because it has zero incoming Nodes
We push node 0 in the stack and move to next node having minimum number of adjacent nodes i.e. node 1.
file

Step 2:

In this step , because there is no adjacent of this node so push the node 1 in the stack and move to next node.
file

Step 3:

In this step , We choose node 2 because it has minimum number of adjacent nodes after 0 and 1 .
We call DFS for node 2 and push all the nodes which comes in traversal from node 2 in reverse order.
So push 3 then push 2 .
file

Step 4:

We now call DFS for node 4
Because 0 and 1 already present in the stack so we just push node 4 in the stack and return.
file

Step 5:

In this step because all the adjacent nodes of 5 is already in the stack we push node 5 in the stack and return.
file

Step 6: This is the final step of the Topological sorting in which we pop all the element from the stack and print it in that order .
'''




from collections import deque
def topologicalSortUtil(v, adj, visited, stack):
    """AI is creating summary for topologicalSortUtil

    Args:
        v ([type]): [description]
        adj ([type]): [description]
        visited ([type]): [description]
        stack ([type]): [description]
    """
    # Mark the current node as visited
    visited[v] = True

    # Recur for all adjacent vertices
    for i in adj[v]:
        if not visited[i]:
            topologicalSortUtil(i, adj, visited, stack)

    # Push current vertex to stack which stores the result
    stack.append(v)


# Function to perform Topological Sort
def topologicalSort(adj, V):
    # Stack to store the result
    stack = []

    visited = [False] * V

    # Call the recursive helper function to store
    # Topological Sort starting from all vertices one by
    # one
    for i in range(V):
        if not visited[i]:
            topologicalSortUtil(i, adj, visited, stack)

    # Print contents of stack
    print("Topological sorting of the graph:", end=" ")
    while stack:
        print(stack.pop(), end=" ")


# Driver code
if __name__ == "__main__":
    # Number of nodes
    V = 4

    # Edges
    edges = [[0, 1], [1, 2], [3, 1], [3, 2]]

    # Graph represented as an adjacency list
    adj = [[] for _ in range(V)]

    for i in edges:
        adj[i[0]].append(i[1])

    topologicalSort(adj, V)


# Kahns Algorithm - What I was trying to do in 2392.py
# Function to return list containing vertices in Topological order.

'''
Key Points:
Algorithm:
 - Add all nodes with in-degree 0 to a queue.
 - While the queue is not empty:
    - Remove a node from the queue.
    - For each outgoing edge from the removed node, decrement the in-degree of the destination node by 1.
    - If the in-degree of a destination node becomes 0, add it to the queue.
 - If the queue is empty and there are still nodes in the graph, the graph contains a cycle and cannot be topologically sorted.
 - The nodes in the queue represent the topological ordering of the graph.

How to find the in-degree of each node? 
To find the in-degree of each node by initially calculating the number of incoming edges to each node. 
Iterate through all the edges in the graph and increment the in-degree of the destination node for each edge. 
This way, you can determine the in-degree of each node before starting the sorting process.
'''


def topological_sort(adj, V):
    # Vector to store indegree of each vertex
    indegree = [0] * V
    for i in range(V):
        for vertex in adj[i]:
            indegree[vertex] += 1

    # Queue to store vertices with indegree 0
    q = deque()
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)
    result = []
    while q:
        node = q.popleft()
        result.append(node)
        # Decrease indegree of adjacent vertices as the current node is in topological order
        for adjacent in adj[node]:
            indegree[adjacent] -= 1
            # If indegree becomes 0, push it to the queue
            if indegree[adjacent] == 0:
                q.append(adjacent)

    # Check for cycle
    if len(result) != V:
        print("Graph contains cycle!")
        return []
    return result


if __name__ == "__main__":
    n = 6  # Number of nodes

    # Edges
    edges = [[0, 1], [1, 2], [2, 3], [4, 5], [5, 1], [5, 2]]

    # Graph represented as an adjacency list
    adj = [[] for _ in range(n)]

    # Constructing adjacency list
    for edge in edges:
        adj[edge[0]].append(edge[1])

    # Performing topological sort
    print("Topological sorting of the graph:", end=" ")
    result = topological_sort(adj, n)

    # Displaying result
    for vertex in result:
        print(vertex, end=" ")
