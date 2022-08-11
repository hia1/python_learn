# -- coding: utf-8 --


print("python字符串格式化输出")
print("hello", "python", 'world')  # 添加空格
print("he\tworld")
print("\tworld")
print("hello\nworld")  # \n是换行，n是newword
print("hello\tworld")  # \t是制表符，4位表示一个制表符，所以这三个输出中间的空格不一样
print("helloo\tworld")
print("hellooo\tworld")
print("hello\rworld")  # \r:world将hello进行了覆盖
print("hello\bworld")  # \b退一个格

print('http:\\\\www.baidu.com.')
print("http:\\\\www.baidu.com.")
print('老师说：\'大家好！\'')  # 斜杠和单引号在斜杠后面可以正常输出，如果没有加斜杠会报错

print(-9 % 4)  # -9-4*（-3）
print(9 % -4)  # -9-（-4）*（-3）

a = 10
c = a
b = 10
print(a == b)  # True说明a与b的值value是相等的
print(c is b)  # True说明a与b的id标识是相等的
r = range(10)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]默认从0开始，默认相差1
print(r)  # range(0,10)
print(list(r))  # list用于查看range对象中的整数序列    list是列表的意思

for item in 'python':
    print(item)

# 计算1-100之间的偶数和
sum = 0
for i in range(1, 101):
    if not bool(i % 2):  # 可以这样写
        sum += i
print(sum)

