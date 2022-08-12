from queue import LifoQueue

stack = LifoQueue()
stack.put('a')
stack.put('b')


print(stack.qsize())

print(stack.get())