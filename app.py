# Things to remember while creating python variables
# must start with letter or underscore
# can not start with numbers
# can only contain alphanumeric and underscore
# can not be any keywords
# variables are case sensitive

'''
local variable (define inside method or function)
global variable (define outside method or function)
'''

x = 5  # int
y = "Python"  # string
print(x)
print(y)

a = b = c = 1
print(a)
print(b)
print(c)


# city = ["Tokyo","Mumbai","New York City"]
p,q,r = ["Tokyo","Mumbai","New York City"]
# print(p)
# print(q)
# print(r)
print(p+'\n'+ q+'\n'+r)
print(p,q,r)

print(type(x))
x=str(x)
print(type(x))
print(type(y))



'''
+ - * / % // : Arithmatic  operator
=, +=,-=,/=,*=,%= : assignment operator
==, <=,>=, >, <, != : comparison operator
and, or, not: logical operator
XOR, OR, NOT, AND: bitwise operator

'''


i = 10
i = i+ 10
print(i)
i+=10
print(i)

