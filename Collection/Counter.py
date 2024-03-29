from collections import Counter
a=[1,2,2,1,1,1,2,34,5,]
c=Counter(a)
print(c)

print(list(c.elements()))

print(c.most_common())

sub={2:1,2:2}
print(c.subtract(sub))
print(c.most_common())
