# QUESTION 1

class current_node:
    def __init__(self, id):
        self.id = id
        self.neighbors = []

    def get_neighbors(self, neighbors):
        self.neighbors += neighbors

    def visit(self):
        print(self.id)

    def bfs(self):                                              #citation:http://interviewcat.com/2015/05/05/post-1-python-graphs-and-searching/
        bfs_list = []						#intialise list
        active = [self]						#current list that has not been put into bfs_list
        
	    
        while len(active) > 0:                                          #traverse through all current_nodes in active list
                    current_node = active[0]		                #start at first current_node indexed at 0
                    del active[0]					#delete the current_node from active because its been visited
            
                    if current_node.id not in bfs_list:                 #citation:https://codereview.stackexchange.com/questions/135156/bfs-implementation-in-python-3
                            current_node.visit()			#print the current node by calling visit method
                
                            for n in current_node.neighbors:	        #add the neighbors of the current node to active list	
                                active.append(n)                        #citation:https://stackoverflow.com/questions/46383493/python-implement-breadth-first-search
                            bfs_list.append(current_node.id)		#add the current node to the bfs list


a, b, c = current_node(0), current_node(1), current_node(2)
a.get_neighbors([b, c])
b.get_neighbors([c, a])
c.get_neighbors([a, b])
a.bfs()


#############################################################################################################################################################################

# QUESTION 2   returns 1-hop neighbors of node i

def get_N(graph, i):
	N = []									#empty list
	for (a,b) in graph:							#iteration for each edge 
		if i in (a,b): 							#check to see if i is an element
			N.append(a+b-i)			 			#delete i if it is an element
	return N									#return the list

	

	
# returns 2-hop neighbors of node i				#Citation: https://gist.github.com/anirudhjayaraman/272e920079fd8cea97f81487ef1e78a3
def get_NN(graph, i):						#1 hop neighbor of 1 hop neighbor is 2 hop neighbor
  TwohopN = []							#empty 2 hop neighbor list

  N = get_N(graph,i)						#get 1hop neighbor 

  for node in N:						#find the 1hop neighbor of 1hop neighbor by iterating through each neighbor of i node
								#Citation:https://gist.github.com/AdityaSoni19031997/11a510bc88abc948f2e4f7a642f36ea5
                nodeNeighbor=get_N(graph,node)                          #get neighbor of each i in TwohopN
                TwohopN.append(nodeNeighbor)				#add to the list 
  
  result=(set(sum(TwohopN,[])))					#create set to remove duplicates 

  result.remove(i)						#remove i since its a 1 hop neighbor
  
  return list(result)						#convert result set into list format


graph = {(3,0):1, (2,1):2, (4,3):3, (0,2):11, (1,3):2}
NN = get_NN(graph, 0)
print(NN)
