def check_for_line():
    word="learning"
    line=1
    with open ("practice.txt" , "r") as f:
        while True:
            data=f.readline()
            if (word in data):
                print(line)
            line +=1
    return -1

check_for_line()
        
