# list 遍历
names = ['Michael', 'Bob', 'Tracy']
for name in names:
	print	'Hello, '+ name + '!'

# dict 遍历
myset = {
    'a': 1234,
    'c': 34,
    'b': '312',
    'd': 312
}
for key in myset:
    print key, myset[key]


# while 使用
sum = 0
n = 100
while n > 0:
    sum = sum + n
    n = n - 1
print(sum)