def add(a, b):
    return a[0] + b[0], a[1] + b[1]


x = open("day2.txt")
lines = x.readlines()
print(lines)

keypad = ((0, 0, 0, 0, 0),
          (0, 1, 2, 3, 0),
          (0, 4, 5, 6, 0),
          (0, 7, 8, 9, 0),
          (0, 0, 0, 0, 0))
keypad2 = ((0,0,0,0,0,0,0),
           (0,0,0,1,0,0,0),
           (0,0,2,3,4,0,0),
           (0,5,6,7,8,9,0),
           (0,0,"A","B","C",0,0),
           (0,0,0,"D",0,0,0),
           (0,0,0,0,0,0,0))

keypad = keypad2

moves = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

# keypad[row][col]
pos = (2, 2)

result = []

for line in lines:
    for inst in line:
        newPos = add(pos, moves.get(inst, (0,0)))
        if keypad[newPos[0]][newPos[1]] != 0:
            print("Current pos {} instruction {} moving to {}".format(pos, inst, newPos))
            pos = newPos
        else:
            print("Current pos {} instruction {} not moving".format(pos, inst))
    # next line
    print("end of line. Pos is {} value is {}".format(pos, keypad[pos[0]][pos[1]]))
    result.append(keypad[pos[0]][pos[1]])

print("Code is {}".format(result))