a= 1234
tem = a
rev=0
while a>0:
    last = a%10
    rev = rev*10+last
    a=a//10
    print(rev)
if tem==rev:
    print("palindrome")
else:
    print("not palindrome")