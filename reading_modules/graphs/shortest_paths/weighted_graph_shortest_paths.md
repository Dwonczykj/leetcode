[https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/)

Last Updated : 05 Jul, 2024

Given a weighted graph and a source vertex in the graph, find the ****shortest paths**** from the source to all the other vertices in the given graph.

****Note:**** The given graph does not contain any negative edge.

****Examples:****

> ****Input:**** src = 0, the graph is shown below.
> 
> ![1-(2)](https://media.geeksforgeeks.org/wp-content/uploads/20240111182238/Working-of-Dijkstras-Algorithm-768.jpg)
> 
> ****Output:**** 0 4 12 19 21 11 9 8 14  
> ****Explanation:**** The distance from 0 to 1 = 4.  
> The minimum distance from 0 to 2 = 12. 0->1->2  
> The minimum distance from 0 to 3 = 19. 0->1->2->3  
> The minimum distance from 0 to 4 = 21. 0->7->6->5->4  
> The minimum distance from 0 to 5 = 11. 0->7->6->5  
> The minimum distance from 0 to 6 = 9. 0->7->6  
> The minimum distance from 0 to 7 = 8. 0->7  
> The minimum distance from 0 to 8 = 14. 0->1->2->8

## <u><span>Dijkstra’s Algorithm using </span></u> [<u><span>Adjacency Matrix </span></u>](https://www.geeksforgeeks.org/adjacency-matrix-meaning-and-definition-in-dsa/) <u><span>:</span></u>

> The idea is to generate a _****SPT (shortest path tree)****_ with a given source as a root. Maintain an Adjacency Matrix with two sets,
> 
> -   one set contains vertices included in the shortest-path tree,
> -   other set includes vertices not yet included in the shortest-path tree.
> 
> At every step of the algorithm, find a vertex that is in the other set (set not yet included) and has a minimum distance from the source.

<u><b><strong>Algorithm </strong></b></u> :

-   Create a set ****sptSet**** (shortest path tree set) that keeps track of vertices included in the shortest path tree, i.e., whose minimum distance from the source is calculated and finalized. Initially, this set is empty.
-   Assign a distance value to all vertices in the input graph. Initialize all distance values as ****INFINITE**** . Assign the distance value as 0 for the source vertex so that it is picked first.
-   While ****sptSet**** doesn’t include all vertices
    -   Pick a vertex ****u**** that is not there in ****sptSet**** and has a minimum distance value.
    -   Include u to ****sptSet**** .
    -   Then update the distance value of all adjacent vertices of ****u**** .
        -   To update the distance values, iterate through all adjacent vertices.
        -   For every adjacent vertex ****v,**** if the sum of the distance value of ****u**** (from source) and weight of edge ****u-v**** , is less than the distance value of ****v**** , then update the distance value of ****v**** .

****Note:**** We use a boolean array ****sptSet\[\]**** to represent the set of vertices included in ****SPT**** . If a value ****sptSet\[v\]**** is true, then vertex v is included in ****SPT**** , otherwise not. Array ****dist\[\]**** is used to store the shortest distance values of all vertices.

### <u><b><strong>Illustration of Dijkstra Algorithm </strong></b></u> ****:****

> To understand the Dijkstra’s Algorithm lets take a graph and find the shortest path from source to all nodes.
> 
> Consider below graph and ****src = 0****
> 
> ![1-(2)](https://media.geeksforgeeks.org/wp-content/uploads/20240111182238/Working-of-Dijkstras-Algorithm-768.jpg)
> 
> <u><b><strong>Step 1:</strong></b></u>
> 
> -   The set _****sptSet****_ is initially empty and distances assigned to vertices are {0, INF, INF, INF, INF, INF, INF, INF} where ****INF**** indicates infinite.
> -   Now pick the vertex with a minimum distance value. The vertex 0 is picked, include it in _****sptSet****_ . So _****sptSet****_ becomes {0}. After including 0 to _****sptSet****_ , update distance values of its adjacent vertices.
> -   Adjacent vertices of 0 are 1 and 7. The distance values of 1 and 7 are updated as 4 and 8.
> 
> The following subgraph shows vertices and their distance values, only the vertices with finite distance values are shown. The vertices included in ****SPT**** are shown in ****green**** colour.
> 
> ![6](https://media.geeksforgeeks.org/wp-content/uploads/20231121131452/6.jpg)
> 
>   
> <u><b><strong>Step 2:</strong></b></u>
> 
> -   Pick the vertex with minimum distance value and not already included in ****SPT**** (not in ****sptSET**** ). The vertex 1 is picked and added to ****sptSet**** .
> -   So ****sptSet**** now becomes {0, 1}. Update the distance values of adjacent vertices of 1.
> -   The distance value of vertex 2 becomes ****12**** .  
>     ![4](https://media.geeksforgeeks.org/wp-content/uploads/20231121131946/4.jpg)
> 
>   
> <u><b><strong>Step 3:</strong></b></u>
> 
> -   Pick the vertex with minimum distance value and not already included in ****SPT**** (not in ****sptSET**** ). Vertex 7 is picked. So ****sptSet**** now becomes ****{0, 1, 7}.****
> -   Update the distance values of adjacent vertices of 7. The distance value of vertex 6 and 8 becomes finite ( ****15 and 9**** respectively).  
>     ![5](https://media.geeksforgeeks.org/wp-content/uploads/20231121132026/5.jpg)
> 
>   
> <u><b><strong>Step 4:</strong></b></u>
> 
> -   Pick the vertex with minimum distance value and not already included in ****SPT**** (not in ****sptSET**** ). Vertex 6 is picked. So ****sptSet**** now becomes ****{0, 1, 7, 6}**** .
> -   Update the distance values of adjacent vertices of 6. The distance value of vertex 5 and 8 are updated.  
>     ![3-(1)](https://media.geeksforgeeks.org/wp-content/uploads/20231121132105/3-(1).jpg)
> 
>   
> We repeat the above steps until _****sptSet****_ includes all vertices of the given graph. Finally, we get the following S ****hortest Path Tree (SPT).****
> 
> ![2-(2)](https://media.geeksforgeeks.org/wp-content/uploads/20231121132145/2-(2).jpg)

Below is the implementation of the above approach:

C++ C Java Python` ``` <span></span><span># Python program for Dijkstra's single</span> <span># source shortest path algorithm. The program is</span> <span># for adjacency matrix representation of the graph</span>  <span># Library for INT_MAX</span> <span>import</span> <span>sys</span>   <span>class</span> <span>Graph</span><span>():</span>      <span>def</span> <span>__init__</span><span>(</span><span>self</span><span>,</span> <span>vertices</span><span>):</span>         <span>self</span><span>.</span><span>V</span> <span>=</span> <span>vertices</span>         <span>self</span><span>.</span><span>graph</span> <span>=</span> <span>[[</span><span>0</span> <span>for</span> <span>column</span> <span>in</span> <span>range</span><span>(</span><span>vertices</span><span>)]</span>                       <span>for</span> <span>row</span> <span>in</span> <span>range</span><span>(</span><span>vertices</span><span>)]</span>      <span>def</span> <span>printSolution</span><span>(</span><span>self</span><span>,</span> <span>dist</span><span>):</span>         <span>print</span><span>(</span><span>"Vertex </span><span>\t</span><span>Distance from Source"</span><span>)</span>         <span>for</span> <span>node</span> <span>in</span> <span>range</span><span>(</span><span>self</span><span>.</span><span>V</span><span>):</span>             <span>print</span><span>(</span><span>node</span><span>,</span> <span>"</span><span>\t</span><span>"</span><span>,</span> <span>dist</span><span>[</span><span>node</span><span>])</span>      <span># A utility function to find the vertex with</span>     <span># minimum distance value, from the set of vertices</span>     <span># not yet included in shortest path tree</span>     <span>def</span> <span>minDistance</span><span>(</span><span>self</span><span>,</span> <span>dist</span><span>,</span> <span>sptSet</span><span>):</span>          <span># Initialize minimum distance for next node</span>         <span>min</span> <span>=</span> <span>sys</span><span>.</span><span>maxsize</span>          <span># Search not nearest vertex not in the</span>         <span># shortest path tree</span>         <span>for</span> <span>u</span> <span>in</span> <span>range</span><span>(</span><span>self</span><span>.</span><span>V</span><span>):</span>             <span>if</span> <span>dist</span><span>[</span><span>u</span><span>]</span> <span>&lt;</span> <span>min</span> <span>and</span> <span>sptSet</span><span>[</span><span>u</span><span>]</span> <span>==</span> <span>False</span><span>:</span>                 <span>min</span> <span>=</span> <span>dist</span><span>[</span><span>u</span><span>]</span>                 <span>min_index</span> <span>=</span> <span>u</span>          <span>return</span> <span>min_index</span>      <span># Function that implements Dijkstra's single source</span>     <span># shortest path algorithm for a graph represented</span>     <span># using adjacency matrix representation</span>     <span>def</span> <span>dijkstra</span><span>(</span><span>self</span><span>,</span> <span>src</span><span>):</span>          <span>dist</span> <span>=</span> <span>[</span><span>sys</span><span>.</span><span>maxsize</span><span>]</span> <span>*</span> <span>self</span><span>.</span><span>V</span>         <span>dist</span><span>[</span><span>src</span><span>]</span> <span>=</span> <span>0</span>         <span>sptSet</span> <span>=</span> <span>[</span><span>False</span><span>]</span> <span>*</span> <span>self</span><span>.</span><span>V</span>          <span>for</span> <span>cout</span> <span>in</span> <span>range</span><span>(</span><span>self</span><span>.</span><span>V</span><span>):</span>              <span># Pick the minimum distance vertex from</span>             <span># the set of vertices not yet processed.</span>             <span># x is always equal to src in first iteration</span>             <span>x</span> <span>=</span> <span>self</span><span>.</span><span>minDistance</span><span>(</span><span>dist</span><span>,</span> <span>sptSet</span><span>)</span>              <span># Put the minimum distance vertex in the</span>             <span># shortest path tree</span>             <span>sptSet</span><span>[</span><span>x</span><span>]</span> <span>=</span> <span>True</span>              <span># Update dist value of the adjacent vertices</span>             <span># of the picked vertex only if the current</span>             <span># distance is greater than new distance and</span>             <span># the vertex in not in the shortest path tree</span>             <span>for</span> <span>y</span> <span>in</span> <span>range</span><span>(</span><span>self</span><span>.</span><span>V</span><span>):</span>                 <span>if</span> <span>self</span><span>.</span><span>graph</span><span>[</span><span>x</span><span>][</span><span>y</span><span>]</span> <span>&gt;</span> <span>0</span> <span>and</span> <span>sptSet</span><span>[</span><span>y</span><span>]</span> <span>==</span> <span>False</span> <span>and</span> \                         <span>dist</span><span>[</span><span>y</span><span>]</span> <span>&gt;</span> <span>dist</span><span>[</span><span>x</span><span>]</span> <span>+</span> <span>self</span><span>.</span><span>graph</span><span>[</span><span>x</span><span>][</span><span>y</span><span>]:</span>                     <span>dist</span><span>[</span><span>y</span><span>]</span> <span>=</span> <span>dist</span><span>[</span><span>x</span><span>]</span> <span>+</span> <span>self</span><span>.</span><span>graph</span><span>[</span><span>x</span><span>][</span><span>y</span><span>]</span>          <span>self</span><span>.</span><span>printSolution</span><span>(</span><span>dist</span><span>)</span>   <span># Driver's code</span> <span>if</span> <span>__name__</span> <span>==</span> <span>"__main__"</span><span>:</span>     <span>g</span> <span>=</span> <span>Graph</span><span>(</span><span>9</span><span>)</span>     <span>g</span><span>.</span><span>graph</span> <span>=</span> <span>[[</span><span>0</span><span>,</span> <span>4</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>8</span><span>,</span> <span>0</span><span>],</span>                <span>[</span><span>4</span><span>,</span> <span>0</span><span>,</span> <span>8</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>11</span><span>,</span> <span>0</span><span>],</span>                <span>[</span><span>0</span><span>,</span> <span>8</span><span>,</span> <span>0</span><span>,</span> <span>7</span><span>,</span> <span>0</span><span>,</span> <span>4</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>2</span><span>],</span>                <span>[</span><span>0</span><span>,</span> <span>0</span><span>,</span> <span>7</span><span>,</span> <span>0</span><span>,</span> <span>9</span><span>,</span> <span>14</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>],</span>                <span>[</span><span>0</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>9</span><span>,</span> <span>0</span><span>,</span> <span>10</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>],</span>                <span>[</span><span>0</span><span>,</span> <span>0</span><span>,</span> <span>4</span><span>,</span> <span>14</span><span>,</span> <span>10</span><span>,</span> <span>0</span><span>,</span> <span>2</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>],</span>                <span>[</span><span>0</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>2</span><span>,</span> <span>0</span><span>,</span> <span>1</span><span>,</span> <span>6</span><span>],</span>                <span>[</span><span>8</span><span>,</span> <span>11</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>1</span><span>,</span> <span>0</span><span>,</span> <span>7</span><span>],</span>                <span>[</span><span>0</span><span>,</span> <span>0</span><span>,</span> <span>2</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>0</span><span>,</span> <span>6</span><span>,</span> <span>7</span><span>,</span> <span>0</span><span>]</span>                <span>]</span>      <span>g</span><span>.</span><span>dijkstra</span><span>(</span><span>0</span><span>)</span>  <span># This code is contributed by Divyanshu Mehta and Updated by Pranav Singh Sambyal</span> ``` `
C# JavaScript

**Output**

```
Vertex      Distance from Source
0                 0
1                 4
2                 12
3                 19
4                 21
5                 11
6                 9
7                 8
8                 14
```

****Time Complexity:**** O(V <sup><span>2 </span></sup> )  
****Auxiliary Space:**** O(V)

****Notes:****

-   The code calculates the shortest distance but doesn’t calculate the path information. Create a parent array, update the parent array when distance is updated and use it to show the shortest path from source to different vertices.
-   The time Complexity of the implementation is ****O(V**** **<sup><strong>2 </strong></sup>** ****)**** . If the input [graph is represented using adjacency list](https://www.geeksforgeeks.org/graph-and-its-representations/) , it can be reduced to O(E \* log V) with the help of a binary heap. Please see [Dijkstra’s Algorithm for Adjacency List Representation](https://www.geeksforgeeks.org/greedy-algorithms-set-7-dijkstras-algorithm-for-adjacency-list-representation/) for more details.
-   Dijkstra’s algorithm doesn’t work for graphs with negative weight cycles.

## <u><span>Why Dijkstra’s Algorithms fails for the Graphs having Negative Edges ?</span></u>

The problem with negative weights arises from the fact that Dijkstra’s algorithm assumes that once a node is added to the set of visited nodes, its distance is finalized and will not change. However, in the presence of negative weights, this assumption can lead to incorrect results.

Consider the following graph for the example:

![Failure-of-Dijkstra-in-case-of-negative-edges](https://media.geeksforgeeks.org/wp-content/uploads/20231106115051/Failure-of-Dijkstra-in-case-of-negative-edges.jpg)

In the above graph, A is the source node, among the edges ****A**** to ****B**** and ****A**** to ****C**** , ****A**** to ****B**** is the smaller weight and Dijkstra assigns the shortest distance of ****B**** as 2, but because of existence of a negative edge from ****C**** to ****B**** , the actual shortest distance reduces to 1 which Dijkstra fails to detect.

****Note:**** We use [Bellman Ford’s Shortest path algorithm](https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/) in case we have negative edges in the graph.

## <u><span>Dijkstra’s Algorithm using </span></u> [<u><span>Adjacency List </span></u>](https://www.geeksforgeeks.org/adjacency-list-meaning-definition-in-dsa/) <u><span>in O(E logV):</span></u>

> For Dijkstra’s algorithm, it is always recommended to use [****Heap****](https://www.geeksforgeeks.org/heap-data-structure/) (or ****priority queue**** ) as the required operations (extract minimum and decrease key) match with the speciality of the heap (or priority queue). However, the problem is, that priority\_queue doesn’t support the decrease key. To resolve this problem, do not update a key, but insert one more copy of it. So we allow multiple instances of the same vertex in the priority queue. This approach doesn’t require decreasing key operations and has below important properties.
> 
> -   Whenever the distance of a vertex is reduced, we add one more instance of a vertex in priority\_queue. Even if there are multiple instances, we only consider the instance with minimum distance and ignore other instances.
> -   The time complexity remains ****O(E \* LogV)**** as there will be at most O(E) vertices in the priority queue and O(logE) is the same as O(logV)

Below is the implementation of the above approach:

C++ Java Python` ``` <span></span><span>import</span> <span>heapq</span>  <span># iPair ==&gt; Integer Pair</span> <span>iPair</span> <span>=</span> <span>tuple</span>  <span># This class represents a directed graph using</span> <span># adjacency list representation</span> <span>class</span> <span>Graph</span><span>:</span>     <span>def</span> <span>__init__</span><span>(</span><span>self</span><span>,</span> <span>V</span><span>:</span> <span>int</span><span>):</span> <span># Constructor</span>         <span>self</span><span>.</span><span>V</span> <span>=</span> <span>V</span>         <span>self</span><span>.</span><span>adj</span> <span>=</span> <span>[[]</span> <span>for</span> <span>_</span> <span>in</span> <span>range</span><span>(</span><span>V</span><span>)]</span>      <span>def</span> <span>addEdge</span><span>(</span><span>self</span><span>,</span> <span>u</span><span>:</span> <span>int</span><span>,</span> <span>v</span><span>:</span> <span>int</span><span>,</span> <span>w</span><span>:</span> <span>int</span><span>):</span>         <span>self</span><span>.</span><span>adj</span><span>[</span><span>u</span><span>]</span><span>.</span><span>append</span><span>((</span><span>v</span><span>,</span> <span>w</span><span>))</span>         <span>self</span><span>.</span><span>adj</span><span>[</span><span>v</span><span>]</span><span>.</span><span>append</span><span>((</span><span>u</span><span>,</span> <span>w</span><span>))</span>      <span># Prints shortest paths from src to all other vertices</span>     <span>def</span> <span>shortestPath</span><span>(</span><span>self</span><span>,</span> <span>src</span><span>:</span> <span>int</span><span>):</span>         <span># Create a priority queue to store vertices that</span>         <span># are being preprocessed</span>         <span>pq</span> <span>=</span> <span>[]</span>         <span>heapq</span><span>.</span><span>heappush</span><span>(</span><span>pq</span><span>,</span> <span>(</span><span>0</span><span>,</span> <span>src</span><span>))</span>          <span># Create a vector for distances and initialize all</span>         <span># distances as infinite (INF)</span>         <span>dist</span> <span>=</span> <span>[</span><span>float</span><span>(</span><span>'inf'</span><span>)]</span> <span>*</span> <span>self</span><span>.</span><span>V</span>         <span>dist</span><span>[</span><span>src</span><span>]</span> <span>=</span> <span>0</span>          <span>while</span> <span>pq</span><span>:</span>             <span># The first vertex in pair is the minimum distance</span>             <span># vertex, extract it from priority queue.</span>             <span># vertex label is stored in second of pair</span>             <span>d</span><span>,</span> <span>u</span> <span>=</span> <span>heapq</span><span>.</span><span>heappop</span><span>(</span><span>pq</span><span>)</span>              <span># 'i' is used to get all adjacent vertices of a</span>             <span># vertex</span>             <span>for</span> <span>v</span><span>,</span> <span>weight</span> <span>in</span> <span>self</span><span>.</span><span>adj</span><span>[</span><span>u</span><span>]:</span>                 <span># If there is shorted path to v through u.</span>                 <span>if</span> <span>dist</span><span>[</span><span>v</span><span>]</span> <span>&gt;</span> <span>dist</span><span>[</span><span>u</span><span>]</span> <span>+</span> <span>weight</span><span>:</span>                     <span># Updating distance of v</span>                     <span>dist</span><span>[</span><span>v</span><span>]</span> <span>=</span> <span>dist</span><span>[</span><span>u</span><span>]</span> <span>+</span> <span>weight</span>                     <span>heapq</span><span>.</span><span>heappush</span><span>(</span><span>pq</span><span>,</span> <span>(</span><span>dist</span><span>[</span><span>v</span><span>],</span> <span>v</span><span>))</span>          <span># Print shortest distances stored in dist[]</span>         <span>for</span> <span>i</span> <span>in</span> <span>range</span><span>(</span><span>self</span><span>.</span><span>V</span><span>):</span>             <span>print</span><span>(</span><span>f</span><span>"</span><span>{</span><span>i</span><span>}</span><span> </span><span>\t\t</span><span> </span><span>{</span><span>dist</span><span>[</span><span>i</span><span>]</span><span>}</span><span>"</span><span>)</span>  <span># Driver's code</span> <span>if</span> <span>__name__</span> <span>==</span> <span>"__main__"</span><span>:</span>     <span># create the graph given in above figure</span>     <span>V</span> <span>=</span> <span>9</span>     <span>g</span> <span>=</span> <span>Graph</span><span>(</span><span>V</span><span>)</span>      <span># making above shown graph</span>     <span>g</span><span>.</span><span>addEdge</span><span>(</span><span>0</span><span>,</span> <span>1</span><span>,</span> <span>4</span><span>)</span>     <span>g</span><span>.</span><span>addEdge</span><span>(</span><span>0</span><span>,</span> <span>7</span><span>,</span> <span>8</span><span>)</span>     <span>g</span><span>.</span><span>addEdge</span><span>(</span><span>1</span><span>,</span> <span>2</span><span>,</span> <span>8</span><span>)</span>     <span>g</span><span>.</span><span>addEdge</span><span>(</span><span>1</span><span>,</span> <span>7</span><span>,</span> <span>11</span><span>)</span>     <span>g</span><span>.</span><span>addEdge</span><span>(</span><span>2</span><span>,</span> <span>3</span><span>,</span> <span>7</span><span>)</span>     <span>g</span><span>.</span><span>addEdge</span><span>(</span><span>2</span><span>,</span> <span>8</span><span>,</span> <span>2</span><span>)</span>     <span>g</span><span>.</span><span>addEdge</span><span>(</span><span>2</span><span>,</span> <span>5</span><span>,</span> <span>4</span><span>)</span>     <span>g</span><span>.</span><span>addEdge</span><span>(</span><span>3</span><span>,</span> <span>4</span><span>,</span> <span>9</span><span>)</span>     <span>g</span><span>.</span><span>addEdge</span><span>(</span><span>3</span><span>,</span> <span>5</span><span>,</span> <span>14</span><span>)</span>     <span>g</span><span>.</span><span>addEdge</span><span>(</span><span>4</span><span>,</span> <span>5</span><span>,</span> <span>10</span><span>)</span>     <span>g</span><span>.</span><span>addEdge</span><span>(</span><span>5</span><span>,</span> <span>6</span><span>,</span> <span>2</span><span>)</span>     <span>g</span><span>.</span><span>addEdge</span><span>(</span><span>6</span><span>,</span> <span>7</span><span>,</span> <span>1</span><span>)</span>     <span>g</span><span>.</span><span>addEdge</span><span>(</span><span>6</span><span>,</span> <span>8</span><span>,</span> <span>6</span><span>)</span>     <span>g</span><span>.</span><span>addEdge</span><span>(</span><span>7</span><span>,</span> <span>8</span><span>,</span> <span>7</span><span>)</span>      <span>g</span><span>.</span><span>shortestPath</span><span>(</span><span>0</span><span>)</span> ``` `
C# JavaScript

**Output**

```
Vertex Distance from Source
0          0
1          4
2          12
3          19
4          21
5          11
6          9
7          8
8          14
```

****Time Complexity:**** O(E \* logV), Where E is the number of edges and V is the number of vertices.  
****Auxiliary Space:**** O(V)

## <u><span>Applications of Dijkstra’s Algorithm:</span></u>

-   ****Google maps**** uses Dijkstra algorithm to show shortest distance between source and destination.
-   In ****computer networking**** , Dijkstra’s algorithm forms the basis for various routing protocols, such as OSPF (Open Shortest Path First) and IS-IS (Intermediate System to Intermediate System).
-   Transportation and traffic management systems use Dijkstra’s algorithm to optimize traffic flow, minimize congestion, and plan the most efficient routes for vehicles.
-   Airlines use Dijkstra’s algorithm to plan flight paths that minimize fuel consumption, reduce travel time.
-   Dijkstra’s algorithm is applied in electronic design automation for routing connections on integrated circuits and very-large-scale integration (VLSI) chips.

For a more detailed explanation refer to this article [Dijkstra’s Shortest Path Algorithm using priority\_queue of STL](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-using-priority_queue-stl/) .

Are you looking to bridge the gap from **Data Structures and Algorithms (DSA) to Software Development**? Dive into our [**DSA to Development - Beginner to Advance Course**](https://gfgcdn.com/tu/Q8V/) on GeeksforGeeks, crafted for aspiring developers and seasoned programmers alike. Explore essential coding skills, software engineering principles, and practical application techniques through hands-on **projects** and real-world examples. Whether you're starting your journey or aiming to refine your skills, this course empowers you to build robust software solutions. Ready to advance your programming prowess? Enroll now and transform your coding capabilities!