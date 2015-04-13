def  minArea( x,  y,  k):
    if(k==1):
        return 1
    lower=0
    higher=0

    minX = sorted(x)[0]
    maxX= sorted(x)[len(x)-(k+1)]
    minY = sorted(y)[0]
    maxY= sorted(y)[len(y)-(k+1)]
    
    if(minX<minY):
        lower=[minX,y[x.index(minX)]]
    else:
        lower=[minY,x[y.index(minY)]]
    if(maxX>maxY):
        higher=[maxX,y[x.index(maxX)]]
    else:
        higher=[maxY,x[y.index(maxY)]]

    if(lower[0]<=lower[1]):
        minVal=lower[0]-1
    else:
        minVal=lower[1]-1
    if(higher[0]>=higher[1]):
        maxVal=higher[0]+1
    else:
        maxVal=higher[1]+1
    area = (maxVal-minVal)*(maxVal-minVal)
    return area