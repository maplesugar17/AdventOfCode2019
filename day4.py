# 1
input = "147981-691423"
start = int(input.split("-")[0])
end = int(input.split("-")[1])
sameadjacent = False
count = 0
current = start
possiblepw = []
while current <= end:
    digitlist = list(map(int, str(current)))
    for i in range(0, len(digitlist)+2):
        if i >= len(digitlist) - 1:
            if sameadjacent:
                count = count + 1
                sameadjacent = False
                current += 1
                possiblepw.append(current)
                break
            else:
                sameadjacent = False
                current += 1
        else:
            if digitlist[i] > digitlist[i+1]:
                a = 10**(len(digitlist)-i-2)
                b = (digitlist[i]-digitlist[i+1])
                current += (10**(len(digitlist)-i-2)*(digitlist[i]-digitlist[i+1]))
                break
            if digitlist[i] == digitlist[i+1]:
                sameadjacent = True
print(count)

#2
import numpy.np

possiblepw_np = np.array(possiblepw)
