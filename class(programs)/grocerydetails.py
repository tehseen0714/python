class grocery:
    def __init__(self):
      self.grocery={}

    def rice(self):
       rice_type=input("rice name sona masoori/basmati:")
       weight=int(input("enter weight of rice(kg):"))
       if rice_type=="sona_masoori":
          price=50*weight
       elif rice_type=="basmati":
          price=60*weight
       else:
          print("invalid")
          return
       self.grocery[rice_type]={"weight":weight,"price":price}
       print("price",price)
    
    def pulse(self):
       pulse_type=input(" types of pulse 1. lentils 2.beans 3.peas")
       weight=int(input("enter weight of pulse"))
       if pulse_type=="lentils":
          price=50*weight
       elif pulse_type=="beans":
          price=45*weight
       elif pulse_type=="peas":  
          price=60*weight
       else:
          print("invalid")
          return 
       self.grocery[pulse_type]={"weight":weight,"price":price}
       print("price",price)

    def wheat(self):
       wheat_type=input("flour or grains")
       weight=int(input("enter weight:"))
       if wheat_type=="flour":
          price=50*weight
       elif wheat_type=="grains":
          price=40*weight
       else:
          print("invalid")
          return
       self.grocery[wheat_type]={"weight":weight,"price":price}
       print("price",price)


if __name__=="__main__":

     obj=grocery()
     while True:
       print("1.rice 2. pulse  3.wheat 4.exit")
       choice=int(input("Enter your choice:"))
       if choice==1:
         obj.rice()
       elif choice==2:
         obj.pulse()
       elif choice==3:
        obj.wheat()
       elif choice==4:
        print("exiting program")
        break
       else:
        print("invalid choice")
         

            
            
        

       

        
          
    
