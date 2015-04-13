for j in [i*2 for i in xrange(5)]:
  print j
N=10

l = [i for i in xrange(N)]
verts = [[0 for x in range(3)] for y in range(2)]
print l
print verts
path=[]
fName = "path.txt"
with open(fName) as f:
  E = int(f.readline())
  N = int(f.readline())
  while N>0:
    line = f.readline(); N-=1
    path.append(tuple(map(float,line.split(' '))))
print set(path)
for i in xrange(len(path)):
  print int(path[i][0]), int(path[i][1]), path[i][2]
f.close()

edges = set([
      (0.35,4,5),
      (0.37,4,7),
      (0.28,5,7),
      (0.16,0,7),
      (0.32,1,5),
      (0.38,0,4),
      (0.17,2,3),
      (0.19,1,7),
      (0.26,0,2),
      (0.36,1,2),
      (0.29,1,3),
      (0.34,2,7),
      (0.40,6,2),
      (0.52,3,6),
      (0.58,6,0),
      (0.93,6,4),
            ])
edges = list(edges)
edges.sort()
print "Old ", edges

edges = sorted(edges,key=lambda x: x[2])
print "new", edges

l1 = [1,2,3,4,5]
d = dict()
d['vertices'] = l1
d['edges'] = edges

print d