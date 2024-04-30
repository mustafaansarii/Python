# with open("demo.txt" , "r") as f:
#     data=f.read()

# with open("demo.txt", "w") as f:
#     f.write("helllo")

import os

# os.remove("demo.txt")

# with open("practice.txt","w") as f:
#     f.write("hi everyone\n how are you\n everything is going on!")

# with open("practice.txt","r") as f:
#     data=f.read()
# new=data.replace("how", "hey")
# print(new)

# with open("practice.txt","w") as f:
#     f.write(new)


with open("practice.txt" , "r") as f:
    data=f.read()
    if (data.find("word") != -1):
        print("found")
    else:
        print("not found")