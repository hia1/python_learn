# -- coding: utf-8 --
import xlrd

excelFile=r'F:\pythonLearn\com\yang\practice100\requests_practice\casedemo01.xls'
xlBook =xlrd.open_workbook(excelFile)
# 获取excel工作簿数
sheet_counts=len(xlBook.sheets())
print(u"工作簿数为:  ", sheet_counts)
#获取表的行列数
table = xlBook.sheets()[0]
nrows = table.nrows
ncols = table.ncols
print(u"表数据行列为(%d, %d)" % (nrows, ncols))
# 循环读取数据
for i in range(0,nrows):
    rowValues = table.row_values(i)  # 按行读取数据
    # 输出读取的数据
    for data in rowValues:
        print(data,'')
    print('')

# 获取一行或一列的值，参数是第几行
print(table.row_values(0)) # 获取第一行值
print(table.col_values(0)) # 获取第一行值