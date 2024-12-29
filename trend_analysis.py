import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
import seaborn as sns
import datetime as dt
import tushare as ts
plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus']=False
#读取通过tushare库获取的股票数据，以及数据的基础信息，如占用内存和数据类型
data=pd.read_csv("SH_SZ.csv")
data.info()
#trade_date()列是object类型，因此需要转化为datetime类型
data['trade_date']=pd.to_datetime(data['trade_date'],format="%Y%m%d")
print("................")
print(data['trade_date'].dtype)
#展示数据的前五行
data.head()
#走势分析
fig=plt.figure(figsize=(12,5))
axes1=fig.add_subplot(1,2,1)
axes2=fig.add_subplot(1,2,2)
axes1.set_title("1990-2021上证-深证指数每日收盘价走势图")
sns.lineplot(x=data.trade_date,y=data.close,hue=data.ts_code,ax=axes1)
axes2.set_title("1990-2021上证-深证指数每日成交量走势图")
sns.lineplot(x=data.trade_date,y=data.vol,hue=data.ts_code,ax=axes2)
# 格式化x轴，只显示年份
date_format = mdates.DateFormatter('%Y')
axes1.xaxis.set_major_formatter(date_format)
axes2.xaxis.set_major_formatter(date_format)

# 自动调整x轴标签的显示
fig.autofmt_xdate()
#获取000001.SZ股票中，收盘价大于40的记录，并用pd.pivot_table绘制透视表
sh_5000=data[(data.ts_code=='000001.SZ')&(data.close>40)]
print(sh_5000)
#aggfunc用于确定对特定列使用什么聚合函数
pd.pivot_table(sh_5000,index=[sh_5000.trade_date.dt.year,sh_5000.trade_date.dt.month],values=['close','vol'],aggfunc={'close':lambda x:np.mean(x),'vol':lambda x:np.sum(x)})

plt.show()
