# -- coding: utf-8 --


# 已知一个字符串为 “hello_world_yoyo”, 如何得到一个队列 [“hello”,”world”,”yoyo”]
import logging
import random
from functools import reduce
import numpy as np

def test0():
    test = 'hello_world_yoyo'
    print(test.split("_"))
    # 有个列表 [“hello”, “world”, “yoyo”]如何把把列表里面的字符串联起来，得到字符串 “hello_world_yoyo”
    test = ["hello", "world", "yoyo"]
    print("_".join(test))
    # 把字符串 s 中的每个空格替换成”%20”
    # 输入：s = “We are happy.”
    # 输出：”We%20are%20happy.”

    s = 'We are happy.'
    print(s.replace(" ", "20%"))

    # 打印99乘法表
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("{}x{}={}".format(j, i, i * j), end=" ")
        print()

    i = 1
    while i <= 9:
        j = 1
        while j <= i:
            print("{}x{}={}".format(j, i, i * j), end=" ")
            j += 1
        print()
        i += 1

    # 找出单词 “welcome” 在 字符串”Hello, welcome to my world.” 中出现的位置，找不到返回-1
    # 从下标0开始索引
    test = "Hello, welcome to my  world."
    s = test.find("welcome")
    print(s)
    count = 0
    for i in range(0, len(test) + 1):
        if test.find("w", i, i + 1) > 0:
            count += 1
    print(count)
# test0()


'''题目:输入一个字符串str, 输出第m个只出现过n次的字符，如在字符串 gbgkkdehh 中,
找出第2个只出现1 次的字符，输出结果：d'''


def test01(str_test, num, counts):
    """
    :param str_test: 字符串
    :param num: 字符串出现的次数
    :param count: 字符串第几次出现的次数
    :return:
    """
    # 定义一个空数组，存放逻辑处理后的数据
    list = []
    # for循环字符串的数据
    for i in str_test:
        # 使用 count 函数，统计出所有字符串出现的次数
        count = str_test.count(i, 0, len(str_test))
        # 判断字符串出现的次数与设置的counts的次数相同，则将数据存放在list数组中
        if count == num:
            list.append(i)
    # 返回第n次出现的字符串
    return list[counts - 1]
# print(test01('gbgkkdehh', 1, 2))


'''判断字符串a=”welcome to my world” 是否包含单词b=”world”
包含返回True，不包含返回 False'''


def test02(a, b):
    if b in a:
        return True
    else:
        return False
# print(test02("welcome to my world","world"))


'''输出指定字符串A在字符串B中第一次出现的位置,如果B中不包含A,则输出-1
从 0 开始计数
A = “hello”
B = “hi how are you hello world, hello yoyo !”'''


def test03(a, b):
    if a in b:
        return b.find(a)
    return -1
# print(test03("hello","hi how are you hello world, hello yoyo !"))


'''输出指定字符串A在字符串B中最后出现的位置,如果B中不包含A, 输出-1从 0 开始计数
A = “hello”
B = “hi how are you hello world, hello yoyo !”'''


def test04(a, b):
    if a in b:
        return b.rfind(a)
    return -1
# print(test04("hello","hi how are you hello world, hello yoyo !"))


'''
给定一个数a，判断一个数字是否为奇数或偶数
a1 = 13
a2 = 10
'''


def test05(a):
    if type(a) is int:
        if a % 2 == 0:
            print("偶数")
        else:
            print("奇数")
    else:
        print("非整数")
# test05(0.8)


'''
输入一个姓名，判断是否姓王
a = “王五”
b = “老王”
'''


def test06():
    while True:
        try:
            str01 = input("请输入姓名")
        except ValueError:
            print("error type")
            continue
        if "王" in str01:
            if str01.find("王") == 0:
                print("pass")
            else:
                print("非王姓")
            break
# test06()


'''如何判断一个字符串是不是纯数字组成
a = “123456”
b = “yoyo123”'''


def test07(a):
    if a.isdecimal():
        print("pass")
    else:
        print("error")
# test07("12345A")


def test08(a, b):
    print(a, a.upper())
    print(b, b.lower())

# test08("This is string example….wow!",'Welcome To My World')


'''将字符串 a = “ welcome to my world “首尾空格去掉'''
a = " welcome to my world "
# print(a.strip())


def trim(s):
    flag = 0
    if s[:1] == ' ':
        s = s[1:]
        flag = 1
    if s[-1:] == ' ':
        s = s[:-1]
        flag = 1
    if flag == 1:
        return trim(s)
    else:
        return s
# print(trim('  Hello world!  '))


'''s = “ajldjlajfdljfddd”，去重并从小到大排序输出”adfjl”'''


