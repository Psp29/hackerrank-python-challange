if __name__ == '__main__':
    N = int(input())
    stack = []
    
    for _ in range(N):
        command, *values = input().split()
        num_values = list(map(int, values))
        if command == 'print':
            print(stack)
        elif command == 'insert':
            stack.insert(num_values[0], num_values[1])
        elif command == 'append':
            stack.append(num_values[0])
        elif command == 'reverse':
            stack.reverse()
        elif command == 'remove':
            stack.remove(num_values[0])
        elif command == 'sort':
            stack.sort()
        elif command == 'pop':
            stack.pop()