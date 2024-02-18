def sqare(num):
    return num*num
l1=[4,2,3]
# l2=[]
# for item in l1:
#     l2.append(sqare(item))
# print(l2)

print(list(map(sqare,l1)))
print(set(map(sqare,l1)))