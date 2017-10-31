
if __name__ == "__main__":
    vertices = ["a", "b", "c", "d", "e", "f"]
    adjacency_list = {
       "a": ["b", "d"],
       "b": ["e"],
       "c": ["e", "f"],
       "d": ["b"],
       "e": ["d"],
       "f": ["f"]
       }

    print("\n**********  D E P T H   F I R S T   S E A R C H  ************************\n")
    print("Vertices: ", vertices)
    print("Adjacency Lists: ", adjacency_list)
    print("")
    DFS(vertices, adjacency_list) 
