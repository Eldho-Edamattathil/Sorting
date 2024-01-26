queue=[]

# first method

queue.append(10)
queue.append(20)
queue.append(30)
print(queue
      )

queue.pop(0)
print(queue)

# next method
queu1=[]
queu1.insert(0,10)
queu1.insert(0,20)
queu1.insert(0,30)
print(queu1)

queu1.pop()
print(queu1)
que1 = []

def enqueue():
    if limit ==len(que1):
      print("Que is full")
    else:
      num = int(input("Enter the number: "))
      que1.append(num)
      print(f'The number {num} has been added to the queue')

def dequeue():
    if not que1:
        print("Queue is empty")
    else:
        e = que1.pop(0)
        print(f'The number {e} has been removed')

def display():
    print(que1)

limit=int(input("Enter the limit"))
while True:
    choice = int(input("Enter the option: 1-Enqueue 2-Dequeue 3-Display 4-Exit "))
    
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Enter a proper option")
        
        
        
        
import collections
q=collections.deque()
q.append(10)
q.append(20)
print(q)
q.popleft()
q.appendleft(30)
q.pop()
print(q)


import queue
q=queue.Queue()
# In Queue , there it can take elements by put or put_nowait. If use only put mthod, if we define maxsize of queue by queue.Queue(3). Then if we try to add 4th element, 
# it will blok itme  until free slot is avaibable. To prevent that we can use put_nowait() or use timeout put(timeout=1) or put(block=False). bY Default block is true.
# same for get method 
q.put(10)
q.put(20)
q.put(30)
print(q)
print(q.get())
print(q.empty())
print(q.full())


q1=queue.PriorityQueue()
q1.put(10)
q1.put(20)
q1.put(40)
print(q1.get())
print(q1.get())


# priority with element

q2=[]
q2.append((1,2))
q2.append((3,5))
q2.append((2,6))
q2.append((4,4))
q2.sort(reverse=True)
print(q2.pop(0))




