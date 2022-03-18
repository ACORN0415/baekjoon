import sys
def input():
    return sys.stdin.readline().rstrip()
stack = []
N = int(input())
for x in range(0,N):
    command = input()
    if 'push' in command:
        number = command.split()[1]
        stack.append(number)
    elif command == 'pop':
        if len(stack)>0:
            top = stack.pop()
            print(top)
        else:
            print(-1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command =='top':
        if len(stack)>0:
            print(stack[len(stack)-1])
        else:
            print(-1)