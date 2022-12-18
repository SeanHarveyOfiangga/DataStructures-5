# first example
from queues import Queue
 
fifo = Queue()
fifo.enqueue("1st")
fifo.enqueue("2nd")
fifo.enqueue("3rd")

print(fifo.dequeue())

print(fifo.dequeue())

print(fifo.dequeue())

#second example
from queues import Queue

fifo = Queue("1st", "2nd", "3rd")
print()
print(len(fifo))

for element in fifo:
    print(element)

print(len(fifo))
