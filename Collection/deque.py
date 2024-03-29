from collections import deque

a=['e','r','e']
d=deque(a)
print(d)

d.append("python")
print(d)

d.appendleft("python")
print(d)

d.pop()
print(d)

d.popleft()
print(d)

print(type(d))

g=deque([])
print(g.append(67))