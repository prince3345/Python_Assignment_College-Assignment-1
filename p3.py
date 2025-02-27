# WAP to create a user define function and perform separate arithmetic Operator.

num1 = int(input("enter number1:"))
num2 = int(input("enter number2:"))
def add(num1 , num2):
    ans =num1+ num2
    print(ans) 

def sub(num1 ,num2):
    ans= num1-num2
    print(ans)

def mul(num1 ,num2):
    ans= num1*num2
    print(ans)

def div(num1 ,num2):
    ans= num1/num2
    print(ans)

def mod(num1 ,num2):
    ans= num1%num2
    print(ans)

print("enter 1 for addition")
print("enter 1 for subtraction")
print("enter 1 for multiplication")
print("enter 1 for divison")
print("enter 1 for modulus")
choice = input("choice =")
if choice == 1:
    num1 = int(input("enter number1:"))
    num2 = int(input("enter number2:"))
    add()
    
elif choice ==2:
    num1 = int(input("enter number1:"))
    num2 = int(input("enter number2:"))
    sum()
    
elif choice ==3:
    num1 = int(input("enter number1:"))
    num2 = int(input("enter number2:"))
    sub() 
    
elif choice == 1:
    num1 = int(input("enter number1:"))
    num2 = int(input("enter number2:"))
    div()  
    
elif choice == 1:
    num1 = int(input("enter number1:"))
    num2 = int(input("enter number2:"))
    mod()           