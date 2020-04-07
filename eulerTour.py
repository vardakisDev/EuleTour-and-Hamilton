

# import networkx as nx
# import numpy as np
# import matplotlib.pyplot as plt

# # G = nx.complete_graph(9)
# # nx.draw_networkx(G)
# # plt.show()

# # x =nx.eulerian_path(G,source=0)
# print(list(x))
# n = getinput()
# G = nx.complete_graph(n)
# A = nx.to_numpy_matrix(G)
# print(A)


#---------------------------------------#
# https://algorithmist.com/wiki/Euler_tour
# This algorithm is based on the following observation: if C is any cycle in a Eulerian graph,
# then after removing the edges of C, the remaining connected components will also be Eulerian graphs.
# The algorithm consists in finding a cycle in the graph, removing its edges and repeating this steps with each remaining connected component.
# It has a very compact code with recursion:

def getinput():
    x = int(input("Give the n: "))

    return x


def IsEulerian(n):
    if n % 2 == 1:
        return True
    else:
        return False


def visit(current):
    for x in range(n):
        if g[current][x] > 0:
            g[current][x] -= 1
            g[x][current] -= 1
            visit(x)
    circuit.append(current)


# max input is 43 .. n > 43 gives recursion erroor FIX !
n = getinput()
if IsEulerian(n) == False:
    print('No path')
else:
    g = [[0 if i == j else 1 for j in range(n)]for i in range(n)]
    circuit = []
    visit(0)
    circuit.reverse()
    circuit = [x+1 for x in circuit]
    print(circuit)
