# 1
f = open('day1input.txt', 'r', encoding='UTF-8')
datalist = f.readlines()
totalmass = 0
for data in datalist:
    totalmass = totalmass + (int(data)//3-2)

print(totalmass)
f.close()

# 2
f = open('day1input.txt', 'r', encoding='UTF-8')
datalist = f.readlines()
totalmass = 0
for data in datalist:
    mass = int(data)
    while True:
        mass = mass // 3 - 2
        if mass <= 0:
            break
        else:
            totalmass = totalmass + mass
print(totalmass)
f.close()
