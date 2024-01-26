

def insertion(my_list):
  for i in range(1,len(my_list)):
    current_value=my_list[i]
    pos=i
    while current_value<my_list[pos-1] and pos>0:
      my_list[pos]=my_list[pos-1]
      pos=pos-1
    my_list[pos]=current_value
    

my_list=[1,32,332,219,1233]    
insertion(my_list)
print(my_list)