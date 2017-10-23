

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
