# def seletion(list1):
#   for i in range(len(list1)-1):
#     min_val=min(list1[i:])
#     min_ind=list1.index(min_val,i)
#     if list1[i]!=list1[min_ind]:
#       list1[i],list1[min_ind]=list1[min_ind],list1[i]
#   return list1

# list1=[1,5,4,6,32,1]
# print(seletion(list1))

num=int(input("Enter the length of list"))
print("ENter values")
list1=[int(input()) for x in range(num)]
for i in range(len(list1)-1):
  m_ind=i
  for j in range(i+1,len(list1)):
    if list1[j]<list1[m_ind]:
      m_ind=j
      
  if list1[i]!=list1[m_ind]:
    list1[i],list1[m_ind]=list1[m_ind],list1[i]
    
    

print(list1)