def sumOfPowerOf2(N):
    i=1
    sum=0	# Not considering power of 0
    while N>0:
        i = i<<1
        sum+=i
        N-=1
    return sum

# input = raw_input("Enter power of 2 = ")
input = 5
print "Sum = ",sumOfPowerOf2(int(input))