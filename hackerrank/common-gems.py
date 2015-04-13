import sys
# Enter your code here. Read input from STDIN. Print output to STDOUT
fd = open("input.txt",'rU')
T=int(fd.readline())
offset = 97
chrs=[False]*26
mystring = fd.readline().split("\n")[0]
print mystring
for c in mystring:
    chrs[ord(c)-offset] = True
while T>1:
    newstring  = fd.readline().split("\n")[0]
    for i in xrange(26):
        # print (chrs[i] and chr(i+offset) not in newstring)
        if(chrs[i] and chr(i+offset) not in newstring):
            chrs[i] = False
    T-=1
count=0
for j in (i for i in chrs if i):
    count+=1
print count
