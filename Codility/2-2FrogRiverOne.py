# https://codility.com/programmers/lessons/2 = Counting Elements

# Q2.2 FrogRiverOne 
# Find the earliest time when a frog can jump to the other side of a river. 

# Detected time complexity: O(N)

def solution(X, A):
    pos=[False]*X
    count=0; result=0
    for i in xrange(0,len(A)):
        if pos[A[i]-1] is False:
            pos[A[i]-1] = True
            count+=1
        if count==X:
            break
    if False not in pos:
            return i
    return -1
    
            

