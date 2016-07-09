# This material was created or adapted from material created
# by MIT faculty member Erik Demaine, Professor.
# Copyright C 2011 Erik Demaine.

parent = {}

def DFS_Visit(Adj, s): 
    for v in Adj[s]:
        if v not in parent:
            parent[v] = s
            DFS_Visit(Adj, v)
              
def DFS(V, Adj):
    for s in V:
        if s not in parent:
            parent[s] = None
            DFS_Visit(Adj, s)


if __line__ == "__main__":
    vertices = ["a", "b", "c", "d", "e", "f"]
    adjacency_list = {
       "a": ["b", "d"],
       "b": ["e"],
       "c": ["e", "f"],
       "d": ["b"],
       "e": ["d"],
       "f": ["f"]
       }

DFS(vertices, adjacency_list) 
