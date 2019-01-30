
def dfs(G,i):						#G is the graph and i is the node we want to start the search from
    n=len(G)						#all nodes
	visited = [False]*n				#nothing has been visited when this method is invoked.. therefore the entire G is FALSE(not visited)
    dfs_visit(G, i, visited)		#call method to pay i a visit and then its neighbors and so on
    return visited

def dfs_visit(G, i, visited):				#visits all nodes in a dfs manner. DFS involves BACKTRACKING!
    #print(i)
    visited[i]=True							#mark the first node as visited
    for j in range(len(G)):					#iterate through nodes
        if G[i][j]==1 and not visited[j]:	#if i has j as its neighbor and j has not been visited
            dfs_visit(G, j, visited)		#then j becomes i and called recursively. 

# Boolean function, determines whether a gragh G is a tree
# a graph G is a tree if (a) G is connected and (b) G has n-1 edges
def is_tree(G):
    return connected(G) and edge_count(G)

# call DFS to determine whether graph G is connected, 
# i.e., whether every node in G is visited during DFS
def connected(G):
    visited = dfs(G,0)					#start at the first node and see if all nodes have been visited. Then it meets first condition of connected Graph
    return len(set(visited))==1			#all nodes have been visited (TRUE)    

# a tree with n nodes should have n-1 edges
def edge_count(G):
    count = 0        
    for i in range(len(G)):
        for j in range(len(G)):
            count += G[i][j]
    return count == 2*(len(G)-1)


G = [[0,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]]  #a four-node star graph
print(is_tree(G))
