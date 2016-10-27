
names = ['Michael', 'Bob', 'Tracy']
for name in names:
	print	'Hello, '+ name + '!'

'''
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)
'''

listnum = list(range(101))
# print listnum
sum = 0
for x in xrange(1,101):
	sum += x
print sum


sum = 0
n = 100
while n > 0:
    sum = sum + n
    n = n - 1
print(sum)