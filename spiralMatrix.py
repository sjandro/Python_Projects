# n = int(raw_input().split(',')[0])
# matrix = ""
# for i in xrange(1, n + 1):
#     if matrix == "":
#         matrix = raw_input()
#     elif i % 2 == 0:
#         row = raw_input().split(',')
#         row.reverse()
#         #print row
#         matrix = matrix + "," + ",".join(row)
#     else:
#         matrix = matrix + "," + raw_input()

#     print matrix

import itertools

arr = [['0','1','2','3'],
       ['4','5','6','7'],
       ['8','9','10','11'],
       ['12','13','14','15']]

def shift(seq, n):
    n = n % len(seq)
    return seq[n:] + seq[:n]

def buildMatrix(matrix, lst, x, y, start, end):
    for num in lst:
        print "x: " + str(x) + " y: " + str(y) 
        matrix[x][y] = num
        if x == start and y < end:
            y += 1
        elif y == end and x < end:
            x += 1
        elif x == end and y > start:
            y -= 1
        elif x > start and y == start:
            x -= 1
    return matrix

def buildSquence(matrix, x, y, start, end, parameter):
    l = []
    for i in range(parameter):
        print "x: " + str(x) + " y: " + str(y) 
        l.append(matrix[x][y])
        if x == start and y < end:
            y += 1
        elif y == end and x < end:
            x += 1
        elif x == end and y > start:
            y -= 1
        elif x > start and y == start:
            x -= 1
    return l



def transpose_and_yield_top(arr):
#    count = 0
    while arr:
        # if(count == 4):
        #   break
        yield arr[0]
        #print arr[0]
        #count += 1
        l = list(zip(*arr[1:]))
        print l
        arr = list(reversed(l))

# def outerLayerSize(n):
#   if n == 1:
#       return 1
#   else:
#       return n * 4 - 4

# test = ",".join(list(itertools.chain(*transpose_and_yield_top(arr))))
# mlist = [list(i) for i in list(transpose_and_yield_top(arr))]
# final_sque = []
# for i in range(len(mlist)):
#   for j in range(len(mlist[i])):
#       final_sque.append(mlist[i][j])
# print final_sque

#spiral_matrix = list(itertools.chain(*transpose_and_yield_top(arr)))
#spiral_matrix = final_sque
matrix = [[0 for i in range(len(arr))] for i in range(len(arr))]

#layers = []
params_length = len(arr) 
#index = 0
x = 0
y = 0
start = 0
end = len(arr) - 1
while params_length > 0:
    #size = outerLayerSize(params_length)
    size = 1 if params_length == 1 else params_length * 4 - 4
    params_length -= 2
    print size
    #layers.append(spiral_matrix[index:size+index])
    layers = buildSquence(arr, x, y, start, end, size)
    print buildMatrix(matrix,shift(layers, -2),x,y,start,end)

    #index = size
    x += 1
    y += 1
    start += 1
    end -= 1
#print layers
# l = shift(test.split(","), -2)
# print l

# matrix = [[0 for i in range(len(arr))] for i in range(len(arr))]
# print matrix

# x = 0
# y = 0
# start = 0
# end = len(arr) - 1
# for i in range(len(layers)):
#   print buildMatrix(matrix,shift(layers[i], -2),x,y,start,end)
#   x += 1
#   y += 1
#   start += 1
#   end -= 1






