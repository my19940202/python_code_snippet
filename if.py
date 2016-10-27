'''
age = 12
if age >= 18:
    print 'your age is', age
    print 'adult'
print 'END'
#not
pp = 90
if not age  >= 30:
    print pp

print 'if else'
# if else
if age >= 18:
    print 'adult'
else:
    print 'teenager'


#if elif  (elseif)
if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teenager'
elif age >= 3:
    print 'kid'
else:
    print 'baby'

#for LOOP
L = ['Adam', 'Lisa', 'Bart']
for name in L:
    print name

# while 
N = 10
x = 0
while x < N:
    print x
    x = x + 1




#python x++ have no such grammer only +=
sum = 0
x = 1
while x <= 100000:
    if x%2 == 1:
        sum += x
    if x == 100:
        break;
    x += 1
print sum



#
sum = 1
x = 1
n = 1
while True:
    sum += x
    x *= 2
    n += 1
    if n > 20:
        break
print sum
print x

'''
# continue 
sum = 0
x = 0
while True:
    x = x + 1
    if x > 10:
        break
    if x%2 == 0:
        continue
    sum += x
print sum




