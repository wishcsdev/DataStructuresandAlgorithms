#PRIMS Algo
def mst(G,n):						#pass in matrix with weights and n is the number of vertices
    MST = {}						#create dump set that will have the final sequence of mst. use {} for sets
    open = list(range(1,n))			#nodes that have not been visited yet
    closed = [0]					#start with 0 node so put it into closed list  
    while open:											#iterate through open list until no set of vertices are left in the list
        flag = True										#is this the first node
        for (i,j) in G:									#iterate through all node sets in the graph
            if (i in open) == (j in open): continue		#if i and j are the same contained in the open list, then continue
            if flag or G[(i,j)]<G[(u,v)]: 				#if this is the first node or if WEIGHT of (i,j) < (u,v)
                u,v = i,j								#pick the smaller set and make them the new set
                flag = False							#no longer the first node
        MST[(u,v)] = G[(u,v)]							#now your MST set contains this set as a list []
        if u in open: 
			v = u										#if node u is in open list then make v=u
        open.remove(v)									#remove v node and add it to the closed because in the next iteration you will be starting with v 
        closed += [v]									# put it into the visited list
    return MST


G={(0,1):1,(0,3):3,(1,2):6,(1,3):5,(1,4):1,(2,5):2,(3,4):1,(4,5):4,(2,4):5}
print(mst(G,6))
