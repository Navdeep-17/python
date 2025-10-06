#public
class person:
    def __init__(self,x,y):#init is special method ,refer as initializer or constructor,self object referance
        self.name=x
        self.age=y
p=person("dinesh","19")#"p" object referance,Person object creation
print(p.name)
print(p.age)

#producted
class person:
    def __init__(self,x,y):#init is special method ,refer as initializer or constructor,self object referance
        self._name=x
        self._age=y
p=person("dinesh","19")#"p" object referance
print(p._name)
print(p._age)

#private
class person:
    def __init__(self,x,y):#init is special method ,refer as initializer or constructor,self object referance
        self.__name=x
        self.__age=y
p=person("dinesh","19")#"p" object referance
print(p._person__name)
print(p.__age)