class Hashtable:
  def __init__(self):
    self.max=15
    self.arr=[[] for i in range(self.max)]
  
  
  def get_hash(self,key):
    h=0
    for c in key:
      h=+ord(c)
      
    return h% self.max

  def __setitem__(self,key,value):
    h=self.get_hash(key)
    found=False
    for ind, element in enumerate(self.arr[h]):
      if len(element)==2 and element[0]==key:
        self.arr[h][ind]=(key,value)
        found=True
        break
    if not found:
      self.arr[h].append((key,value))
      
  def __getitem__(self,key):
    h=self.get_hash(key)
    for element in self.arr[h]:
      if element[0]==key:
        return element[1]
      
  def find_max_value(self):
        max_value = 0  # Start with negative infinity as the initial max value
        for sublist in self.arr:
            for element in sublist:
                if element[1] > max_value:
                    max_value = element[1]
        return max_value
      
      
  def find_average(self):
        total_values = 0
        total_count = 0
        for sublist in self.arr:
            for element in sublist:
                total_values += element[1]
                total_count += 1

        if total_count == 0:
            return 0  
        return total_values / total_count
      
h=Hashtable()
h['Jan 1']=	27
h['Jan 2']=	31
h['Jan 3']=	23
h['Jan 4']=	26
h['Jan 5']=	29
h['Jan 6']=	31
h['Jan 7']=	35


print(h.arr)
s=h.find_max_value
print(s)
print(h.find_average)



dict1={}
dict1={'jan1':1,'jan2':2,'jan3':3,'jan4':4}

max_value=max(dict1.values())
print(max_value)


    