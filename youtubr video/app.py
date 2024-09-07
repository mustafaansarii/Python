n=112

reverse=0
while n:
    reverse=(reverse*10)+(n%10)
    n//=10
print(reverse)



