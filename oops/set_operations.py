class set_operations:
  
  def create_set(self,set):
    set={1,2,3,4,5,6,7}
    return set

  def clear_set(self,set):
    set={1,2,3}
    set.clear()
    return set
  
  def remove_element(self,set):
    set={1,2,3,4,5,6,7,8}
    for i in set.copy():
     if i==8:
      set.remove(i)
    return set
  
  def set_intersection(self):
    set1={1,2,3,4,5}
    set2={9,8,7,6,5,4}
    for i in set1:
     for j in set2:
        if i==j:
            return i
        
  def  iteration(self,set):
    set={1,2,3,4,5,6,7}
    for i in set:
     return set
   
  def max_of_set(self,set):
    set={1,2,3}
    return max(set)
  
  def min_of_set(self,set):
    set={1,2,3}
    return min(set)
  
  def frozen_set(self,set):
    frozen_set=frozenset([1,2,3,4,5])
    return (frozen_set)
  
obj=set_operations()

set=obj.create_set(set)
print("set:",set)

set=obj.clear_set(set)
print("set:",set)

set=obj.remove_element(set)
print("set:",set)

set=obj.set_intersection()
print("intersecting set:",set)

set=obj.iteration(set)
print("set:",set)

max=obj.max_of_set(set)
print("maximum:",max)

min=obj.min_of_set(set)
print("minimum:",min)

frozen_set=obj.frozen_set(set)
print("frozen set:",frozen_set)




