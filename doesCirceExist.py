# def  doesCircleExists(commands):
#     res = []
#     for command in commands:
#         direction = 1
#         position = [0,0]
#         for i in xrange(4):
#             for instruction in command:
#                 if instruction == 'G':
#                     if direction == 1: position[0] += 1
#                     elif direction == 2: position[1] += 1
#                     elif direction == 3: position[0] -= 1
#                     elif direction == 4: postion[1] -= 1
#                 if instruction == 'L':
#                     direction += 1
#                     direction = direction % 4
#                 if instruction == 'R':
#                     direction -= 1
#                     direction = direction % 4
#                     print("New dir: " + str(direction))
#         print("dir: " + str(direction))
#         print("pos: " + str(position))
#         if position[0] == 0 and position[1] == 0 and direction == 1:
#             res.append("YES")
#         else:
#             res.append("NO")
#     return res


def main():
    commands = ["RR"]
    res = doesCircleExists(commands)
    print(res)



def  doesCircleExists(commands):
    res = []
    for command in commands:
        direction = 0
        position = [0,0]
        angle={0:[1,0],90:[0,1],180:[-1,0],270:[0,-1],360:[1,0],-90:[0,-1],-180:[-1,0],-270:[0,1]}
        for i in xrange(4):
            for instruction in command:
                if instruction == 'L': direction += 90
                if instruction == 'R': direction -= 90
                if instruction == 'G':
                    position[0] += angle[direction][0]
                    position[1] += angle[direction][1]       
                if direction == -360 or direction == 360:
                    direction = 0
                    
        if position == [0, 0]:
            res.append("YES")
        else:
            res.append("NO")
    return res

if __name__ == '__main__':
	main()