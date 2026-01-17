a= 1234
rev=0
while a>0:
    last = a%10
    rev = rev*10+last
    a=a//10
    print(rev)