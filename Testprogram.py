# first example
from queues import Queue
 
fifo = Queue()
fifo.enqueue("1st")
fifo.enqueue("2nd")
fifo.enqueue("3rd")
print("First Example")
print(fifo.dequeue())

print(fifo.dequeue())

print(fifo.dequeue())

#second example
from queues import Queue

fifo = Queue("1st", "2nd", "3rd")
print("\nSecond Example")
print(len(fifo))

for element in fifo:
    print(element)

print(len(fifo))

#third example
from queues import Stack
print("\nThird Example")
lifo = Stack("1st", "2nd", "3rd")
for element in lifo:
    print(element)