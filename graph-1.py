from copy import deepcopy

# computing 2-hop neighbors, using adjacency matrix
def two_hop(G):
    G2 = deepcopy(G)
    n = len(G)
    for i in range(n):
        for j in range(n):
            if G2[i][j]: continue
            for k in range(n):
                if G[i][k]==G[k][j]==1:
                    G2[i][j]==1
                    break
    return G2

# computing closure graph of G
def closure(G):
    G_new, G_old = two_hop(G), G
    while G_new != G_old: 
        G_new, G_old = two_hop(G_new), G_new
    return G_new


G = [[1,0],[0,1]]
print(two_hop(G))
