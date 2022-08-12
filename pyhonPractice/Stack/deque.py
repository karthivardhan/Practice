from collections import deque

stack = deque()
stack.append('a')
stack.append('b')
stack.append('c')

print(stack)

stack.pop()
print(stack)