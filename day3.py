# 1
f = open('day3input.txt', 'r', encoding='UTF-8')
lines = f.readlines()
routes = [[], []]
coordinates = []
crosspoints = []

for i, path in enumerate(lines):
    routes[i] = path.rstrip('\n').split(",")

def move(pos, opcode, operand):
    poses = []
    for _ in range(operand):
        if opcode == "U":
            pos[1] = pos[1] + 1
        elif opcode == "D":
            pos[1] = pos[1] - 1
        elif opcode == "L":
            pos[0] = pos[0] - 1
        elif opcode == "R":
            pos[0] = pos[0] + 1
        poses.append(list(pos))
    return poses

for i in range(2):
    currentpos = [[0, 0]]
    for index, r in enumerate(routes[i]):
        currentpos = move(currentpos[-1], r[0], int(r[1:]))
        if i == 0:
            coordinates.extend(list(currentpos))
        if i == 1:
            for pos in currentpos:
                if pos in coordinates:
                    print("crossing at:", pos)
                    crosspoints.append(list(pos))

dists = []
for crosspoint in crosspoints:
    dists.append(abs(crosspoint[0]) + abs(crosspoint[1]))

print(min(dists))
