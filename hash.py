class Hashtable:
  def __init__(self):
    self.max=10
    # self.arr=[None for i in range(self.max)]
    self.arr=[[] for i in range(self.max)]
    
  def get_hash(self,key):
    h=0
    for c in key:
      h+=ord(c)
    return h% self.max
  
  
  # def __setitem__(self,key,val):
  #   h=self.get_hash(key)
  #   self.arr[h]=val
  
  def __setitem__(self,key,val):
    h=self.get_hash(key)
    found=False
    for idx,element in enumerate(self.arr[h]):
      if len(element)==2 and element[0]==key:
        self.arr[h][idx]=(key,val)
        found=True
        break
    if not found:
      self.arr[h].append((key,val))
    
  
  
  # def __getitem__(self,key):
  #   h=self.get_hash(key)
  #   return self.arr[h]
  
  def __getitem__(self,key):
    h=self.get_hash(key)
    for element in self.arr[h]:
      if element[0]==key:
        return element[1]
  
  def __delitem__(self,key):
    h=self.get_hash(key)
    for ind,element in enumerate(self.arr[h]):
      if element[0]==key:
        del self.arr[h][ind]
        break
      
      
    
  
  
  
t=Hashtable()
print(t.get_hash('march 6'))
print(t.get_hash('march 17'))
t['march 6']= 324
t['dec 8']=234
t['march 17']= 500
del t['march 17']
print(t['march 6'])
print(t.arr)