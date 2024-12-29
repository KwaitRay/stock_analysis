import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import datetime as dt
import tushare as ts
import matplotlib.dates as mdates
plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus']=False
data=pd.read_csv("stocks.csv")
#trade_date()列是object类型，因此需要转化为datetime类型,否则绘图x轴会出问题
data['trade_date']=pd.to_datetime(data['trade_date'],format="%Y%m%d")

#收益分析
def simple_return_daily(series):
    #计算绝对日收益率
    s = (series-series.shift(1))/series.shift(1)
    return s

def long_return_daily(series):
    #计算对数日收益率
    s = np.log(series/series.shift(1))
    return s

data['simple_return_daily']=data.groupby('ts_code')['close'].transform(simple_return_daily)
data['long_return_daily']=data.groupby('ts_code')['close'].transform(long_return_daily)

data['trade_date']=pd.to_datetime(data.trade_date)
#初始化绘图
plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus']=False
fig=plt.figure(figsize=(12,5))
axes1=fig.add_subplot(1,2,1)
axes2=fig.add_subplot(1,2,2)
# 格式化x轴，只显示年份
date_format = mdates.DateFormatter('%Y')
axes1.xaxis.set_major_formatter(date_format)
axes2.xaxis.set_major_formatter(date_format)
# 自动调整x轴标签的显示
fig.autofmt_xdate()
#初始化平均年化收益率数据
return_yearly=[]
stocks={'平安银行':'000001.SZ','万科A':'000002.SZ','国农科技':'000004.SZ','世纪星源':'000005.SZ'}
for stock_code in stocks.values():
    stock_data=data[data.ts_code==stock_code][['trade_date','ts_code','simple_return_daily','long_return_daily']]
    #计算股票的累计日收益率,并在stock_data表中新建一列accumulate来存放，cumprod表示累积，dropna去除NAN值
    stock_data['accumulate']=(stock_data['simple_return_daily']+1).cumprod().dropna()
    #计算股票的年化收益率,注意公式np.mean()
    return_yearly.append((1+np.mean(stock_data['long_return_daily']))**252-1)
    #seaborn绘图
    axes1.set_title('2021年股票%s的累计日收益率图' %stock_code)
    sns.lineplot(data=stock_data,x='trade_date',y='accumulate',ax=axes1)
#axes1.legend(title='股票名',bbox_to_anchor=(1.02,1),loc='upper left')
#初始化平均年收益dataframe，并按照return_yearly数值进行排序，用于之后进行绘图
stocks_yearly=pd.DataFrame(columns=['code','return_yearly'])
stocks_yearly['code']=stocks.values()
stocks_yearly['return_yearly']=return_yearly
stocks_yearly.sort_values('return_yearly',inplace=True)
#按照不同公司代码，绘制平均年收益条形图,barplot
axes2.set_title('选定股票平均年化收益率图')
sns.barplot(data=stocks_yearly,x='code',y='return_yearly',ax=axes2)
plt.show()

#风险分析
def MeanDevition(series):
    #平均差计算
    d = np.abs(series-series.mean()).mean()
    return d
def MaxMinDevition(series):
    #极差计算
    d = series.max()-series.min()
    return d
def QuantileDevition(series):
    #四分位距计算
    d = series.quantile(0.75)-series.quantile(0.25)
    return d
def VariationCoef(series):
    #离散系数计算
    d = series.std()/series.mean()
    return d
def Skewness(series):
    #偏度计算
    return series.skew()
def Kurtosis(series):
    #峰度计算
    return series.kurt()

risk_data=data.groupby('ts_code')['long_return_daily'].agg([np.mean,np.std,np.var,MeanDevition,MaxMinDevition,QuantileDevition,VariationCoef,Skewness,Kurtosis])
print(risk_data)