def test09(s):
    str_list = []
    for i in s:
        if i in str_list:
            str_list.remove(i)
        str_list.append(i)
    str_list.sort(reverse=False)
    print(str_list)
    return "".join(str_list)

# print(test09("jldjlajfdljfddd"))


"""题目 打印出如下图案（菱形）:"""


def test10():
    n = 8
    for i in range(-int(n / 2), int(n / 2) + 1):
        # print(abs(i),abs(n-abs(i)*2))
        print(" " * abs(i), "*" * abs(n - abs(i) * 2))
    m = 7
    for i in range(-int(m // 2), int(m // 2) + 1):
        # print(abs(i), abs(n - abs(i) * 2))
        print(" " * abs(i), "*" * (abs(n - abs(i) * 2) - 1))


# print(test10())

'''题目 给一个不多于5位的正整数，要求：
一、求它是几位数，
二、逆序打印出各位数字。
a = 12345'''


def test11():
    while True:
        try:
            int_value = int(input(("请输入正整数")))
            int_value = str(int_value)
            print("长度{}位，值为{}".format(len(int_value), int_value))
            int_list = []
            for i in int_value:
                int_list.append(int(i))
                int_list.sort()
            return print("".join('%s' % id for id in int_list))
        except ValueError:
            print("输入有误")
            continue
# test11()


'''如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。
例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数
那么问题来了，求1000以内的水仙花数（3位数）'''


def test12():
    while True:
        try:
            input_num = int(input("请输入一个1000以内三位整数"))
            if (100 < input_num and input_num < 1000):
                pass
                list_num = []
                for i in range(100, input_num):
                    if (i % 10)**3 + ((i % 100) // 10)**3 + (i // 100)**3 == i:
                        list_num.append(i)
                return print(list_num)
            else:
                print("请输入合法数字")
                continue
        except ValueError:
            print("value error")
            continue
        except BaseException as e:
            print(e)
            continue
# test12()


'''计算求1-2+3-4+5-…-100的值'''


def test13():
    m = 0
    for i in range(1, 100):
        if i % 2 == 0:
            i = -1 * i
        m = m + i
    print(m)
# test13()


'''计算公式 13 + 23 + 33 + 43 + …….+ n3
实现要求：
输入 : n = 5
输出 : 225
对应的公式 : 13 + 23 + 33 + 43 + 53 = 225'''


def test14(n):
    m = 0
    for i in range(1, n + 1):
        m = m + i**3
    print(m)
# test14(5)


'''已知 a的值为”hello”，b的值为”world”，如何交换a和b的值？
得到a的值为”world”，b的值为”hello”'''


def test15(a, b):
    s = a
    a = b
    b = s
    print(a, b)

# test15("aaa","bbb")


'''如何判断一个数组是对称数组：
要求：判断数组元素是否对称。例如[1，2，0，2，1]，[1，2，3，3，2，1]这样的都是对称数组
用Python代码判断，是对称数组打印True，不是打印False,如：
x = [1, “a”, 0, “2”, 0, “a”, 1]'''


def test16():
    x = [1, 'a', 0, '2', 1, 'a', 1]
    # 通过下标的形式，将字符串逆序进行比对
    if x == x[::-1]:
        return True
    return False
# print(test16())


'''如果有一个列表a=[1,3,5,7,11]
问题：1如何让它反转成[11,7,5,3,1]
2.取到奇数位值的数字，如[1,5,11]'''


def test17(a):
    list_trans = []
    list_trans = a[::-1]
    print(list_trans)
    list_get = []
    for i in range(0, len(a)):
        if i % 2 == 0:
            list_get.append(a[i])
    print(list_get)

# test17([1, 3, 5, 7, 11])


'''
1.对列表a 中的数字从小到大排序
a = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8]
2.L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
找出列表中最大值和最小值
3.a = [“hello”, “world”, “yoyo”, “congratulations”]
找出列表中单词最长的一个
4.a = [1, -6, 2, -5, 9, 4, 20, -3] 按列表中的数字绝对值从小到大排序
'''


def test18():
    a = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
    print("升序", sorted(a))
    print("最大值", max(a))
    print("最小值", min(a))

    word = ["hello", "world", "yoyo", "congratulations"]
    parLen = len(word[0])
    for i in word:
        if len(i) > parLen:
            parLen = i
    print(parLen)

    a = [1, -6, 2, -5, 9, 4, 20, -3]
    list1 = []
    for i in a:
        i = abs(i)
        list1.append(i)
    list2 = sorted(list1)
    s = "".join("%s" % id for id in list2)
    print(list2, s)

# test18()


'''b = [“hello”, “helloworld”, “he”, “hao”, “good”]
按list里面单词长度倒叙'''

def test19():
    b = ["hello", "helloworld", "he", "hao", "good"]
    dict_b = {}
    for i in b:
        dict_b[i] = len(i)  # 直接添加键值对
    message = sorted(dict_b.items(), key=lambda x: x[1], reverse=True)
    print(message)
    lists = []
    for j in message:
        lists.append(j[0])
    print(lists)
# test19()


'''L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
如何用一行代码得出[1, 2, 3, 5, 11, 33, 88]
将列表中的重复值取出(仅保留第一个)，要求保留原始列表顺序
如a=[3, 2, 1, 4, 2, 6, 1] 输出[3, 2, 1, 4, 6]'''


def test20():
    l1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
    print(sorted(set(l1)))
    a = [3, 2, 1, 4, 2, 6, 1]
    lista = []
    for i in a:
        if i not in lista:
            lista.append(i)
    print(lista)
# test20()


'''a = [1, 3, 5, 7]
b = [‘a’, ‘b’, ‘c’, ‘d’]
如何得到[1, 3, 5, 7, ‘a’, ‘b’, ‘c’, ‘d’]'''


def test21():
    a = [1, 3, 5, 7]
    b = ['a', 'b', 'c', 'd']
    print(a + b)
# test21()


''''
用一行代码生成一个包含 1-10 之间所有偶数的列表
列表a = [1,2,3,4,5], 计算列表成员的平方数，得到[1,4,9,16,25]
使用列表推导式，将列表中a = [1, 3, -3, 4, -2, 8, -7, 6]
找出大于0的数，重新生成一个新的列表
'''
# 列表推导式


def test22():
    print(list(i for i in range(1, 11) if i % 2 == 0))
    print(list(i**2 for i in range(1, 6)))
    a = [1, 3, -3, 4, -2, 8, -7, 6]
    print(list(i for i in a if i > 0))
# test22()


'''
统计在一个队列中的数字，有多少个正数，多少个负数，如[1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
'''


def test23():
    lists = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
    l2 = sorted(lists)
    print(l2, l2.index(0))
    print("正数%d,负数%d" % (l2.index(0), len(l2) - 1 - l2.index(0)))
    print("正数{}，负数{}".format(l2.index(0), len(l2) - 1 - l2.index(0)))


# test23()
'''
a = [“张三”,”张四”,”张五”,”王二”] 如何删除姓张的
'''


def test24():
    # 倒序循环可以解决正序循环漏掉”张四“的bug
    a = ["张三", "张四", "张五", "王二"]
    for i in range(len(a) - 1, -1, -1):
        if a[i][0] == "张":
            a.pop(i)
    print(a)
# test24()


'''
有个列表a = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8] 使用filter 函数过滤出大于0的数
'''


def test25():
    def test(a):
        return a > 0
    a = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
    newList = filter(test, a)
    print(list(newList))

    def testb(b):
        return b[0] != "张"
    b = ["张三", "张四", "张五", "王二"]
    newList = filter(testb, b)
    print(list(newList))


# test25()

'''过滤掉列表中不及格的学生
a = [
{“name”: “张三”, “score”: 66},
{“name”: “李四”, “score”: 88},
{“name”: “王五”, “score”: 90},
{“name”: “陈六”, “score”: 56},
]'''


def test26():
    a = [
        {"name": "张三", "score": 66},
        {"name": "李四", "score": 88},
        {"name": "王五", "score": 90},
        {"name": "陈六", "score": 56}
    ]
    newList=list(filter(lambda x:x.get("score")>=60,a))
    print(newList)
# test26()

'''有个列表 a = [1, 2, 3, 11, 2, 5, 88, 3, 2, 5, 33]
找出列表中最大的数，出现的位置，下标从0开始'''
def test27():
    a = [1, 2, 3, 11, 2, 5, 88, 3, 2, 5, 33]
    print(a.index(max(a)))
# test27()


'''**a = [
‘my’, ‘skills’, ‘are’, ‘poor’, ‘I’, ‘am’, ‘poor’, ‘I’,
‘need’, ‘skills’, ‘more’, ‘my’, ‘ability’, ‘are’,
‘so’, ‘poor’
]
找出列表中出现次数最多的元素
'''
def test28():
    a = [
        "my", "skills", "are", "rich", "I", "am", "rich", "I",
        "need", "skills", "more", "my", "ability", "are",
        "so", "rich"
    ]
    dict1={}
    for i in a:
        if i not in dict1:
            dict1[i]=a.count(i)

    print(dict1)
    return sorted(dict1.items(),key=lambda x:x[1],reverse=True)[0][0]

# print(test28())

'''给定一个整数数组A及它的大小n，同时给定要查找的元素val，
请返回它在数组中的位置(从0开始)，若不存在该元素，返回-1。
若该元素出现多次请返回第一个找到的位置
如 A1=[1, “aa”, 2, “bb”, “val”, 33]
或 A2 = [1, “aa”, 2, “bb”]'''
def test29(a,string):
    if string not in a:
        return -1
    else:
        for i in a:
            if i==string:
                return (a.index(string))

# print(test29([1, "aa", "val",  2, "bb", "val", 33], 'val'))



"""
给定一个整数数组nums 和一个目标值target ，请你在该数组中找出和为目标值的那两个整数，并返回他
们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
示例:
给定nums=[2，7，11，15]，target=9
因为nums[0] + nums[1] =2+7 = 9
所以返回[0， 1]
"""

def test30(nums,target):
    newlist={}
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                newlist[i]=j
    print(newlist)
num = [2, 5, 7, 15,4,0,-3,12,4,1,8,3,6]
# test30(num,9)


'''a = [[1,2],[3,4],[5,6]] 如何一句代码得到 [1, 2, 3, 4, 5, 6]'''
def test31():
    a = [[1, 2], [3, 4], [5, 6]]
    newlist=[]
    for i in a:
        newlist.extend([i[0],i[1]])
    print(newlist)
    print([j for i in a for j in i])
# test31()

'''
列表转字符串，L = [1, 2, 3, 5, 6]，如何得出 ‘12356’？
'''
def test32(oldlist):
    lists=[str(i) for i in oldlist]
    new_str="".join(lists)
    return print(new_str)
# test32([1, 2, 3, 5, 6])

'''列表组装字典 '''
def test33(a,b):
    c={a:b for a,b in zip(a,b)}
    print(c)
# test33(["a", "b", "c"],[1, 2, 3])


'''如下列表
people = [
{“name”:”yoyo”, “age”: 20},
{“name”:”admin”, “age”: 28},
{“name”:”zhangsan”, “age”: 25},
]
按年龄age从小到大排序'''

def test34():
    people = [
        {"name": "yoyo", "age": 20},
        {"name": "admin", "age": 28},
        {"name": "zhangsan", "age": 25},
    ]
    print(sorted(people, key=lambda x: x['age'], reverse=True))

# test34()

'''
现有 nums=[2, 5, 7] ，如何在该数据最后插入一个数字 9 ，如何在2后面插入数字0
如何打乱列表a的顺序,每次得到一个无序列表
输出1-100除3余1 的数，结果为tuple
'''
def test35():
    nums=[2, 5, 7]
    nums.append(9)
    print(nums)
    nums.insert(1, 0)
    print(nums)
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(a)
    print(a)
    tuples=()
    for i in range(1,101):
        if i%3==1:
            tuples+=(i,)
# test35()


'''
将(‘a’, ‘b’, ‘c’, ‘d’, ‘e’) 和 (1,2, 3, 4, 5)两个tuple转成
（1， 2， 3， 4， 5）为key, (‘a’, ‘b’, ‘c’, ‘d’, ‘e’) 为value的字典
字典转字符串；将字典里的值是数值型的转换为字符串，如a = {‘aa’: 11, ‘bb’: 222}
得到{‘aa’: ‘11’, ‘bb’: ‘222’}
'''
def test36():
    a = (1, 2, 3, 4, 5)
    b = ("a", "b", "c", "d", "e")
    d= list(zip(a, b))
    c={a:b for a,b in zip(a,b)}
    print(d)
    print(c)
    a = {'a': 11, 'bb': 222}
    str_a=str(a)
    print(str_a)
    for i in a:
        a[i]=str(a.get(i))
    print(a)
    b = {'a': 11, 'bb': 222}
    for i in b.items():
        b.update({i[0]:str(i[1])})
    print(b)
    c={'a': 11, 'bb': 222}
# test36()

'''map函数对列表a=[1,3,5],b=[2,4,6]相乘得到[2,12,30]
reduce函数计算1-100的和
两个字典合并a={“A”:1,”B”:2},b={“C”:3,”D”:4}

'''
def test37():
    a = [1, 3, 5]
    b = [2, 4, 6]
    print(list(map(lambda x,y:x*y ,a,b)))#map函数
    # reduce函数
    newlist=[]
    for i in range(0,101):
        newlist.append(i)
    print(reduce(lambda x,y:x+y,newlist))
    a = {"A": 1, "B": 2}
    b = {"C": 3, "D": 4}
    a.update(b)#字典内置update函数
    print(a)
# test37()

'''m1={‘a’:1,’b’:2,’c’:1} # 将同样的value的key集合在list里，输出{1:[‘a’,’c’],2:[‘b’]}'''
def test38():
    m1 = {"a": 1, "b": 2, "c": 1}
    newdict={}
    for key,value in m1.items():
        if value not in newdict:
            newdict[value]=[key]
        else:
            newdict[value].append(key)
    print(newdict)

# test38()


'''d = {"name": "zs", "age": 18, "city": "深圳", "tel": "1362626627"}字典根据键从小到大排序

'''

def test39():
    d = {"name": "zs", "age": 18, "city": "深圳", "tel": "1362626627"}
    newd=sorted(d.items() ,key=lambda x:x[0],reverse=False)
    newdict={}
    for i in newd:
        newdict[i[0]]=i[1]
    print(newdict)

# test39()


'''函数计算10！'''

def test40(num):
    print(reduce(lambda  x,y:x*y,  range(1,12)))
    if num==1 or num==0:
        return 1
    else:
        return num*test40(num-1)
# print(test40(11))


'''有1、2、3、4数字能组成多少互不相同无重复数的三位数?
分别打印这些三位数的组合'''
def test41():
    l = ["1", "2", "3", "4"]
    newlist=[]
    for i in range(len(l)):
        for j in range(len(l)):
            for k in range(len(l)):
                if i!=j and j!=k and i!=k:
                    # print(l[i]+l[j]+l[k])
                    newlist.append(l[i]+l[j]+l[k])
    print(newlist)
# test41()


'''在以下文本中找出 每行中长度超过3的单词:
Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick'''
def test42():
    a = '''Call me Ishmael. Some years ago - never mind how long precisely - having
    little or no money in my purse, and nothing particular to interest me
    on shore, I thought I would sail about a little and see the watery part
    of the world. It is a way I have of driving off the spleen, and regulating
    the circulation. - Moby Dick'''

    list1=[[j for j in i.split(' ') if len(j)>3 ]for i in a.split('\n')]
    print(list1)
# test42()

'''a = [11, 2, 33, 1, 5, 88, 3]
冒泡排序：
依次比较两个相邻的元素，如果顺序（如从小到大、首字母从A到Z）
错误就把他们交换过来'''
def test43():
    arr = [11, 2, 33, 1, 5, 88, 3]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    print(arr)
# test43()

'''有一个数据list of dict如下
a = [
{“yoyo1”: “123456”},
{“yoyo2”: “123456”},
{“yoyo3”: “123456”},
]
写入到本地一个txt文件，内容格式如下：
yoyo1,123456
yoyo2,123456
yoyo3,123456
'''
def test44():
    a = [
        {"yoyo1": "123456"},
        {"yoyo2": "123456"},
        {"yoyo3": "123456"},
    ]
    with open("dict.txt","w") as f:
        for i in a:
            for key,value in i.items():
                f.write("{},{}\n".format(key,value))
                print("{},{}\n".format(key,value))
# test44()


'''题目：求一个3*3矩阵主对角线元素之和。'''

def test45():
    mat = [[1, 2, 3],
           [3, 4, 5],
           [4, 5, 6]
           ]
    res=0
    for i in range(len(mat)):
        res+=mat[i][i]
    print(res)
# test45()


'''实例039：有序列表插入元素
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。'''
def test46():
    lis = [1, 10, 100, 1000, 10000, 100000]
    n=int(input("insert a number"))
    lis.append(n)
    for i in range(len(lis)-1):
        if lis[i]>=n:
            for j in range(i,len(lis)):
                lis[j],lis[-1]=lis[-1],lis[j]
            break
    print(lis)
# test46()

'''
实例040：逆序列表
题目：将一个数组逆序输出。
程序分析：依次交换位置，或者直接调用reverse方法。
'''
def test47():
    lis = [1, 10, 100, 1000, 10000, 100000]
    for i in range(int(len(lis) / 2)):
        lis[i], lis[len(lis) - 1 - i] = lis[len(lis) - 1 - i], lis[i]
    print('第一种实现：')
    print(lis)
    lis = [1, 10, 100, 1000, 10000, 100000]
    print('第二种实现：')
    lis.reverse()
    print(lis)
# test47()





x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print  ('我们的数组是：')
print (x)
print ( '\n')
# 切片
z = x[1:4,1:3]
print ( '切片之后，我们的数组变为：')
print (z)
print ( '\n')
# 对列使用高级索引
y = x[1:4,[1,2]]
print  ('对列使用高级索引来切片：')
print (y)


















