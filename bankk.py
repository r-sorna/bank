while True:
  mail=input("enter your mail:")
  if "@" and "." in mail:
    if "gmail" and "outlook" in mail:
      break
    break    
  else:
    print("please enter valid mail id")
    continue
while True:
  schar=["@","#","%","*"]
  pas=input("enter your password:")
  if len(pas)==6 or len(pas)==7 or len(pas)==8:
    if pas in schar: 
      break
    break
  else:
    print("not valid")
    continue
while True:  
  phnum=input("enter your phone number:")  
  if phnum[0]=="9" or phnum(len)==10:
    break
  else:
    print("enter valid number")
    continue
def deposite():
    balance=0
    amount=0
    amount=float(input("enter amount"))
    balance+=amount
    print("amount deposited",amount)
def withdraw():
    balance=0
    amount=0
    amount=float(input("enter amount to be withdraw"))
    if balance>=amount:
        balance-=amount
        print("you withdrew:",amount)
    else:
        print("insufficient balance")
def avlbalance():
    balance=0
    print("your Available balance is:",balance)
print("enter your choice")
i=int(input("1.Deposite/2.withdraw/3.Available balace"))
if i==1:
    deposite()
elif i==2:
    withdraw()
elif i==3:
    avlbalance()
else:
    print("please Enter valid number")
    
