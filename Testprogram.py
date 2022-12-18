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

#fourth example
lifo = []
print("\nFourth Example")
lifo.append("1st")
lifo.append("2nd")
lifo.append("3rd")

print(lifo.pop())
print(lifo.pop())
print(lifo.pop())

#fifth example
from heapq import heappush
print("\nFifth Example")
fruits = []
heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(fruits, "banana")

print(fruits)

#sixth example
from heapq import heappop
print("\nSixth Example")
print(heappop(fruits))
print(fruits)

#seventh example
person1 = ("John", "Brown", 42)
person2 = ("John", "Doe", 42)
person3 = ("John", "Doe", 24)
print("\nSeventh Example")
print(person1 < person2)

print(person2 < person3)

#eight example
from queues import PriorityQueue
CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

messages = PriorityQueue()
messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

print("\nEighth Example")
print(messages.dequeue())