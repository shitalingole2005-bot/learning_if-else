x=int(input("enter the no."))
y=int(input("enter the no."))
if x > 0 and y > 0:
    print("quedrant 1")
elif x < 0 and y > 0:
    print("que 2")
elif x > 0 and y < 0:
    print("que 3")
elif x < 0 and y < 0:
    print("que 4")
elif x == 0 and y == 0:
    print ("origin")
else:
    print("invalid")