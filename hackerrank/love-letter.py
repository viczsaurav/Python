import sys
# Enter your code here. Read input from STDIN. Print output to STDOUT
fd = open("input.txt",'rU')
T=int(fd.readline())

while T>0:
    chrs=[]
    st = fd.readline().split("\n")[0]
    chrs.extend(st)
    i= len(chrs)-1
    j=0
    cnt=0
    while(i>j):      
        while(chrs[i] != chrs[j]):
            if (ord(chrs[i]) > ord(chrs[j])):
                chrs[i] = chr(ord(chrs[i])-1)
            else:
                chrs[j] = chr(ord(chrs[j])-1)
            cnt+=1
        i-=1
        j+=1
    print cnt
    T-=1