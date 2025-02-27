# WAP to declare global variable. 

var =10
def f():
    global var 
    var=20
    print(var)
f()    
print(var)    