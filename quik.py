def pivot_vv(list1,first,last):
  pivot=list1[first]
  left=first+1
  right=last
  while True:
    while left<=right and list1[left]<=pivot:
      left+=1
    while left<=right and list1[right]>=pivot:
      right-=1
    if right<left:
      break
    else:
      list1[left],list1[right]=list1[right],list1[left]
  list1[first], list1[right] = list1[right], list1[first]

  
  return right

def quil_sort(list1,first,last):
  if first<last:
    p=pivot_vv(list1,first,last)
    quil_sort(list1,first,p-1)
    quil_sort(list1,p+1,last)
    
    
    
list1=[6213,2213,1231,3213,5,3]
n=len(list1)-1
quil_sort(list1,0,n)
print(list1)



# for random pivot
# import random
# def pivot(list1,first,last):
#   rand_index=random.randint(first,last)
#   list1[rand_index],list1[first]=list1[first],list1[rand_index]
#   pivot=list1[first]
#   left=first+1
#   right=last
#   while True:
#     while left<right and list1[left]<=pivot:
#       left+=1
#     while left<right and list1[right]>=pivot:
#       right-=1
#     if right<left:
#       break
#     else:
#       list1[left],list1[right]=list1[right],list1[left]
#   list1[first], list1[right] = list1[right], list1[first]

  
#   return right

# def quil_sort(list1,first,last):
#   if first<last:
#     p=pivot(list1,first,last)
#     quil_sort(list1,first,p-1)
#     quil_sort(list1,p+1,last)
    
    
    
# list1=[6,2,1,3,5,3]
# n=len(list1)-1
# quil_sort(list1,0,n)
# print(list1)

# median
# import statistics  
# def pivot(list1,first,last):
#   low=list1[first]
#   high=list1[last]
#   mid=(first+last)//2
#   mid_val=list1[mid]
#   pivot_val=statistics.median([low,mid_val,high])
#   if pivot_val==low:
#     pind=first
#   elif pivot_val==high:
#     pind=last
#   else:
#     pind=mid
    
#   list1[first],list1[pind]=list1[pind],list1[first]
  
  
  
  
  
  
  
#   pivot=list1[first]
#   left=first+1
#   right=last
#   while True:
#     while left<right and list1[left]<=pivot:
#       left+=1
#     while left<right and list1[right]>=pivot:
#       right-=1
#     if right<left:
#       break
#     else:
#       list1[left],list1[right]=list1[right],list1[left]
#   list1[first], list1[right] = list1[right], list1[first]

  
#   return right

# def quil_sort(list1,first,last):
#   if first<last:
#     p=pivot(list1,first,last)
#     quil_sort(list1,first,p-1)
#     quil_sort(list1,p+1,last)
    
    
    
# list1=[6,2,1,3,5,3]
# n=len(list1)-1
# quil_sort(list1,0,n)
# print(list1)