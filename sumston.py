# Complexity on this should be O(n log n) with a tree worst case
# This a List * Hash it could be O(2n) or rather O(n) best case
# This is a FIRST PASS, but I won't admit its known weaknesses, ever.
def sumston (A, B, N):
    for x in A:
        if (N - x) in B: output_triple(x, (N - x), N) 
            

def output_triple(x, y, N):
    data_hash = {"x": str(x), "y": str(y), "N": str(N)}
    output_template = "{x} + {y} = {N}"
    output = output_template.format(**data_hash)
    print(output)

# ***  T E S T S  *****************************************************
if __name__ == "__main__":
    print("________________________________________________________________________")
    print("First pass with A, B, and X")
    A = [6, 5, 4]
    B = [1, 2, 3]
    X = 7
    print(" ".join(str(x) for x in A))
    print(" ".join(str(x) for x in B))
    print(X)
    sumston(A, B, X)

    print("________________________________________________________________________")
    print("First pass with C, D, and Y")
    C = [0, 0, 0]
    D = [0, 0, 0]
    Y = 7
    print(" ".join(str(x) for x in C))
    print(" ".join(str(x) for x in D))
    print(Y)
    sumston(C, D, Y)

    print("________________________________________________________________________")
    print("First pass with E, F, and Z")
    F = [0, 6, 0]
    E = [3, 3, 3]
    Z = 9
    print(" ".join(str(x) for x in E))
    print(" ".join(str(x) for x in F))
    print(Z)
    sumston(E, F, Z)

