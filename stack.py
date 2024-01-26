# stack using list 
# stack can be  implemented using list or modules"""
# stack uses lifo order
# bascis operaions push and pop
# whwn using list, append is used for push


# stakkkk
# stak is the ordered colletion of item in which additoion and removal of item always take aat same end.This end is top and opposite end is base.
# stak stores item in LIFO order.
# 4 operations
# push, pop, peektop, isempty
# appliation of stak: to reverse sstring ,, used in forward and bakward features in web browsers, undo features


# stack=[]
# stack.append(10)
# stack.append(20)
# stack.append(50)
# print(stack)

# stack.pop(1)
# print(stack)

# # to check stack is empty:
# len(stack)==0
# not stack

# print(not stack)


# # push

# def push():
 
#   if len(stack)==limit:
#     print("Stck is full")
#   else: 
#     num=int(input("enter the elememt"))
#     stack.append(num)
#     print(stack)
  


# def pop_element():
#   if not stack:
#     print("Stck empty")
#   else:
#     e=stack.pop()
#     print(f'element {e} has been removed')
#     print(f'Updated stack: {stack}')

# limit=int(input("Enter the limit of stack"))
# while True:
  
#   choice=int(input("Enter the opreation choice 1-push 2-push 3-quit"))
#   if choice==1:
#     push()
#   elif choice==2:
#     pop_element()
    
#   elif choice==3:
#     break
#   else:
#     print("Enter the cporrect option")
    
    
  # same can be done with modules as well
  
# import collections
# stack=collections.deque()
# stack.append(1)
# stack.append(2)
# print(stack)
# stack.pop()
# print("dsjaf")
# print(stack)


import queue
stack=queue.LifoQueue(3)
stack.put(10)
stack.put(20)
stack.put(40,timeout=1)
while not stack.empty():
    print(stack.get())

