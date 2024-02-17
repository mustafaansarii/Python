def readfile(filename):
    with open (filename,"r") as f:
        print(f.read())
readfile("1.txt")
readfile("2.txt")
readfile("3.txt")