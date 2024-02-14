class Vector:
    def __init__(self,vec):
        self.vec=vec
    def __str__(self):
        str1= ""
        index=0
        for i in self.vec:
            str1 += f" {i} a{index} +"
            index+=1
        return str1[:-1]
    def __add__(self, vec2):
        newlist=[]
        for i in range(len(self.vec)):
            newlist.append(self.vec[i]+vec2.vec[i])
v1=Vector([1,2,3])
v2=Vector([11,12,13])
print(v1)
print(v2)
