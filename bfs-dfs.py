def bfs(G,i):				#use of queue LIFO, i is the node
    active = [i]			#node that was passed in
    closed = []				#nodes that have been visited
    while active:			#while there is some node in the list that needs to visited
        i = active[0]		#take first node in active
        print(i)			#print it
        active, closed = active[1:], closed+[i]		#move the first one into visited
        for j in range(len(G)):
            if G[i][j] and j not in active+closed:
                active += [j]						#adding to list therefore queue

def dfs(G,i):				#use of stack FIFO
    active = [i]
    closed = []
    while active:
        i = active[0]
        print(i)
        active, closed = active[1:], closed+[i]
        for j in range(len(G)):
            if G[i][j] and j not in active+closed:
                active = [j]+active					#appending in front of list therefore stack 

G0 = [[0,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]]  #a four-node star graph
G = [[0,1,1,0,0,0,0],[1,0,0,1,1,0,0],[1,0,0,0,0,1,1],[0,1,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,1,0,0,0,0]]
bfs(G,0)
dfs(G,0)
