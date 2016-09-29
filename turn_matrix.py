# you have a 2 dimentional matrix square, like below
#     0     1     2
#     3     4     5
#     6     7     8

# It is required to fill the code in "turn_array(param) " method in order to rotate the matrix number of shifts clockwise.
# Here are some examples
# for 0 shifts
#     0     1     2
#     3     4     5
#     6     7     8

# for 1 shift
#     3     0     1
#     6     4     2
#     7     8     5

# for 2 shift2
#     6     3     0
#     7     4     1
#     8     5     2


# The matrix WILL BE square , i.e. height = width
# Matrix width > 2

###### WHAT ARE WE LOOKING FOR
# to see your ability to :
# 1) write readable clean code
# 2) problem solving using (if/else/loops/etc ... )
# 3) arrays and data structures

# the "main" function is provided to get you started.

# Please modify this method
def turn_array(param , shifts):
    matrix = [[0 for i in range(len(param))] for i in range(len(param))]
    params_length = len(param)
    x = 0
    y = 0
    start = 0
    end = len(param) - 1
    while params_length > 0:
        size = 1 if params_length == 1 else params_length * 4 - 4
        params_length -= 2
        outer_layer = build_squence(param, x, y, start, end, size)
        matrix = build_matrix(matrix,shift_squence(outer_layer, (shifts * -1)),x,y,start,end)
        x += 1
        y += 1
        start += 1
        end -= 1

    return matrix

def build_squence(matrix, x, y, start, end, parameter):
    squence = []
    for i in range(parameter):
        squence.append(matrix[x][y])
        if x == start and y < end: y += 1
        elif y == end and x < end: x += 1
        elif x == end and y > start: y -= 1
        elif x > start and y == start: x -= 1
    return squence

def shift_squence(squence, n):
    n = n % len(squence)
    return squence[n:] + squence[:n]

def build_matrix(matrix, lst, x, y, start, end):
    for val in lst:
        matrix[x][y] = val
        if x == start and y < end: y += 1
        elif y == end and x < end: x += 1
        elif x == end and y > start: y -= 1
        elif x > start and y == start: x -= 1
    return matrix

# Everything below is a helper code, you can ignore it.
#
#

def print_matrix(param):
    for row in param:
        for val in row:
            print('{:5}'.format(val), end='')
        print()

    return


def main():
    width = 20
    matrix = [[(x + width*y)for x in range(width)] for y in range(width)]

    print_matrix(turn_array(matrix, 0))


if __name__ == '__main__':
    main()
