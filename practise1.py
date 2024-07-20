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

# 基础的函数 
# print() 输出内容到控制台
# input() 从控制台读取输入
# type() 给出对象的类型
# len() 给出对象的长度/项目数
# int() 将数字或字符串转换为整数
# float() 将数字转换为浮点数
# str() 将对象转换为字符串
# bool() 将对象转换为布尔值  true/false
# range() 给出一个表示整数序列的不可变序列对象
# list() 将可迭代对象转换为列表
# tuple() 将可迭代对象转换为元组
# set() 创建一个无序且不包含重复元素的集合
# dict() 创建一个字典，可以储存键值对儿
# sorted() 可迭代对象进行排序并返回新的已排序列表 [3,1,4,1,5,9]变为 [1,1,3,4,5,9]
# enumerate() 将一个可遍历的数据对象组合为一个索引序列，并列出数据和数据下标
# round() 对浮点数进行四舍五入
# abd() 给出数字的绝对值
# sum() 计算可迭代对象的总和
# min() 给出可迭代对象的最小值
# max() 最大值
# any() 判断对象是否至少有一个元素为True
# all() 判断对象是否所有元素都是true

#使用hex()函数将整数转化为十六进制字符串的函数
n1 = 225
n2 = 1000
n = [n1, n2]
for x in n:
    print(hex(x))

#定义函数并且解一元二次方程的练习  搞不明白？

import math

def quadratic(a, b, c):
    if a == 0:
        raise ValueError("系数a不能为0")
    
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root, root
    else:
        real_part = -b / (2*a)
        imag_part = math.sqrt(-discriminant) / (2*a)
        return complex (real_part, imag_part), complex(real_part, -imag_part)

root1, root2 = quadratic(1, -3, 2)
print(f"方程 x^2 - 3x + 2 = 0 的解为：{root1} 和 {root2}")
root1, root2 = quadratic(1, 1, 1)
print(f"方程 x^2 + x + 1 = 0 的解为：{root1} 和 {root2}")

print('New Season')

#二维平面移动坐标的例子
import math
def move (x, y, step, angle=0) :
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

#位置参数

#自制 x 平方的函数
def power(x):
    return x * x
print(power(5))

#自制 x 的 n 次方的函数

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print( power(5, 2))

#使二次方为默认值的函数

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5))
print(power(5, 3))
 
#例子-学生注册的函数 enroll 注册
def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)

print(enroll('Sarah', 'F'))

#继续扩大注册需要的信息范围

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age', age)
    print('city:', city)

print(enroll('sarah', 'F'))
print(enroll('Bob', 'M', 7, city='Tianjin'))

#一个关于默认参数的糟糕的例子
def add_end(L=[]):
    L.append('END')
    return L
print(add_end([1, 2, 3]))
print(add_end(['x', 'y', 'z']))
print(add_end())
print(add_end())

#上面这个函数的修复方法
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())
print(add_end())

#定义一个函数的例子

def calc(numbers):
    sum = 0 
    for n in numbers:
        sum = sum + n * n
    return sum
print(sum)

print(calc([1, 2, 3]))

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

nums = [1, 2, 3]
print(calc(*nums))


#关键字参数的例子

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Bob', 35, city='Beijing')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])

#命名关键字参数的例子
def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)
person('jack', 24, city='Beijing', addr='Chaoyang', zipcode=100010)
def person(name, age, *, city, job):
    print(name, age, city, job)
person('Jack', 24, city='Beijing', job='Engineer')

def person(name, age, *argus, city, job):
    print(name, age, args, city, job)

#参数组合的例子
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
f1(1,2)
f1(1,2,c=3)
f1(1,2,3, 'a', 'b')
f1(1,2,3, 'a', 'b', x=998)
f2(1,2,d=99, ext=None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

#将一个允许两个数计算的函数变成可以接受一个或多个数计算的函数
def mul(*args):
    sum = 1
    for num in args:
        sum *= num
    return sum
print(mul(2, 3))
print(mul(2, 3, 4))

#递归乘阶的练习

def fact(n):
    if n ==1:
        return 1
    return n * fact(n - 1)
print(fact(100))
#要注意防止栈溢出 递归的数量不要太大

#以下是优化防溢出的例子
def fact(n):
    return fact_iter(n, 1)
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print(fact_iter(5, 1))

#汉诺塔的练习 移动N个盘子从A到C需要哪些步骤

def move(n, a, b, c):
    if n == 1:
        print(f"{a} to {c}")
    else:
        move(n - 1, a, c, b)
        print(f"{a} to {c}")
        move( n - 1, b, a, c)
move(3, 'A', 'B', 'C')