# 输出100-999之间的水仙花数
for item in range(100, 1000):
    if (item % 10) ** 3 + (item // 10 % 10) ** 3 + (item // 100) ** 3 == item:
        # 注意：在python中，整除是// 双斜杠
        print(item)
"""从键盘中录入密码，最多录入3次，如果正确就结束循环"""
# for item in range(3):
#     pwd = input("请输入密码：")
#     if pwd == '8888':
#         print("密码正确！")
#         break
#     else:
#         print("密码错误！请重新输入")
# #for-else
# for item in range(3):
#     pwd = input("请输入密码：")
#     if pwd == '8888':
#         print("密码正确！")
#         break
#     else:
#         print("密码错误！请重新输入")
# else:
#     print("对不起，三次密码均输入错误！")

# break
for i in range(5):
    for j in range(1, 11):
        if j % 2 == 0:
            break
        print(j)

# continue
for i in range(5):
    for j in range(1, 11):
        if j % 2 == 0:
            continue
        print(j, end='\t')  # 不换行
    print()  # 换行

"""
正数索引：    0       1     2
          ['hello','world',98]
负数索引：    -3      -2    -1
"""
lst = ['hello', 'world', 98]
print(lst[0], lst[-3])

# 列表切片操作
lst = [10, 20, 30, 40, 50, 60, 70, 80]
print('————————————step步长为正数的情况————————————')
print(lst[1:6:1])  # 不包含6
print(lst[1:6])  # 默认步长为1
print(lst[1:6:])
print(lst[1:6:2])
print(lst[:6:2])  # start默认从0开始
print(lst[1::2])  # stop默认到结束
print('————————————step步长为负数的情况————————————')
print('原列表：', lst)
print(lst[::-1])  # 反向输出原列表
print(lst[7::-1])  # 默认包括0
print(lst[6:0:-2])  # 不包括0，包括6

lst = [12, 86, 32, 7, 36]
print('排序前的列表：', lst, id(lst))
lst.sort()  # 默认升序
print('排序后的列表：', lst, id(lst))  # 不产生新的列表对象
lst.sort(reverse=True)  # 降序
print('排序后的列表：', lst, id(lst))

lst = [12, 86, 32, 7, 36]
print('原列表：', lst)
# 会产生一个新的列表对象
new_list = sorted(lst)
print(lst, id(lst))
print(new_list, id(new_list))
# 指定关键书参数，实现列表元素的降序排序
desc_list = sorted(lst, reverse=True)
print(desc_list, id(desc_list))

# 字典
scores = {'张三': 100, '李四': 98, '王五': 45}
print(scores)
print(type(scores))
student = dict(name='jack', age=20)
print(student)
scores = {'张三': 100, '李四': 98, '王五': 45}
print(scores['张三'])
# print(scores['陈六'])    #输入不存在的键，会报 KeyError: '陈六'
print(scores.get('张三'))
print(scores.get('陈六'))  # 输入不存在的键，不会报错，会输出None   注意与[]区别
print(scores.get('麻七', 99))  # 这个99是在用get函数查找‘麻七’所对应的value不存在时，提供的一个默认值
scores = {'张三': 100, '李四': 98, '王五': 45}
print('张三' in scores)
print('张三' not in scores)

# 获取所有的key
scores = {'张三': 100, '李四': 98, '王五': 45}
keys = scores.keys()
print(keys)
print(type(keys))
print(list(keys))  # 将所有key组成的视图转成列表
# 获取所有的value
values = scores.values()
print(values)
print(type(values))
print(list(values))  # 将所有value组成的视图转成列表
# 获取所有的key-value对
items = scores.items()
print(items)
print(type(items))
print(list(items))  # 转换之后的列表元素是由元组组成
d = {'name': '张三', 'name': '李四'}
print(d)  # 键不允许重复，会出现覆盖的情况

d = {'name': '张三', 'nikename': '张三'}
print(d)  # 值允许重复

items = ['Fruits', 'Books', 'Other']
prices = [96, 78, 85, 100, 120]
d = {item.upper(): price
     for item, price in zip(items, prices)}  # upper（）函数是转换为大写字母的函数
print(d)  # 若两个列表长度不同，则以长度短的那个为准

# 元组
# 当元组只有一个元素时，要加小括号（）和逗号，
t = ("hello",)  # 如果元组中只有一个元素，逗号不能省
print(t)
print(type(t))
t = (10, [20, 30], 9)
# 尝试将t[1]改为100
# t[1] = 100  #会报错，元素是不允许修改元素的
# 由于[20,30]是列表，而列表是可变序列，所以可以向列表中添加元素，而列表的内存地址不变
print(id(t))
print(id(t[1]))
t[1].append(100)
print(t[1])
print(id(t[1]))
print(t)
print(id(t))
# 元组遍历
t = ('hello', 'world', 98)
for item in t:
    print(item)

# 集合
"""
集合与列表、字典一样都是可变序列
集合是没有值value的字典
无序不可重复
"""
s = {2, 3, 4, 5, 5, 6, 7, 7}  # 集合不允许重复，它会把重复的元素去掉
print(s, type(s))

s4 = set({15, 22, 74, 25, 25, 6, 6})  # 将集合转换为集合
print(s4, type(s4))
s5 = set('python')  # 集合元素是无序的
print(s5, type(s5))
s7 = set()  # 使用ste方法，这样才可以定义一个空集合
print(s7, type(s7))
# 调用add（）方法，一次添加一个元素
print(s)
s.add(80)
print(s)  # 无序的添加到集合中
# 调用update（）方法，至少添加一个元素(可添加多个元素）
print(s)
s.update([45, 23, 89])
print(s)
# 调用remove（）方法，一次删除一个指定元素，如果指定的元素不存在抛出KeyError
print(s)
s.remove(45)
print(s)
# s.remove(100)  #不存在100，抛出异常 KeyError: 100
# 一个集合是否是另一个集合的子集
s1 = {10, 20, 30, 40, 50, 60}
s2 = {10, 20, 30}
s3 = {10, 20, 90}
print(s2.issubset(s1))  # 意思是s2是s1的子集吗
print(s3.issubset(s1))
# 一个集合是否是另一个集合的超集
# 如果B是A的子集，那么A就是B的超集
s1 = {10, 20, 30, 40, 50, 60}
s2 = {10, 20, 30}
s3 = {10, 20, 90}
print(s1.issuperset(s2))  # 意思是s1是s2的超集吗
print(s1.issuperset(s3))
# 两个集合是否没有交集
# 可以调用isdisjoint判断
print(s2.isdisjoint(s3))  # False 不是没有交集，那就是有交集
s4 = {100, 200, 300}
print(s2.isdisjoint(s4))  # True 是没有交集，那就是没有交集
# 方法一：内置函数intersection
print(s1.intersection(s2))
# 方法二：&符号
print(s1 & s2)

# 字符串查询
print("字符串查询********")
s = 'hello,hello'
print(s.index('lo'))
print(s.rindex('lo'))
print(s.find('lo'))
print(s.rfind('lo'))
# print(s.index('k'))   #报错
print(s.find('k'))  # 不会报错#因此建议用find（）或者rfind（）来查找
print("字符串调整大小写********")
s = "hello,python"
a = s.upper()
print(s, id(s))  # 原来的s是不会改变的
print(a, id(a))  # 字符串是不可变序列，转换成大写之后会产生一个新的字符串对象
b = s.lower()
print(s, id(s))
print(b, id(b))  # 转换之后，会产生一个新的字符串对象 虽然转换为小写之后，字符串的内容是一样的
s = "hEllo Python"
print(s, s.swapcase())
print(s, s.capitalize())
print(s, s.title())
print("字符串内容对齐********")
# center（） 居中对齐，第一个参数指定宽度，第二个参数指定填充符，第二个参数默认是空格，如果设置的宽度小于字符串实际宽度，则返回原字符串
s = "hello,python"
print(s.center(20, '*'))
print(s.center(20))
print(s.upper().ljust(20, "$"))
print(s.ljust(20))
print(s.rjust(20, "*"))
print(s.zfill(20))
print("字符串切片************")
s = "hello world python"
lst = s.split()
print(lst)
s1 = "hello|world|python"
print(s1.split(sep='|'))
print(s1.split(sep='|', maxsplit=1))  # 分出一段后，剩余的子串为一段
print(s.rsplit())
print(s1.rsplit(sep='|'))
print(s1.rsplit(sep='|',maxsplit=1))   #只有这一句的结果有所不同，从右开始劈分，最大劈分次数为1
#isidentifier()判断指定的字符串是不是合法的标识符（只由数字、字母、下划线组成）
s = 'hello,world'
print('1',s.isidentifier())   #,不是
print('2','hello'.isidentifier())
print('3','张三_'.isidentifier())
print('4','张三_123'.isidentifier())
print('5','\t'.isspace())
print('6','abc'.isalpha())
print('7','张三'.isalpha())   #True
print("字符串替换与合并")
s = "hello,python"
print(s.replace('python','java'))
s1 = "hello,python,python,python"
print(s1.replace('python','java',2))
#将列表或元组中的字符串合并成一个字符串
lst = ['hello','python','java']
print('|'.join(lst))
print(''.join(lst))
t = ('hello','python','java')
print(''.join(t))
print('*'.join('python'))
print("字符串比较操作")
 # ==比较的是value是否相等
# is比较的是id是否相等
a = b = 'python'
c = 'python'
print(a==b)
print(a==c)
print(a is b)
print(a is c)
print("格式化字符串")
name = '张三'
age = 24
print("我叫%s,今年%d岁" % (name,age))
print("我叫{0},今年{1}岁".format(name,age))
print(f"我叫{name},今年{age}岁")
#对于%
print("%10d" % 99)    #这个10表示的是宽度
print("%.3f" % 3.1415926)   #.3表示小数点后三位
#可以同时表示宽度和精度
print("%10.3f" % 3.1415946)   #一共总宽度为10，保留小数点后三位
s = '天涯共此时'
#编码
print(s.encode(encoding='GBK'))  #在GBK这种编码格式中，一个中文占两个字节
print(s.encode(encoding='utf-8'))  #在utf-8这种编码格式中，一个中文占三个字节
#解码
#byte代表就是一个二进制数据（字节类型的数据）
byte = s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))    #GBK的只能用GBK去解
#print(byte.decode(encoding='utf-8'))   #会报错，因为GBK的只能用GBK去解

