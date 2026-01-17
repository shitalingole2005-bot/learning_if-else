n = 1234
sum= 0
while n>0:
    last= n%10
    print(n)
    n= n//10
    sum = sum + last
    print("sum of digit:",sum)