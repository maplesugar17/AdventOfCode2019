# 1
import collections
input = "147981-691423"
start = int(input.split("-")[0])
end = int(input.split("-")[1])
sameadjacent = False
count = 0
current = start
possiblepw = []

while current <= end:
    digitlist = list(map(int, str(current)))
    # print(digitlist)
    for i in range(0, len(digitlist)+2):
        if i >= len(digitlist) - 1:
            # print("   最後の桁です")
            if sameadjacent:
                # print("   パスワードっぽいよ")
                count = count + 1
                sameadjacent = False
                possiblepw.append(current)
                current += 1
                break
            else:
                sameadjacent = False
                current += 1
        else:
            # print("   比較します:", digitlist[i],"と",digitlist[i+1])
            if digitlist[i] > digitlist[i+1]:
                # print("   減ってるよ")
                a = 10**(len(digitlist)-i-2)
                b = (digitlist[i]-digitlist[i+1])
                current += (10**(len(digitlist)-i-2)*(digitlist[i]-digitlist[i+1]))
                break
            if digitlist[i] == digitlist[i+1]:
                # print("   同じだよ")
                sameadjacent = True
# print(count)

#2
import collections

a = 0
for pw in possiblepw:
    digits = [int(num) for num in str(pw)]
    # print("数は:", digits)
    c = collections.Counter(digits)
    # print("   count:", c)
    mode = c.most_common()[0][0]
    if len(c) == 1:
        continue
    if c.most_common()[0][1] == 2:
        # print("   要素は２個ずつです")
        a += 1
        continue
    elif c.most_common()[0][0] < c.most_common()[1][0] and c.most_common()[0][1] != c.most_common()[1][1] != 1:
        # print("   最頻値よりも大きい数のかぶりがいるよ", digits)
        a += 1
        continue
    else:
        print("あてはまらないよ",digits)


print(a)
