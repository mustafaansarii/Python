a=[2,3,4,5,5,6,7,8,9,8,76,65,5,43,23,23,32,3,2]

# b=[]
# for itam in a:
#     if itam%2==0:
#         b.append(itam)
# print(b)

#shortcute for the same
b=[i for i in a if i%2==0]
print(b)

t={1,2,3,4,5,6,67}
s={i for i in t}
print(t)