import module
module.add()
module.sub()
module.mul()

print("\n")

import module as m
m.add()
m.sub()
m.mul()

print("\n")
'''
from module import *
add()
sub()
mul()

print("\n")
'''
from module import add,sub
add()
sub()
mul()
