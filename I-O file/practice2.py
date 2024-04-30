with open("number.txt", "r") as f:
    n=f.read()
    num=""
    for i in range(len(n)+1):
        if n[i]==",":
            print(int(num), end= ' ')
            num= ""
        else:
            num+= n[i]
    