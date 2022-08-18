# -- coding: utf-8 --
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#读取CSV文件
df = pd.read_csv(r"F:\tianchi\人口普查收入数据集（UCI）\income_census_train.csv")
# print(df)

def analysis_series(series):
    data_s = df[series]
    # 判断是否有异常值
    if len(data_s[data_s.isnull()])!=0:
        #删除空值,any表示有一个地方为空就删除
        data_s=data_s.dropna(axis=0,how="any")
    else:
        # print(data_s)
        print(series+"_平均值",data_s.mean())
        print(series+"_方差",data_s.std())
        print(series+"_中位数",data_s.median())
        print(series+"_最大值",data_s.max())
        print(series+"_最小值",data_s.min())
        print(series+"_偏度",data_s.skew())
        print(series+"_峰度",data_s.kurt())

    print(len(data_s))
def quantitle(series,k):
    data_s = df[series]
    #四分位数分析
    # print("__________________数据过滤")
    print("__________________数据过滤前",len(data_s))
    q_low=data_s.quantile(q=0.25)
    q_high=data_s.quantile(q=0.75)
    q_interval=q_high-q_low
    data_s=data_s[data_s<q_high+k*q_interval][data_s>q_low-k*q_interval]
    print("__________________数据过滤后", len(data_s))
    #不同区间值的分布,bins也可以赋值一个整数
    data_s_his=np.histogram(data_s.values,bins=np.arange(data_s.min(),data_s.max(),data_s.std()))
    print(data_s_his)
    #出现次数
    value_count=data_s.value_counts().sort_index()
    print(value_count)
    #出现比率
    value_count=data_s.value_counts(normalize=True).sort_index()
    print(value_count)




analysis_series("age")
analysis_series("fnlwgt")
quantitle("age",1.5)
quantitle("fnlwgt",1.5)
#groupby，按字段分组
def groupyby(series):
    data_groupby=df.groupby(series)
    print("按%s分组_平均值"%series)
    print(data_groupby.mean())
    print("按%s分组_中位数"%series)
    print(data_groupby.median())
groupyby("race")
groupyby("occupation")
#loc切片可以获取指定字段数据
work_race=df.loc[:,["occupation","race"]].value_counts().sort_index()
# print(work_race)
#想获取什么工作赚钱多
work_salary=df.loc[:,["workclass","capital_gain"]].groupby("workclass").mean()
print(work_salary)


plt.bar(np.arange(len(df["fnlwgt"].value_counts())),df["fnlwgt"].value_counts())
plt.show()