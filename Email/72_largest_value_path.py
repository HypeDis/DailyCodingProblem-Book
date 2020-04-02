"""
In a directed graph, each node is assigned an uppercase letter. We define a path's value as the number of most frequently-occurring letter along that path. For example, if a path in the graph goes through "ABACA", the value of the path is 3, since there are 3 occurrences of 'A' on the path.

Given a graph with n nodes and m directed edges, return the largest value path of the graph. If the largest value is infinite, then return null.

The graph is represented with a string and an edge list. The i-th character represents the uppercase letter of the i-th node. Each tuple in the edge list (i, j) means there is a directed edge from the i-th node to the j-th node. Self-edges are possible, as well as multi-edges.

For example, the following input graph:

ABACA

[(0, 1),
 (0, 2),
 (2, 3),
 (3, 4)]

Would have maximum value 3 using the path of vertices [0, 2, 3, 4], (A, A, C, A).

The following input graph:

A

[(0, 0)]

Should return null, since we have an infinite loop.
"""


def largestPath(edgeList, nodes):
    # find the root nodes
    # traverse through the graph and count char frequencies
    # keep track of visited nodes
    adjList, rootNodes = analyzeList(edgeList)
    if not rootNodes:
        return None
    curMax = 0
    for root in rootNodes:
        curMax = max(curMax, helper(adjList, root, nodes, {}, {}, 0))
    return curMax


def helper(adjList, root, nodes, visited, freqList, curMax):
    if root in visited and visited[root]:
        return None
    visited[root] = True

    char = nodes[root]
    freqList[char] = freqList.get(char, 0) + 1
    curMax = max(freqList[char], curMax)

    if root not in adjList:
        return curMax

    for child in adjList[root]:
        curMax = max(curMax,
                     helper(adjList, child, nodes, visited, freqList, curMax))
    return curMax
    visited[root] = False


def analyzeList(eL):
    aL = {}
    dL = {}
    for pair in eL:
        frm = pair[0]
        to = pair[1]
        aL[frm] = aL.get(frm, [])
        aL[frm].append(to)
        dL[to] = dL.get(frm, [])
        dL[to].append(frm)
    roots = []
    for node in aL:
        if node not in dL:
            roots.append(node)
    return aL, roots


eL = [(0, 1), (0, 2), (2, 3), (3, 4)]
nL = 'ABACA'
print(largestPath(eL, nL))
eL2 = [(0, 0)]
nL2 = 'A'
print(largestPath(eL2, nL2))


# adjL = {
#     0:[1,2],
#     2:[3],
#     3:[4],
# }
# depList = {
#     0:[],
#     1:[0],
#     2:[0],
#     3:[2],
#     4:[4],
# }