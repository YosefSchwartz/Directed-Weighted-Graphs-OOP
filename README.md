# Exam 3 - Directed weighted graph, OOP course. 
***Authors:** Eden Shkuri & Yosef Schwartz*  
***Program language:** Python 3.9*

### Main information
In this project we create three classes to implement directed weighted graph principals and their main algorithms.
you can build graph, add and remove node or edge, get list of all edges that start in specific node, or the specific node is the destination, and more.

furthermore, this project allow you to calculate some data on graphs, save to JSON format or load from JSON format and plot the graph on screnn by your position, and if none, by randominal position.
For example:
1. `connected_component(id)` - This function return a list of Strongly Connected Component (SCC) that this node (by id) included.  
2. `shortest_path(id1, id2)` - This function calculate the shoretest path by weight from id1 node to id2 node, and return a pair of the distant and the path in list, remmember!, the shortest path may include more nodes from another path, but this path had lower weight by total.
3. `load_from_json(file_name)` - This function get string that represent a path to file in JSON format, and start to build new graph by his data.  
  
  and more

#### Known algorithms
***dijkstra algorithm*** - This algorithm scan all graph from start node, and for each node fill the distance, and infinity if none.  
Read more - https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

***DFS algorithm*** - This algorithm read the graph node by node for the deapth, we choose implements this iterativly.  
NOTE: in our project, were we find SCC we use this algorithm, and then we use almost same algorithm (`DFS_Opp(id)`), this replace the need of graph transpose.
Read more - https://en.wikipedia.org/wiki/Depth-first_search

#### Tests:  
Our tests focus on corrects of algorithms and function, and on time that take to each function.  
We use the default `UnitTesting` class.

##### System required  
Pythons 3.0 and more
