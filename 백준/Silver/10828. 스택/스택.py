from enum import Enum

stacklist = []


def instruction(inst):
    global stacklist
    index = 0
    commands = inst.split()
    command = commands[0]
    if Inst.PUSH.value == command:
        stacklist.append(commands[1])
        index += 1
    elif Inst.SIZE.value == command:
        print(len(stacklist))
    elif Inst.POP.value == command:
        if len(stacklist) == 0:
            print(-1)
        else:
            print(stacklist.pop())
            index -= 1
    elif Inst.EMPTY.value == command:
        if len(stacklist) == 0:
            print(1)
        else:
            print(0)
    elif Inst.TOP.value == command:
        if len(stacklist) == 0:
            print(-1)
        else:
            print(stacklist[index - 1])


class Inst(Enum):
    PUSH = 'push'
    POP = 'pop'
    TOP = 'top'
    SIZE = 'size'
    EMPTY = 'empty'


n = int(input())
lst = []

for i in range(n):
    lst.append(input())

for ins in lst:
    instruction(ins)