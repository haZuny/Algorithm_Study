import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    command = sys.stdin.readline().split()
    if len(command) == 2:
        stack.append(command[1])
    else:
        command = command[0]
        if command == "pop":
            try:
                print(stack.pop())
            except:
                print(-1)                
        elif command == "size":
            print(len(stack))
        elif command == "empty":
            print( 1 if len(stack)==0 else 0 )
        else:
            try:
                print(stack[-1])
            except:
                print(-1)
