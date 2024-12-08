[https://www.geeksforgeeks.org/topological-sorting/](https://www.geeksforgeeks.org/topological-sorting/)

Last Updated : 28 Apr, 2024

Topological sorting for ****Directed Acyclic Graph (DAG)**** is a linear ordering of vertices such that for every directed edge u-v, vertex ****u**** comes before ****v**** in the ordering.

****Note:**** Topological Sorting for a graph is not possible if the graph is not a ****DAG****.

****Example:****

> ****Input:**** Graph :
> 
> ![example](https://media.geeksforgeeks.org/wp-content/uploads/20231016113524/example.png)
> 
> Example
> 
> ****Output:**** 5 4 2 3 1 0  
> ****Explanation:**** The first vertex in topological sorting is always a vertex with an in-degree of 0 (a vertex with no incoming edges).  A topological sorting of the following graph is “5 4 2 3 1 0”. There can be more than one topological sorting for a graph. Another topological sorting of the following graph is “4 5 2 3 1 0”.

## ****Topological Sorting**** ****vs Depth First Traversal (DFS)****: 

In [DFS](https://www.geeksforgeeks.org/depth-first-traversal-for-a-graph/), we print a vertex and then recursively call DFS for its adjacent vertices. In topological sorting, we need to print a vertex before its adjacent vertices. 

****For example,**** In the above given graph, the vertex ‘5’ should be printed before vertex ‘0’, but unlike [DFS](https://www.geeksforgeeks.org/depth-first-traversal-for-a-graph/), the vertex ‘4’ should also be printed before vertex ‘0’. So Topological sorting is different from DFS. For example, a DFS of the shown graph is “5 2 3 1 0 4”, but it is not a topological sorting.

## Topological Sorting in Directed Acyclic Graphs (DAGs)

****DAGs**** are a special type of graphs in which each edge is directed such that no cycle exists in the graph, before understanding why Topological sort only exists for DAGs, lets first answer two questions:

-   ****Why Topological Sort is not possible for graphs with undirected edges?****

> This is due to the fact that undirected edge between two vertices ****u**** and ****v**** means, there is an edge from ****u**** to ****v**** as well as from ****v**** to ****u****. Because of this both the nodes ****u**** and ****v**** depend upon each other and none of them can appear before the other in the topological ordering without creating a contradiction.

-   ****Why Topological Sort is not possible for graphs having cycles?****

> Imagine a graph with 3 vertices and edges = {1 to 2 , 2 to 3, 3 to 1} forming a cycle. Now if we try to topologically sort this graph starting from any vertex, it will always create a contradiction to our definition. All the vertices in a cycle are indirectly dependent on each other hence topological sorting fails.

Hence, a ****Directed Acyclic Graph**** removes the contradiction created by above two questions, hence it is suitable for topological ordering. A [DFS based solution to find a topological sort](https://www.geeksforgeeks.org/topological-sorting/) has already been discussed.

## Topological order may not be Unique:

> ****Topological sorting**** is a dependency problem in which completion of one task depends upon the completion of several other tasks whose order can vary. Let us understand this concept via an example:
> 
> Suppose our task is to reach our School and in order to reach there, first we need to get dressed. The dependencies to wear clothes is shown in the below dependency graph. For example you can not wear shoes before wearing socks.
> 
> ![1](https://media.geeksforgeeks.org/wp-content/uploads/20231106112211/1.jpg)
> 
> From the above image you would have already realized that there exist multiple ways to get dressed, the below image shows some of those ways.
> 
> ![2](https://media.geeksforgeeks.org/wp-content/uploads/20231106112408/2.jpg)
> 
> Can you list [all the possible topological ordering](https://www.geeksforgeeks.org/all-topological-sorts-of-a-directed-acyclic-graph/) of getting dressed for above dependency graph?

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

> ****Step 1:****
> 
> -   We start DFS from node 0 because it has zero incoming Nodes
> -   We push node 0 in the stack and move to next node having minimum number of adjacent nodes i.e. node 1.
> 
> ![file](https://media.geeksforgeeks.org/wp-content/uploads/20230914175432/file.png)
> 
> ****Step 2:****
> 
> -   In this step , because there is no adjacent of this node so push the node 1 in the stack and move to next node.
> 
> ![file](https://media.geeksforgeeks.org/wp-content/uploads/20230914175548/file.png)
> 
> ****Step 3:****
> 
> -   In this step , We choose node 2 because it has minimum number of adjacent nodes after 0 and 1 .
> -   We call DFS for node 2 and push all the nodes which comes in traversal from node 2 in reverse order.
> -   So push 3 then push 2 .
> 
> ![file](https://media.geeksforgeeks.org/wp-content/uploads/20230914175605/file.png)
> 
> ****Step 4:****
> 
> -   We now call DFS for node 4
> -   Because 0 and 1 already present in the stack so we just push node 4 in the stack and return.
> 
> ![file](https://media.geeksforgeeks.org/wp-content/uploads/20230914175620/file.png)
> 
> ****Step 5:****
> 
> -   In this step because all the adjacent nodes of 5 is already in the stack we push node 5 in the stack and return.
> 
> ![file](https://media.geeksforgeeks.org/wp-content/uploads/20230914175633/file.png)
> 
> ****Step 6:**** This is the final step of the Topological sorting in which we pop all the element from the stack and print it in that order .

Below is the implementation of the above approach:

C++ Java Python3` ``` <span></span><span>def</span> <span>topologicalSortUtil</span><span>(</span><span>v</span><span>,</span> <span>adj</span><span>,</span> <span>visited</span><span>,</span> <span>stack</span><span>):</span>     <span># Mark the current node as visited</span>     <span>visited</span><span>[</span><span>v</span><span>]</span> <span>=</span> <span>True</span>      <span># Recur for all adjacent vertices</span>     <span>for</span> <span>i</span> <span>in</span> <span>adj</span><span>[</span><span>v</span><span>]:</span>         <span>if</span> <span>not</span> <span>visited</span><span>[</span><span>i</span><span>]:</span>             <span>topologicalSortUtil</span><span>(</span><span>i</span><span>,</span> <span>adj</span><span>,</span> <span>visited</span><span>,</span> <span>stack</span><span>)</span>      <span># Push current vertex to stack which stores the result</span>     <span>stack</span><span>.</span><span>append</span><span>(</span><span>v</span><span>)</span>   <span># Function to perform Topological Sort</span> <span>def</span> <span>topologicalSort</span><span>(</span><span>adj</span><span>,</span> <span>V</span><span>):</span>     <span># Stack to store the result</span>     <span>stack</span> <span>=</span> <span>[]</span>      <span>visited</span> <span>=</span> <span>[</span><span>False</span><span>]</span> <span>*</span> <span>V</span>      <span># Call the recursive helper function to store</span>     <span># Topological Sort starting from all vertices one by</span>     <span># one</span>     <span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>V</span><span>):</span>         <span>if</span> <span>not</span> <span>visited</span><span>[</span><span>i</span><span>]:</span>             <span>topologicalSortUtil</span><span>(</span><span>i</span><span>,</span> <span>adj</span><span>,</span> <span>visited</span><span>,</span> <span>stack</span><span>)</span>      <span># Print contents of stack</span>     <span>print</span><span>(</span><span>"Topological sorting of the graph:"</span><span>,</span> <span>end</span><span>=</span><span>" "</span><span>)</span>     <span>while</span> <span>stack</span><span>:</span>         <span>print</span><span>(</span><span>stack</span><span>.</span><span>pop</span><span>(),</span> <span>end</span><span>=</span><span>" "</span><span>)</span>   <span># Driver code</span> <span>if</span> <span>__name__</span> <span>==</span> <span>"__main__"</span><span>:</span>     <span># Number of nodes</span>     <span>V</span> <span>=</span> <span>4</span>      <span># Edges</span>     <span>edges</span> <span>=</span> <span>[[</span><span>0</span><span>,</span> <span>1</span><span>],</span> <span>[</span><span>1</span><span>,</span> <span>2</span><span>],</span> <span>[</span><span>3</span><span>,</span> <span>1</span><span>],</span> <span>[</span><span>3</span><span>,</span> <span>2</span><span>]]</span>      <span># Graph represented as an adjacency list</span>     <span>adj</span> <span>=</span> <span>[[]</span> <span>for</span> <span>_</span> <span>in</span> <span>range</span><span>(</span><span>V</span><span>)]</span>      <span>for</span> <span>i</span> <span>in</span> <span>edges</span><span>:</span>         <span>adj</span><span>[</span><span>i</span><span>[</span><span>0</span><span>]]</span><span>.</span><span>append</span><span>(</span><span>i</span><span>[</span><span>1</span><span>])</span>      <span>topologicalSort</span><span>(</span><span>adj</span><span>,</span> <span>V</span><span>)</span> ``` `
C# JavaScript

**Output**

```
Topological sorting of the graph: 3 0 1 2 
```

****Time Complexity:**** O(V+E). The above algorithm is simply DFS with an extra stack. So time complexity is the same as DFS  
****Auxiliary space:**** O(V). The extra space is needed for the stack

****Topological Sorting Using BFS:****

C++ Java Python3` ``` <span></span><span>from</span> <span>collections</span> <span>import</span> <span>defaultdict</span>   <span>class</span> <span>Graph</span><span>:</span>     <span>def</span> <span>__init__</span><span>(</span><span>self</span><span>,</span> <span>vertices</span><span>):</span>         <span># Number of vertices</span>         <span>self</span><span>.</span><span>V</span> <span>=</span> <span>vertices</span>           <span># Dictionary to store adjacency lists</span>         <span>self</span><span>.</span><span>adj</span> <span>=</span> <span>defaultdict</span><span>(</span><span>list</span><span>)</span>        <span>def</span> <span>addEdge</span><span>(</span><span>self</span><span>,</span> <span>u</span><span>,</span> <span>v</span><span>):</span>         <span># Function to add an edge to the graph</span>         <span>self</span><span>.</span><span>adj</span><span>[</span><span>u</span><span>]</span><span>.</span><span>append</span><span>(</span><span>v</span><span>)</span>      <span>def</span> <span>topologicalSort</span><span>(</span><span>self</span><span>):</span>         <span># Function to perform Topological Sort</span>         <span># Create a list to store in-degree of all vertices</span>         <span>in_degree</span> <span>=</span> <span>[</span><span>0</span><span>]</span> <span>*</span> <span>self</span><span>.</span><span>V</span>          <span># Traverse adjacency lists to fill in_degree of vertices</span>         <span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>self</span><span>.</span><span>V</span><span>):</span>             <span>for</span> <span>j</span> <span>in</span> <span>self</span><span>.</span><span>adj</span><span>[</span><span>i</span><span>]:</span>                 <span>in_degree</span><span>[</span><span>j</span><span>]</span> <span>+=</span> <span>1</span>          <span># Create a queue and enqueue all vertices with in-degree 0</span>         <span>q</span> <span>=</span> <span>[]</span>         <span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>self</span><span>.</span><span>V</span><span>):</span>             <span>if</span> <span>in_degree</span><span>[</span><span>i</span><span>]</span> <span>==</span> <span>0</span><span>:</span>                 <span>q</span><span>.</span><span>append</span><span>(</span><span>i</span><span>)</span>          <span># Initialize count of visited vertices</span>         <span>count</span> <span>=</span> <span>0</span>          <span># Create a list to store topological order</span>         <span>top_order</span> <span>=</span> <span>[]</span>          <span># One by one dequeue vertices from queue and enqueue</span>         <span># adjacent vertices if in-degree of adjacent becomes 0</span>         <span>while</span> <span>q</span><span>:</span>             <span># Extract front of queue (or perform dequeue)</span>             <span># and add it to topological order</span>             <span>u</span> <span>=</span> <span>q</span><span>.</span><span>pop</span><span>(</span><span>0</span><span>)</span>             <span>top_order</span><span>.</span><span>append</span><span>(</span><span>u</span><span>)</span>              <span># Iterate through all its neighbouring nodes</span>             <span># of dequeued node u and decrease their in-degree</span>             <span># by 1</span>             <span>for</span> <span>node</span> <span>in</span> <span>self</span><span>.</span><span>adj</span><span>[</span><span>u</span><span>]:</span>                 <span># If in-degree becomes zero, add it to queue</span>                 <span>in_degree</span><span>[</span><span>node</span><span>]</span> <span>-=</span> <span>1</span>                 <span>if</span> <span>in_degree</span><span>[</span><span>node</span><span>]</span> <span>==</span> <span>0</span><span>:</span>                     <span>q</span><span>.</span><span>append</span><span>(</span><span>node</span><span>)</span>              <span>count</span> <span>+=</span> <span>1</span>          <span># Check if there was a cycle</span>         <span>if</span> <span>count</span> <span>!=</span> <span>self</span><span>.</span><span>V</span><span>:</span>             <span>print</span><span>(</span><span>"Graph contains cycle"</span><span>)</span>             <span>return</span>          <span># Print topological order</span>         <span>print</span><span>(</span><span>"Topological Sort:"</span><span>,</span> <span>top_order</span><span>)</span>   <span># Driver code</span> <span>if</span> <span>__name__</span> <span>==</span> <span>"__main__"</span><span>:</span>     <span># Create a graph given in the above diagram</span>     <span>g</span> <span>=</span> <span>Graph</span><span>(</span><span>6</span><span>)</span>     <span>g</span><span>.</span><span>addEdge</span><span>(</span><span>5</span><span>,</span> <span>2</span><span>)</span>     <span>g</span><span>.</span><span>addEdge</span><span>(</span><span>5</span><span>,</span> <span>0</span><span>)</span>     <span>g</span><span>.</span><span>addEdge</span><span>(</span><span>4</span><span>,</span> <span>0</span><span>)</span>     <span>g</span><span>.</span><span>addEdge</span><span>(</span><span>4</span><span>,</span> <span>1</span><span>)</span>     <span>g</span><span>.</span><span>addEdge</span><span>(</span><span>2</span><span>,</span> <span>3</span><span>)</span>     <span>g</span><span>.</span><span>addEdge</span><span>(</span><span>3</span><span>,</span> <span>1</span><span>)</span>      <span>print</span><span>(</span><span>"Following is a Topological Sort of the given graph"</span><span>)</span>     <span>g</span><span>.</span><span>topologicalSort</span><span>()</span> ``` `
JavaScript

**Output**

```
Following is a Topological Sort of the given graph
4 5 2 0 3 1 
```

****Time Complexity:****

The time complexity for constructing the graph is O(V + E), where V is the number of vertices and E is the number of edges.

The time complexity for performing topological sorting using BFS is also O(V + E), where V is the number of vertices and E is the number of edges. This is because each vertex and each edge is visited once during the BFS traversal.

****Space Complexity:****

The space complexity for storing the graph using an adjacency list is O(V + E), where V is the number of vertices and E is the number of edges.

Additional space is used for storing the in-degree of vertices, which requires O(V) space.

A queue is used for BFS traversal, which can contain at most V vertices. Thus, the space complexity for the queue is O(V).

Overall, the space complexity of the algorithm is O(V + E) due to the storage of the graph, in-degree array, and the queue.

In summary, the time complexity of the provided implementation is O(V + E), and the space complexity is also O(V + E).

****Note:**** Here, we can also use a array instead of the stack. If the array is used then print the elements in reverse order to get the topological sorting.

## ****Advantages of Topological Sort:****

-   Helps in scheduling tasks or events based on dependencies.
-   Detects cycles in a directed graph.
-   Efficient for solving problems with precedence constraints.

## Disadvantages of Topological Sort:

-   Only applicable to directed acyclic graphs (DAGs), not suitable for cyclic graphs.
-   May not be unique, multiple valid topological orderings can exist.
-   Inefficient for large graphs with many nodes and edges.

## Applications of Topological Sort:

-   Task scheduling and project management.
-   Dependency resolution in package management systems.
-   Determining the order of compilation in software build systems.
-   Deadlock detection in operating systems.
-   Course scheduling in universities.

****Related Articles:**** 

-   [Kahn’s algorithm for Topological Sorting](https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/)
-   [All Topological Sorts of a Directed Acyclic Graph](https://www.geeksforgeeks.org/all-topological-sorts-of-a-directed-acyclic-graph/)

Are you looking to bridge the gap from **Data Structures and Algorithms (DSA) to Software Development**? Dive into our [**DSA to Development - Beginner to Advance Course**](https://gfgcdn.com/tu/Q8V/) on GeeksforGeeks, crafted for aspiring developers and seasoned programmers alike. Explore essential coding skills, software engineering principles, and practical application techniques through hands-on **projects** and real-world examples. Whether you're starting your journey or aiming to refine your skills, this course empowers you to build robust software solutions. Ready to advance your programming prowess? Enroll now and transform your coding capabilities!