print("函数".center(20,"*"))
def calc(a,b):   #a,b称为形式参数，简称形参，形参的位置是在函数的定义处
    c = a+b
    return c
result = calc(10,20)   #10,20称为实际参数的值，简称实参，实参的位置是函数的调用处
print(result)
#位置实参
#对应的位置互相传（一个萝卜一个坑），如上面的实参第一个位置的10传给形参第一个位置的a
#关键字实参
res = calc(b=10,a=20)  #使用了关键字参数，就会到定义处找到关键字名字相同的去赋值
print(res)
def fun(arg1,arg2):
    print("arg1",arg1)
    print("arg2",arg2)
    arg1 = 100
    arg2.append(10)
    print("arg1", arg1)
    print("arg2", arg2)

n1 = 11
n2 = [20,30,40]
print('n1',n1)
print('n2',n2)
fun(n1,n2)
print('n1',n1)
print('n2',n2)
#在函数调用过程中，进行参数的传递
#如果是不可变对象，在函数体的修改不会影响实参的值   arg1修改为100，不会影响n1的值 （整数是不可变对象）
#如果是可变对象，在函数体的修改会影响到实参的值   arg2的修改 append（10），会影响到n2的值  （列表是可变对象）

#如果函数的返回值有多个，返回的结果为元组
def fun1():
    return 'hello','world'
print(fun1())    #输出('hello', 'world') 为元组类型

#函数定义时，给形参设置默认值，只有与默认值不符的时候才需要传递实参
def fun(a,b=10):  #b称为默认值参数
    a,b=2,3
    print(a,b)
fun(100)
fun(20,30)

