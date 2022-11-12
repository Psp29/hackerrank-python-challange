# A deque is a double-ended queue. It can be used to add or remove elements from both ends.
# Deques support thread safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.

from collections import deque
 
d = deque()
N = int(input("Enter total iterations: ").strip())

for _ in range(N):
    command = list(map(str, input("Please enter command with value: ").split()))
    if "append" in command:
        d.append(command[-1])
    elif "appendleft" in command:
        d.appendleft(command[-1])
    elif "pop" in command:
        d.pop()
    elif "popleft" in command:
        d.popleft()
        
print(f'Final queue is: {" ".join(d)}')