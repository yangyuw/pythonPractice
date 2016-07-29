# coding=UTF-8

myString = 'hello world!'
print myString
# Python的print语句,与字符串格式运算符( %)结合使用,可实现字符串替换功能.%s 表示由一个字符串来替换,而%d
# 表示由一个整数来替换,另外一个很常用的就是%f, 它 表示由一个浮点数来替换
print "%s is number %d!" % ("Python", 1)
# raw_input()得到用户的输入
# user = raw_input('Enter login name: ')
# print 'Your login is:', user
# 获得命令帮助
help(raw_input)

# 列表元素用中括号( [ ])包裹,元素的个数及元素的值可 以改变。元组元素用小括号(( ))包裹,不可以更改(尽管他们的内容可以)
aList = [1, 2, 3, 4]
print aList
print aList[0]
print aList[2:]
print aList[:3]

aTuple = ('robots', 77, 93, 'try')
print aTuple
print aTuple[:3]
# aTuple[1] = 5 不能修改元组的值

# 字典
aDict = {'host': 'earth'}  # create dict
aDict['port'] = 80  # add to dict
print aDict
print aDict.keys()
print aDict['host']
for key in aDict:
    print key, aDict[key]

# if表达式不需要用大括号括起来.
x = 2
if x < .0:
    print '"x" must be atleast 0!'
elif x > 0:
    print '"x" is > 0!'

counter = 0
while counter < 3:
    print 'loop #%d' % (counter)
    counter += 1

for item in ['e-mail', 'net-surfing', 'homework', 'chat']:
    print item,

# 为了美观,带逗号的print语句输出的元素之间会自动添加一个空格.
who = 'knights'
what = 'Ni!'
print 'We are the', who, 'who say', what, what, what, what
print 'We are the %s who say %s' % (who, ((what + ' ') * 4))

# Python 提供了一个 range()内建函数来生成这种列表
for eachNum in range(3):
    print eachNum
  # range() 函数经常和len()函数一起用于字符串索引.
foo = 'abc'
for i in range(len(foo)):
    print foo[i], '(%d)' % i
for i, ch in enumerate(foo):
    print ch, '(%d)' % i

# 列表解析
squared = [x ** 2 for x in range(4)]
for i in squared:
    print i

sqdEvens = [x ** 2 for x in range(8) if x % 2]
for i in sqdEvens:
    print i

# 文件和内建函数open() file()
# filename = raw_input('Enter file name:')
# fobj = open(filename, 'r')
# for eachLine in fobj:
#     print eachLine,
# fobj.close()


# 错误和异常处理
# try:
#     filename = raw_input('Enter file name:')
#     fobj = open(filename, 'r')
#     for eachLine in fobj:
#         print eachLine, fobj.close()
# except IOError, e:
#     print 'file open error:', e

# 函数
def addMe2Me(x):
    'apply + operation to argument'
    return (x + x)
print addMe2Me(4.25)

# 类 类的首字母要大写,由于类可以起到模板的作用,因此可以在创建类的实例的时候,把我们属性强制绑定进去
# 数据封装


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s\'s age is: %s' % (self.name, self.score)

bart = Student('Bart Simpson', 59)
print bart.name
print bart.score
bart.print_score()

# 模块
import sys
sys.stdout.write('Hello World!\n')
print sys.platform
print sys.version

# 实用的函数
# dir([obj]) 显示对象的属性,如果没有提供参数, 则显示全局变量的名字
# help([obj]) 以一种整齐美观的形式 显示对象的文档字符串, 如果没有提供任何参 数, 则会进入交互式帮助。
# int(obj) 将一个对象转换为整数
# len(obj) 返回对象的长度
# open(fn, mode) 以 mode('r' = 读, 'w'= 写)方式打开一个文件名为 fn 的文件
# range([[start,]stop[,step]) 返回一个整数列表。起始值为 start, 结束值为 stop - 1; start 默认值为 0, step默认值为1。
# raw_input(str) 等待用户输入一个字符串, 可以提供一个可选的参数 str 用作提示信 息。
# str(obj) 将一个对象转换为字符串
# type(obj) 返回对象的类型(返回值本身是一个 type 对象!)

# chapter3
# _xxx是私有变量
