
# This file was *autogenerated* from the file ./dice.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5)#!/usr/bin/sage

# Transition matrix

T = matrix(QQ, _sage_const_7 )

for i in range(_sage_const_0 ,_sage_const_6 ):
    T[i,i] = i/_sage_const_6 
    T[i,i+_sage_const_1 ] = (_sage_const_6 -i)/_sage_const_6 

T[_sage_const_6 ,_sage_const_6 ]=_sage_const_1 

rolls = _sage_const_5 

# Outcome matrix

O = T**rolls

# Expected number of different outcomes

E = _sage_const_0 
for i in range(_sage_const_1 ,_sage_const_7 ):
    E = E+i*O[_sage_const_0 ,i]

print(E)
print(float(E))
