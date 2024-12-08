[https://www.geeksforgeeks.org/johnsons-algorithm/](https://www.geeksforgeeks.org/johnsons-algorithm/)

Last Updated : 10 Aug, 2023

The problem is to find the shortest paths between every pair of vertices in a given weighted directed Graph and weights may be negative. We have discussed [Floyd Warshall Algorithm](https://www.geeksforgeeks.org/dynamic-programming-set-16-floyd-warshall-algorithm/) for this problem.  The time complexity of the Floyd Warshall Algorithm is Θ(V<sup><span>3</span></sup>). 

__Using Johnson’s algorithm, we can find all pair shortest paths in O(V___<sup><em>2</em></sup>___log V + VE) time.__ Johnson’s algorithm uses both [Dijkstra](https://www.geeksforgeeks.org/greedy-algorithms-set-6-dijkstras-shortest-path-algorithm/) and [Bellman-Ford](https://www.geeksforgeeks.org/dynamic-programming-set-23-bellman-ford-algorithm/) as subroutines. If we apply [Dijkstra’s Single Source shortest path algorithm](https://www.geeksforgeeks.org/greedy-algorithms-set-6-dijkstras-shortest-path-algorithm/) for every vertex, considering every vertex as the source, we can find all pair shortest paths in O(V\*VLogV) time. 

So using Dijkstra’s single-source shortest path seems to be a better option than Floyd Warshall’s Algorithm([https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/?ref=lbp](https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/?ref=lbp)) , but the problem with Dijkstra’s algorithm is, that it doesn’t work for negative weight edge. __The idea of Johnson’s algorithm is to re-weight all edges and make them all positive, then apply Dijkstra’s algorithm for every vertex.__ 

****How to transform a given graph into a graph with all non-negative weight edges?**** 

One may think of a simple approach of finding the minimum weight edge and adding this weight to all edges. Unfortunately, this doesn’t work as there may be a different number of edges in different paths (See [this](https://www.geeksforgeeks.org/data-structures-graph-question-31/) for an example). If there are multiple paths from a vertex u to v, then all paths must be increased by the same amount, so that the shortest path remains the shortest in the transformed graph. The idea of Johnson’s algorithm is to assign a weight to every vertex. Let the weight assigned to vertex u be h\[u\]. 

We reweight edges using vertex weights. For example, for an edge (u, v) of weight w(u, v), the new weight becomes w(u, v) + h\[u\] – h\[v\]. The great thing about this reweighting is, that all set of paths between any two vertices is increased by the same amount and all negative weights become non-negative. Consider any path between two vertices s and t, the weight of every path is increased by h\[s\] – h\[t\], and all h\[\] values of vertices on the path from s to t cancel each other. 

How do we calculate h\[\] values? 

[Bellman-Ford algorithm](https://www.geeksforgeeks.org/dynamic-programming-set-23-bellman-ford-algorithm/) is used for this purpose. Following is the complete algorithm. A new vertex is added to the graph and connected to all existing vertices. The shortest distance values from the new vertex to all existing vertices are h\[\] values. 

> ****Algorithm:**** 
> 
> 1.  Let the given graph be G. Add a new vertex s to the graph, add edges from the new vertex to all vertices of G. Let the modified graph be G’. 
> 2.  Run the [Bellman-Ford algorithm](https://www.geeksforgeeks.org/dynamic-programming-set-23-bellman-ford-algorithm/) on G’ with s as the source. Let the distances calculated by Bellman-Ford be h\[0\], h\[1\], .. h\[V-1\]. If we find a negative weight cycle, then return. Note that the negative weight cycle cannot be created by new vertex s as there is no edge to s. All edges are from s. 
> 3.  Reweight the edges of the original graph. For each edge (u, v), assign the new weight as “original weight + h\[u\] – h\[v\]”. 
> 4.  Remove the added vertex s and run [Dijkstra’s algorithm](https://www.geeksforgeeks.org/greedy-algorithms-set-6-dijkstras-shortest-path-algorithm/) for every vertex. 

****How does the transformation ensure nonnegative weight edges?**** 

The following property is always true about h\[\] values as they are the shortest distances.

```
<span>   h[v] &lt;= h[u] + w(u, v) </span><br>
```

The property simply means that the shortest distance from s to v must be smaller than or equal to the shortest distance from s to u plus the weight of the edge (u, v). The new weights are w(u, v) + h\[u\] – h\[v\]. The value of the new weights must be greater than or equal to zero because of the inequality “h\[v\] <= h\[u\] + w(u, v)”. 

****Example:**** Let us consider the following graph. 

![Johnson1](https://media.geeksforgeeks.org/wp-content/cdn-uploads/Johnson1.png)

 We add a source s and add edges from s to all vertices of the original graph. In the following diagram s is 4. 

![Johnson2](https://media.geeksforgeeks.org/wp-content/cdn-uploads/Johnson2.png) 

We calculate the shortest distances from 4 to all other vertices using Bellman-Ford algorithm. The shortest distances from 4 to 0, 1, 2 and 3 are 0, -5, -1 and 0 respectively, i.e., h\[\] = {0, -5, -1, 0}. Once we get these distances, we remove the source vertex 4 and reweight the edges using following formula. w(u, v) = w(u, v) + h\[u\] – h\[v\].

 ![Johnson3](https://media.geeksforgeeks.org/wp-content/cdn-uploads/Johnson3.png) 

Since all weights are positive now, we can run Dijkstra’s shortest path algorithm for every vertex as the source. 

-   C++
-   Java
-   Python3
-   C#
-   Javascript

`#include <bits/stdc++.h>`

`#define INF 99999`

`using` `namespace` `std;`

`#define V 4`

`int` `minDistance(``int` `dist[],` `bool` `sptSet[])`

`{`

    `int` `min = INT_MAX, min_index;`

    `for` `(``int` `v = 0; v < V; v++)`

        `if` `(sptSet[v] ==` `false` `&& dist[v] <= min)`

            `min = dist[v], min_index = v;`

    `return` `min_index;`

`}`

`void` `printSolution(``int` `dist[][V])`

`{`

    `printf``(``"Following matrix shows the shortest distances"`

           `" between every pair of vertices \n"``);`

    `for` `(``int` `i = 0; i < V; i++) {`

        `for` `(``int` `j = 0; j < V; j++) {`

            `if` `(dist[i][j] == INF)`

                `printf``(``"%7s"``,` `"INF"``);`

            `else`

                `printf``(``"%7d"``, dist[i][j]);`

        `}`

        `printf``(``"\n"``);`

    `}`

`}`

`void` `floydWarshall(``int` `graph[][V])`

`{`

    `int` `dist[V][V], i, j, k;`

    `for` `(i = 0; i < V; i++)`

        `for` `(j = 0; j < V; j++)`

            `dist[i][j] = graph[i][j];`

    `for` `(k = 0; k < V; k++) {`

        `for` `(i = 0; i < V; i++) {`

            `for` `(j = 0; j < V; j++) {`

                `if` `(dist[i][k] + dist[k][j] < dist[i][j])`

                    `dist[i][j] = dist[i][k] + dist[k][j];`

            `}`

        `}`

    `}`

    `printSolution(dist);`

`}`

`int` `main()`

`{`

    `int` `graph[V][V] = { { 0, 5, INF, 10 },`

                        `{ INF, 0, 3, INF },`

                        `{ INF, INF, 0, 1 },`

                        `{ INF, INF, INF, 0 } };`

    `floydWarshall(graph);`

    `return` `0;`

`}`

**Output**

```
Following matrix shows the shortest distances between every pair of vertices 
      0      5      8      9
    INF      0      3      4
    INF    INF      0      1
    INF    INF    INF      0
```

****Time Complexity:**** The main steps in the algorithm are Bellman-Ford Algorithm called once and Dijkstra called V times. Time complexity of Bellman Ford is O(VE) and time complexity of Dijkstra is O(VLogV). So overall time complexity is O(V<sup><span>2</span></sup>log V + VE). 

The time complexity of Johnson’s algorithm becomes the same as Floyd Warshall’s Algorithm ([https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/?ref=lbp](https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/?ref=lbp))

when the graph is complete (For a complete graph E = O(V<sup><span>2</span></sup>). But for sparse graphs, the algorithm performs much better than Floyd Warshall’s Algorithm( [https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/?ref=lbp](https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/?ref=lbp) ). 

****Auxiliary Space:**** O(V<sup><span>2</span></sup>)

Are you looking to bridge the gap from **Data Structures and Algorithms (DSA) to Software Development**? Dive into our [**DSA to Development - Beginner to Advance Course**](https://gfgcdn.com/tu/Q8V/) on GeeksforGeeks, crafted for aspiring developers and seasoned programmers alike. Explore essential coding skills, software engineering principles, and practical application techniques through hands-on **projects** and real-world examples. Whether you're starting your journey or aiming to refine your skills, this course empowers you to build robust software solutions. Ready to advance your programming prowess? Enroll now and transform your coding capabilities!