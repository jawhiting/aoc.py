def is_triangle(tri):
    x = sorted(tri)
    return (x[0] + x[1]) > x[2]

x = open("day3.txt")
lines = x.readlines()

triangles = [ ([int(i) for i in x.split()]) for x in lines]

print(triangles)

valid = [x for x in triangles if is_triangle(x)]

print(len(valid))

valid = []
# Now, flip them round
for i in range(0, len(triangles), 3):
    # This gives us 3 triangles
    for c in range(0, 3):
        tri = (triangles[i][c], triangles[i+1][c], triangles[i+2][c])
        if is_triangle(tri):
            valid.append(tri)

print(valid)
print(len(valid))