# 1
f = open('day3input.txt', 'r', encoding='UTF-8')
lines = f.readlines()
routes = [[], []]
coordinates_one = []
coordinates_two = []
crosspoints = []

for i, path in enumerate(lines):
    routes[i] = path.rstrip('\n').split(",")

def move(pos, opcode, operand):
    poses = []
    for _ in range(operand):
        if opcode == "U":
            pos = [pos[0], pos[1] + 1]
        elif opcode == "D":
            pos = [pos[0], pos[1] - 1]
        elif opcode == "L":
            pos = [pos[0] - 1 , pos[1]]
        elif opcode == "R":
            pos = [pos[0] + 1 , pos[1]]
        poses.append(pos)
    return poses

for i in range(2):
    currentpos = [[0, 0]]
    for index, r in enumerate(routes[i]):
        currentpos = move(currentpos[-1], r[0], int(r[1:]))
        if i == 0:
            coordinates_one.extend(list(currentpos))
        if i == 1:
            for pos in currentpos:
                coordinates_two.append(pos)
                if pos in coordinates_one:
                    print("crossing at:", pos)
                    crosspoints.append(list(pos))

dists = []
for crosspoint in crosspoints:
    dists.append(abs(crosspoint[0]) + abs(crosspoint[1]))

print(min(dists))

# 2

print(coordinates_one)
print(coordinates_two)
steps = float('inf')
for crosspoint in crosspoints:
    temp = float(coordinates_one.index(crosspoint) + 1 + coordinates_two.index(crosspoint) + 1)
    if temp < steps:
        steps = temp
print(int(steps))
