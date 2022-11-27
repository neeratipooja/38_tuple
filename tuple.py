'''
DATE=27th NOV 2022
DAY= sunday
TOPIC= tuple
AUTHOR= pooja
'''
g=9,
print(type(g)) #tuple
y=('bajaj','anil','godrej')
# y[1]='hp' #typeerror:'tuple' object does not support item assignment
h='hey'    ,   'pooja'
print(h,type(h)) #('hey', 'pooja')
# print(h[2]) inexerror: tuple index out of range
print(h[1]) #pooja
u=(1,3,4.2,'hey',[8,9],('k','p'),None,True)
print(u.count(4.2)) #1
print(u.index([8,9])) #4
print(u.index('hey')) #3