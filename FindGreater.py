a = int(input("enter the value"))
b = 0
while a>0:
    d = a % 10
    if d>b:
        b=d
        a= a//10
        print("greter value:",b)
