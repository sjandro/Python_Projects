import sys

def checkK(index, k):
    if index == k:
        return True
    else:
        return False
    
def  maxStep(n, k):
    step = 0
    for i in xrange(1,n+1):
        if checkK(step+i, k):
            continue
        else:
            step += i

            
    return step

print("Max Step: "+str(maxStep(int(sys.argv[1]),int(sys.argv[2]))))