#  https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/

'''
```md
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
```
'''

'''
The Idea:
Dijkstra’s Algorithm using Adjacency Matrix:
(Adjacency matrix means we init the algorithm with a graph matrix of VxV for V vertices with each [i][j] containing distance from ith to jth vertex)
The idea is to generate a SPT (shortest path tree) with a given source as a root. 
Maintain an Adjacency Matrix with two sets,
- one set contains vertices included in the shortest-path tree,
- other set includes vertices not yet included in the shortest-path tree.
At every step of the algorithm, find a vertex that is in the other set (set not yet included) and has a minimum distance from the source.
'''

'''
Algorithm :

Create a set sptSet (shortest path tree set) that keeps track of vertices included in the shortest path tree, i.e., whose minimum distance from the source is calculated and finalized. Initially, this set is empty.
Assign a distance value to all vertices in the input graph. Initialize all distance values as INFINITE . Assign the distance value as 0 for the source vertex so that it is picked first.
While sptSet doesn’t include all vertices
Pick a vertex u that is not there in sptSet and has a minimum distance value.
Include u to sptSet .
Then update the distance value of all adjacent vertices of u .
To update the distance values, iterate through all adjacent vertices.
For every adjacent vertex v, if the sum of the distance value of u (from source) and weight of edge u-v , is less than the distance value of v , then update the distance value of v .
Note: We use a boolean array sptSet[] to represent the set of vertices included in SPT . If a value sptSet[v] is true, then vertex v is included in SPT , otherwise not. Array dist[] is used to store the shortest distance values of all vertices.
'''


# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph

# Library for INT_MAX




import sys
class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):

        # Initialize minimum distance for next node
        min = sys.maxsize

        # Search not nearest vertex not in the
        # shortest path tree
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u

        return min_index

    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # x is always equal to src in first iteration
            x = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[x] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and \
                        dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]

        self.printSolution(dist)


# Driver's code
if __name__ == "__main__":
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]

    g.dijkstra(0)

# This code is contributed by Divyanshu Mehta and Updated by Pranav Singh Sambyal
