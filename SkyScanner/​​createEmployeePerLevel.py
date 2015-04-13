
def buildEmployeeHeap(emp1, emp2):
    if emp1 not in empList:
        empList[1], empList[2] = emp1, emp2
    else:
        if empList[2*empList.index(emp1)] is None: 
            empList[2*empList.index(emp1)] = emp2
        elif empList[2*empList.index(emp1)+1] is None: 
            empList[2*empList.index(emp1)+1] = emp2
        else: 
            print "Error"
    print empList

def printList():
    queue=[]
    queue.append(0)
    queue.append(-1)    # Sentinel divider
    while (len(queue)>0):
        node = queue.pop(0)
        if node != -1:
            if 2*node+1 >= len(empList): return
            if empList[2*node] is not None:
                print empList[2*node],
                queue.append(2*node)
            if empList[2*node+1] is not None:
                print empList[2*node+1],
                queue.append(2*node+1)
        else:
            print ""
            queue.append(-1)

fname = "emp.txt"
with open(fname) as f:
    N = int(f.readline())
    empList=[None]*(2*N+1)
    for line in f:
        emp1, emp2 = line.split(' ')[0].strip(), line.split(' ')[1].strip()
        buildEmployeeHeap(emp1,emp2)
    print empList
    printList()
f.close()

# buildEmployeeHeap('emp.txt')
# print "###########################"
# buildEmployeeHeap('emp1.txt')
# print "###########################"
# buildEmployeeHeap('emp2.txt')