# This material was created or adapted from material created
# by MIT faculty member Erik Demaine, Professor.
# Copyright C 2011 Erik Demaine.
# MIT License assumed, Modified 2016 Brig Young, github/Sonophoto
parent = {}
level = {}
 
def BFS(s, Adj):
    level[s] = 0
    parent[s] = None
    i = 1
    frontier = [s] # level i - 1
    while frontier:
        next = [] # level i
        for u in frontier:
            for v in Adj[u]: # edge from u to v
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
                print("Current Vertex: ", v, "  Current Frontier: ", frontier, "  Adjacency@Vertex: ", Adj[v])
        frontier = next
        i += 1

if __name__ == "__main__":
    vertices = ["s", "a", "c", "d", "f", "z", "x", "v"]
    adjacency_list = {
        "a": ["s", "z"],
        "z": ["a"],
        "s": ["a", "x"],
        "x": ["s", "d", "c"],
        "d": ["x", "c", "f"],
        "c": ["x", "d", "f", "v"],
        "f": ["d", "c", "v"],
        "v": ["c", "f"]
        }

    print("\n**********  B R E A D T H   F I R S T   S E A R C H  ************************\n")
    print("Vertices: ", vertices)
    print("Adjacency Lists: ", adjacency_list)
    print("")
    BFS("s", adjacency_list) 
