count=0
with open("number.txt", "r") as f:
    n=f.read()
    num=n.split(",")
    for i in num:
        if (int(i)%2==0):
            count+=1
print(count)    