a=302010
s=0
while a!= 0:
    rem = a%10
    if rem == 0:
        a = a//10
        continue
    else:
        s = s*10+rem
        a = a//10
print(s)