#当不知道要传递几个参数时
#可以在形参处写 *args     结果是一个元组
def fun(*args):   #函数定义时的 个数可变的位置参数
    print(args)   #输出时是一个元组
fun(10)
fun(10,20)
fun(10,20,30)
def fun1(**args):    #个数可变的关键字形参————加2个*
    print(args)     #输出时是一个字典
fun1(a=10)
fun1(a=10,b=20)
fun1(a=10,b=20,c=30)

def fun4(*args1,**args2):
    print(args1,args2)   #不会报错

fun4(10,20,a=55)
#fun4(m=6,a=55,56,20)   #会报错
#fun4(6,a=55,56,20)   #会报错
def fun(a,b,c):
    print("a=",a)
    print("b=",b)
    print("c=",c)

#函数的调用
fun(10,20,30)    #位置传参（对应位置传递参数）
lst = [11,22,33]
#fun(lst)    #会报错
fun(*lst)    #在函数调用时，将列表中的每一个元素都转换为位置实参传入
fun(a=100,b=200,c=300)   #关键字参数传入
dict = {'a':54,'b':45,'c':18}
fun(**dict)    #注意，实参是字典时，前面加两颗*
#使用递归计算阶层
def fac(a):
    if a==1:      #出口
        return 1
    else:
        res = a*fac(a-1)
        return res
print(fac(6))

print("python异常处理方式".center(17,"*"))
# try:
#     a = int(input('请输入一个整数：'))
#     b = int(input('请输入另一个整数：'))
#     result = a / b
# except BaseException as e:
#     print("出错了", e)
# else:
#     print("结果为：", result)
# finally:
#     print("谢谢您的使用！")
# print("程序结束！")

print("python类".center(20,"*"))
#一个模板
class Student:    #Student为类的名称（类名），由一个或多个单词组成，每个单词的首字母大写，其余小写
    native_pace = '福建'    #直接写在类里的变量，称为类属性

    #初始化方法
    def __init__(self,name,age):
        self.name = name     #self.name是实例属性，进行了一个赋值操作，将局部变量name的值赋给了实例属性
        self.age = age

    # 实例方法，在类之内定义的称为方法，在类之外定义的称为函数
    def eat(self):
        print("学生在吃饭...")

    #静态方法
    @staticmethod
    def method():   #静态方法中，括号里不能加self
        print("我使用了staticmethod进行修饰，所以我是静态方法")

    #类方法
    @classmethod
    def cm(cls):
        print("我是类方法，因为我使用了classmethod方法进行了修饰")
#在类之内定义的称为方法，在类之外定义的称为函数
def drink():
    print('喝水')   #这叫做函数


class Car:
    def __init__(self,brand):
        #属性前加 __ 属性不能在类对象外部访问
        self.__brand = brand
    def start(self):
        print(self.__brand+"汽车已启动...")

print("类面向对象三大特征：封装 继承 多态".center(20,"*"))

class Person():
    def __init__(self,height,sex,age,name):
        self.height=height
        self.sex=sex
        self.__age=age
        self.name=name
    def info(self):
        print(self.height,self.sex,self.__age)
    def work(self):
        print(self.name,"can work")

class Teacher(Person):
    def __init__(self, height, sex, age, name,salary):
        super().__init__(height, sex, age, name)
        self.salary=salary

    def work(self,salary):
        # super().work()
        print("{0} can work,make {1} one month ".format(self.name,self.salary))


class A(object):
    pass
class B(object):
    pass
class C(A,B):     #C继承了A和B 可以多继承
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #两个对象相加__add__
    def __add__(self, other):
        return self.name+other.name









if __name__ == '__main__':
    student=Student(1,2)
    student.eat()
    print(student.name,student.age)
    print(id(student))
    print(type(student))
    print(Student.method())
    car = Car("宝马X5")
    car.start()
    # print(car.__brand) #在类的外部无法使用
    print(car._Car__brand)#用不用全靠程序员的自觉性

    per=Person(176,'女',24,'yang')
    teach=Teacher(176,'女',24,'li',"10000")
    per.work()
    teach.work("10000")
    print(dir(Car)) #输出从object继承过来属性
    x = C('Jack', 20)
    print(x.__dict__)  # 输出实例对象的属性字典
    print(C.__dict__)
    print(x.__class__)      #输出对象所属的类    <class '__main__.C'>
    print(C.__bases__)    #C类的父类类型的元素
    print(C.__base__)    #类的基类（谁写在前面，就输出谁）
    print(C.__mro__)   #输出类的层次结构
    print(A.__subclasses__())   #查看A的子类
    y=C("Rose",19)
    z=x+y
    print(z)

