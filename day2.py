# 1
'''
f = open('day2input.txt', 'r', encoding='UTF-8')
code = f.read()
code = [int(x.strip()) for x in code.split(',')]

code[1] = 12
code[2] = 2
flag = 0
for index, num in enumerate(code):
    if flag == 0:
        if num == 1:
            code[code[index+3]] = code[code[index+1]] + code[code[index+2]]
            flag = 3
        elif num == 2:
            code[code[index+3]] = code[code[index+1]] * code[code[index+2]]
            flag = 3
        elif num == 99:
            print("job done")
            print(code[0])
            break
        else:
            continue
    else:
        flag = flag - 1

f.close()
'''

idealans = 19690720

def operation(noun, verb):
    f = open('day2input.txt', 'r', encoding='UTF-8')
    code = f.read()
    code = [int(x.strip()) for x in code.split(',')]

    code[1] = noun
    code[2] = verb
    flag = 0
    for index, num in enumerate(code):
        if flag == 0:
            if num == 1:
                code[code[index+3]] = code[code[index+1]] + code[code[index+2]]
                flag = 3
            elif num == 2:
                code[code[index+3]] = code[code[index+1]] * code[code[index+2]]
                flag = 3
            elif num == 99:
                return code[0]
                break
            else:
                continue
        else:
            flag = flag - 1
    f.close()

for i in range(100):
    for j in range(100):
        if operation(i, j) == idealans:
            print("succeeded")
            print(100*i + j)
