
# basics

# list1=[10,35,3,45,3]
# def bubble(list1):
#   for j in range(len(list1)-1):
#     for i in range(len(list1)-1):
#       if list1[i]>list1[i+1]:
#         list1[i],list1[i+1]=list1[i+1],list1[i]

# bubble(list1)
# print(list1)




# without j in i loop

# list1 = []
# num = int(input("Enter the length: "))
# print("Enter the values:")
# for k in range(num):
#     list1.append(int(input()))

# print("The list you entered:", list1)

# def bubble(list1):
#   for j in range(len(list1)-1):
#     for i in range(len(list1)-1):   
#       if list1[i]>list1[i+1]:
#         list1[i],list1[i+1]=list1[i+1],list1[i]
#         print(list1)
#       else:
#         print(list1)
#     print(" ")

# bubble(list1)
# print(list1)




# with j in i loop
list1 = []
num = int(input("Enter the length: "))
print("Enter the values:")
for k in range(num):
    list1.append(int(input()))

print("The list you entered:", list1)

def bubble(list1):
  for j in range(len(list1)-1):
    for i in range(len(list1)-1-j):   
      if list1[i]>list1[i+1]:
        list1[i],list1[i+1]=list1[i+1],list1[i]
        print(list1)
      else:
        print(list1)
    print(" ")
  return list1

bubble(list1)



