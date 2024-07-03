#你好，世界
print('Hello World')

#诈骗短信的例子x
print ('Hi, %s, you have $%d' % ('Michael',100000))

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby','PHP'],
    ['Adam', 'Bart','Lisa']
]

#打印出苹果
print(L[0][0])

#打印出蟒蛇
print(L[1][1])

#打印出丽莎
print(L[2][2])

#BMI指数的练习
bmi = 80.5/(1.5**2)
if bmi < 18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
elif bmi < 28:
    print('超重')
elif bmi < 32:
    print('肥胖')
else:
    print('太胖了')

# case的例子
age = 3
match age:
    case x if x <10:
        print(f'< 10 years old: {x}')
    case 10:
        print('10 years old.')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11~18 years old.')
    case 19:
        print('19 years old.')
    case  _:
        print('not sure.')

# case列表的例子
args = ['gcc', 'hello.c', 'world.c']
# args = ['clean']
# args = ['gcc']

match args:
    # if gcc only, warning:
    case ['gcc']:
        print('gcc: missing source files.')
    # shouing gcc, and miss 1 designated file.
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    # showing clean only:
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')

#for ... in ... 循环的例子
names = ['Water', 'Paper', 'Plant']
for name in names:
    print(name)

#计算整数之和的例子
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

#range()函数的例子
sum = 0 
for x in range(101):
    sum = sum + x
print(sum)

#重复输出列表中的字符的练习
L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print(f'Greetings,{x}')

#打断循环的例子
n = 1 
while n <= 100:
    print(n)
    n = n + 1
print('Done')

#提前打断的例子
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('What r u looking at?') 

#跳过当前循环的例子
n = 0
while n <10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)

#字典的例子
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

# 'list' 有序可变序列，用[]表示,用',' 分隔,支持索引、切片、添加、删除、修改等。
# 'tuple' 有序不可变序列，用()表示, 用','，分隔 不支持添加、删除、修改。 支持索引、切片。用于存放不可变数据。
# 'dict'无序键值对集合，用'{}'表示，键值对用':'键值用','分隔，支持通过键访问值。常用于姓名电话等。
# 'set'无序元素集合，用'{}'表示，用','分隔。内容可被重复录入，但只有一个。
#相互转化需要转化函数。

#使用hex()函数将整数转化为十六进制字符串的函数
n1 = 225
n2 = 1000
n = [n1, n2]
for x in n:
    print(hex(x))

#定义函数并且解一元二次方程的练习  搞不明白？
import math
def quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b + math.sqrt(discriminant)) / (2*a)
    elif discriminant == 0:
        root = -b / (2*a)
        return root, root
    else:
        real_part = -b / (2*a)
        imag_part = math,sqrt(-discriminant) / (2*a)
        return complex(real_part, imag_part), complex(real_part, -imag_part)
a = float(input('1'))
b = float(input('-2'))
c = float(input('3'))
roots = quadratic_equation(a, b, c)
print(roots)
