import sys

def checkPalindrome(line):
    i=0;j=len(line.strip(' '))-1
    while(j>i):
        if line[i]!= line[j]:
            if line[i+1]!= line[j]:
                return j
            if line[i]!= line[j-1]:
                return i

        i+=1;j-=1
    return -1

with open('palindromeIndex.in') as f:
	N = int(f.readline())
	for line in f:
		N-=1
		print checkPalindrome(line.strip('\n'))