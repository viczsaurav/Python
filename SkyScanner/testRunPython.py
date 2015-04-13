import sys

def checkPalindrome(line):
    i=0;j=len(line.strip(' '))-1
    while(j>i):
        if line[i]!= line[j]:
            if line[i+1]!= line[j]:
            	print "here"
                return j
            if line[i]!= line[j-1]:
                print "i = ", line[i-2],line[i-1], line[i], line[i+1],line[i+2]
                print "j= ", line[j-2],line[j-1],line[j],line[j+1], line[j+2]
                return i

        i+=1;j-=1
    return -1

with open('palindromeIndex.in') as f:
	N = int(f.readline())
	for line in f:
		N-=1
		print checkPalindrome(line.strip('\n'))