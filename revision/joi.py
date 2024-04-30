def split_and_join(line):
    # write your code here
    line=line.split()
    b="-".join(line)
    print(b)

print(split_and_join("this is ram"))