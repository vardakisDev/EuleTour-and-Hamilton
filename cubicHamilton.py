# Hamiltonian Paths and Cycles
# A Hamiltonian path in an undirected graph G = (V,E) is a path that goes through every vertex exactly once.
# A Hamiltonian cycle (or Hamiltonian tour) is a cycle that goes through every vertex exactly once. Note that,
# in a graph with n vertices, a Hamiltonian path consists of n−1 edges, and a Hamiltonian cycle consists of n
# edges.
# Theorem: For every n ≥ 2, the n-dimensional hypercube has a Hamiltonian cycle.
# Proof: By induction on n. In the base case, n = 2, the 2-dimensional hypercube, the cycle starts at 00, goes
# through 01, 11, and 10, and returns to 00.
# Suppose now that every (n − 1)-dimensional hypercube has a Hamiltonian cycle. Let v ∈ {0,1}
# n−1 be a
# vertex adjacent to 0
# n−1
# (the notation 0
# n−1 means a sequence of n−1 zeroes) in the Hamiltonian cycle in an
# (n−1)-dimensional hypercube. The following is a Hamiltonian cycle in an n-dimensional hypercube: have
# a path that goes from 0
# n
# to 0v by passing through all vertices of the form 0x (this is simply a copy of the
# Hamiltonian path in dimension (n−1), minus the edge from v to 0
# n−1
# ), then an edge from 0v to 1v, then a
# path from 1v to 10n−1
# that passes through all vertices of the form 1x, and finally an edge from 10n−1
# to 0
# n
# .
# This completes the proof of the Theorem.
# When we start from 0
# n
# and we follow the Hamiltonian cycle described in the above proof, we find an
# ordering of all the n-bit binary strings such that each string in the sequence differs from the previous string
# in only one bit. Such an ordering is called a Gray code (from the name of the inventor) and it has various
# applications in error correction schemes and other fields. You can read about some of these in the wikipedia
# entry (en.wikipedia.org/wiki/Gray code), and you can find out a lot more about Gray codes in the survey
# paper by Carla Savage at www4.ncsu.edu/∼savage/AVAILABLE FOR MAILING/survey.ps

from sympy.combinatorics.graycode import GrayCode


def getinput():
    x = int(input("Give the n: "))

    return x


def IsCubicHamilton(n):
    if n > 1:
        print('There is a Hamilton cycly for the cubic Q', n, "graph")
        a = GrayCode(n)
        print(list(a.generate_gray()))
    else:
        print("There isn't a Hamilton path")


n = getinput()
IsCubicHamilton(n)
