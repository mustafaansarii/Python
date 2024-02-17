num= int(input("Enter the number: "))
table=[num*i for i in range(1,11)]
print(table)
with open("table.txt","a") as f:
    f.write(f"The table of ({num}):\n{str(table)}")
    f.write("\n")