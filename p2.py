# WAP to create a two level of Indentation. 
 
a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))
c = int(input("Enter the value for c: "))


if(a>b):
    if(a>c):
        print(a," is the largest")
    else:
        print(c," is the largest")
else:
    if(b>c):
        print(b," is the largest")
    else:
        print(c," is the largest") 
