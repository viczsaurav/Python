parent = dict()
rank = dict()
edgeList=[]

def initialize(vertex):
    parent[vertex] = vertex
    rank[vertex] = 0

def find(vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent[vertex])
    return parent[vertex]

def union(vertex1, vertex2):
    root1 = find(vertex1)
    root2 = find(vertex2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1

def minPath(graph):
    for vertex in graph['vertices']:
        initialize(vertex)
    mst = set()
    edges = list(graph['edges'])
    # print edges
    edges = sorted(edges,key=lambda x: x[2])
    # print 'new = ', edges
    for edge in edges:
        vertex1, vertex2, weight = edge
        if find(vertex1) != find(vertex2):
            union(vertex1, vertex2)
            mst.add(edge)
    return mst

def printMST(minTree):
	minTree = sorted(minTree,key=lambda x: x[2])
	count=0
	for i in xrange(len(minTree)):
		print int(minTree[i][0]), int(minTree[i][1]), minTree[i][2]
		count+= minTree[i][2]
	print count

fName = "path.txt"
with open(fName) as f:
	V = int(f.readline())
	vertices = [i for i in xrange(V)]
	E = int(f.readline())
	for path in f:
		edgeList.append(tuple(map(float,path.split(' '))))
f.close()

graph = dict()
graph['vertices'] = vertices
graph['edges'] = set(edgeList)

minTree = list(minPath(graph))
print printMST(minTree)

# edges = set([
#             (0.35,4,5),
# 			(0.37,4,7),
# 			(0.28,5,7),
# 			(0.16,0,7),
# 			(0.32,1,5),
# 			(0.38,0,4),
# 			(0.17,2,3),
# 			(0.19,1,7),
# 			(0.26,0,2),
# 			(0.36,1,2),
# 			(0.29,1,3),
# 			(0.34,2,7),
# 			(0.40,6,2),
# 			(0.52,3,6),
# 			(0.58,6,0),
# 			(0.93,6,4),
#             ])
# graph = {
#         'vertices': [0, 1, 2, 3, 4, 5,6,7],
#         'edges': set([
#             (0.35,4,5),
# 			(0.37,4,7),
# 			(0.28,5,7),
# 			(0.16,0,7),
# 			(0.32,1,5),
# 			(0.38,0,4),
# 			(0.17,2,3),
# 			(0.19,1,7),
# 			(0.26,0,2),
# 			(0.36,1,2),
# 			(0.29,1,3),
# 			(0.34,2,7),
# 			(0.40,6,2),
# 			(0.52,3,6),
# 			(0.58,6,0),
# 			(0.93,6,4),
#             ])
#         }
