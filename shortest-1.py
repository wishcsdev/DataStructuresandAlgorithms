#Djikstras Algo
#this prints the shortest distance from given node u to v
def shortest(G, u,v):
    MAX = 800									#arbritrary number that you know wont be reached by the nodes. 
    n = len(G)									#number of nodes
    D = [MAX]*n									#create infinity list which is basically the distance 
    D[u]=0										#distance of node is 0 therefore the program knows it is the starting node.
    Open = list(range(n))						#unvisited nodes
	predecessor=[-1]*n							#the node i came from 
	predecessor[u]=u
    while Open:    
        active = Open[0]						#first node in open is active
		if active == v: break					#if active is the target node then stop
        for i in Open:							#for each node in open 
            if D[i]<D[active]: 
				active = i						#if the distance of node i from u < distance of the active node from u, then active is changed to the new node i 
        for i in open:
			if G[active][i]==0:					#if active node and i are not connected because distance is 0 then continue 
				continue
			if D[active]+G[active][i] < D[i]:	#if distance of active from u plus distance of active and actives neighbor < distnace of i u's neighbor from u
				D[i]=D[active]+G[active][i]		#you go through this path because its shorter
				predecessor[i]=active			#the predecessor now becomes the active
			
		#for i in range(n):											# for each node in range
        #   if G[active][i]: 										#for active node and i are neighbors 
		#		D[i] = min(D[i],D[active]+G[active][i])	 			#distance of i is minimum of the values
        Open.remove(active)						
    return D, predecessor


G = [[0,1,1,0,0,0,0],[1,0,0,1,1,0,0],[1,0,0,0,0,1,1],[0,1,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,1,0,0,0,0]]
print(shortest(G,0,3))

# version 1, shortest path no frills
