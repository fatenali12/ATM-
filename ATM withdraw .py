#python 3.7.1

class ATM:
   def __init__(self,balance,bank_name):
       self.balance=balance
       self.bank_name=bank_name
       self.withdrawals_list=[]
   
   def withdraw(self,request):
       print("Welcome to ",self.bank_name)
       print("Current balance = "+str(self.balance))
      
       if request>self.balance:
          print("More than the Available amount")
          
       elif request<0:
          print("More than zero please")
          
       else:
         
          self.balance-=request
          
          self.withdrawals_list.append(request)
          
          notes = [100, 50, 10, 5] 
          for note in notes: 
             while request >= note:
                print("give ",str(note))
                request-=note
                if request<5 and request>0:
                   print("give ",str(request))
                   request=0            
    
       return self.balance
       
   def show_withdrawals(self):
       for withdrawals in self.withdrawals_list:
          print("withdrawal amount is "+str(withdrawals))  
       
balance1=500
balance2=700

atm1=ATM(balance1,"Smart Bank")   
atm2=ATM(balance2,"Baraka Bank") 

atm1.withdraw(600)
atm1.withdraw(277)
 
atm1.show_withdrawals()


atm2.withdraw(200)
atm2.withdraw(500)

atm2.show_withdrawals()