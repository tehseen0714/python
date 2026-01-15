class list_prgms:
    def append_one_list_to_another(self):
        list1=[1,2,3,4]
        list2=[5,6,7,8,9]
        for i in list2:
          list1.append(i)
        return list1
    
    def copy_a_list(self,list):
       list=[1,2,3,4,5,6,7]
       copy_list=[]
       for i in list:
        copy_list.append(i)
       return copy_list
    
    def count_number_of_strings(self,list):
       list=['abc','xyz','aba','1221']
       count=0
       for word in list:
        if len(word)>=2 and word[0]==word[-1]: 
         count+=1
       return count    
     
    def delete_element_using_index(self,list):
      list=['red','green','white','black','pink','yellow']
      del list[0]
      return list
    
    def list_words_longer_than_n(self,list):
      list=['xyz','abc','mno','qwer','tqews']
      count=3
      for word in list:
        if len(word)>3: 
          return word
        
    def product_of_list(self,list):
      list=[1,2,3,4,5,6,7,8,9]
      prod=1
      for i in list:
       prod*=i
      return prod    
    
    def to_remove_specific_elements(self,list):
      list=['red','green','white','black','pink','yellow']
      new_list=[]
      for i in range(len(list)):
       if i!=0 and i!=4 and i!=5:
        new_list.append(list[i])
      return new_list
    
    def smallest_element(self,list):
      list=[10,7,92,74,25]
      small=list[0]
      for i in list:
       if i<small:
        small=i
      return small
    
    def sort_list(self,list):
      list=[(2,5),(1,2),(4,4),(2,3),(2,1)]
      for i in range(len(list)):
       for j in range(i+1,len(list)):
        if list[i][1]>list[j][1]:
            list[i],list[j]=list[j],list[i]
       return list 
      
    def sum_of_list(self,list):
      list=[1,2,3,4,5,6,7,8]
      count=0
      for i in list:
       count+=i
      return count
    
    def to_check_for_common_member(self):
      list1=[1,2,3,4,5]
      list2=[9,8,7,6,5]
      found=False
      for i in list1:
       for j in list2:
        if i==j:
         found =True
      return found
    
    def to_remove_duplicate(self,list):
      list=[1,2,1,4,2,4,4,3,5]
      new_list=set(list)
      return new_list 
  
    
obj=list_prgms()   
result=obj.append_one_list_to_another()
print("after appending:",result)

copied_list=obj.copy_a_list(list)
print("copied list:",copied_list)

string=obj.count_number_of_strings(list)
print("number of strings:",string)

new_list=obj.delete_element_using_index(list)
print("new list:",new_list)

longer_words=obj.list_words_longer_than_n(list)
print("longer than 3 words:",longer_words)

product=obj.product_of_list(list)
print("product of lis:",product)

new_list=obj.to_remove_specific_elements(list)
print("New list:",new_list)
 
smallest_element=obj.smallest_element(list)
print("smallest element in the list:",smallest_element)

sorted_list=obj.sort_list(list)
print("sorted list is:",sorted_list)

sum=obj.sum_of_list(list)
print("sum of the list:",sum)

common_member=obj.to_check_for_common_member()
print("common member:",common_member)

new_list=obj.to_remove_duplicate(list)
print("new list:",new_list)