# Directed weighted graph
***Authors:** Eden Shkuri & Yosef Schwartz*  
***Program language:** Python 3.9*

### Main information
In this project we have created three classes to implement directed weighted graph principals and their main algorithms.
with this project you can build a graph, add and remove node or edge, get list of all edges that start in a specific node, or ends in this node, and more.

furthermore, this project allow you to calculate some data on graphs, save to JSON format or load from JSON format and plot the graph on screen with your positions or with random positions.  
For example:
1. `connected_component(id)` - This function return a list of Strongly Connected Component (SCC) that this node (by id) associated to.  
2. `shortest_path(id1, id2)` - This function calculate the shoretest path by weight from id1 node to id2 node, and return a tuple of the distance and the path in a list, 
3. `load_from_json(file_name)` - This function get a string that represent a path to file in JSON format, and start to build new graph with it's data.  
  
  
### Known algorithms
***dijkstra's algorithm*** - This algorithm scan all graph from start node, and for each node fill his distance from the src node, infinity if none.  
Read more - https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

***DFS algorithm*** - This algorithm read the graph node by node for the deapth, we choose to implement it in iterativly way.  
NOTE: in our project, were we find SCC we use this algorithm, and then we use almost same algorithm (`DFS_Opp(id)`) (replace the need of a transpose graph).
Read more - https://en.wikipedia.org/wiki/Depth-first_search

#### Tests:  
Our tests focus on correctness of algorithms and function, and on time that take for the algorithms on big graphs.  
We use the default `UnitTesting` class.

##### System required  
Pythons 3.0 at least
  
 
#### Plot graph examples:

<img src="https://user-images.githubusercontent.com/73064850/104216694-106c3100-5443-11eb-8bf1-ad6f30a189dc.jpg" width="600" height="350"> 

  
 <img src="https://user-images.githubusercontent.com/73064850/104215863-0ac21b80-5442-11eb-890c-4a6352fd8daf.jpg" width="600" height="350"> 

