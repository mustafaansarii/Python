class GrandparentClass:
    pass

class ParentClass1(GrandparentClass):
    pass

class ParentClass2:
    pass

class ChildClass(ParentClass1, ParentClass2):
    pass
