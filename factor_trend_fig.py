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
#进一步提取2015年各月的开盘价均值，收盘价均值，最高最高价，最低最低价以及每月成交量总数进行统计分析
sh_2015=data[(data.trade_date.dt.year==2015)&(data.ts_code=='000001.SZ')]
sh_2015.set_index(sh_2015.trade_date,inplace=True)
sh_2015_M=sh_2015.resample('ME').agg({'open':lambda x:np.mean(x),
                                      'close':lambda y:np.mean(y),
                                      'high':lambda z:np.max(z),
                                      'low':lambda m:np.min(m),
                                      'vol':lambda n:np.sum(n)})
#000001.SZ月交易量走势图绘制
fig=plt.figure(figsize=(12,5))
axes1=fig.add_subplot(1,2,1)
axes2=fig.add_subplot(1,2,2)
sns.lineplot(data=sh_2015_M['vol'],ax=axes1)
plt.title("2015年上证指数月交易量走势图")
sns.lineplot(data=sh_2015_M[['open','close','high','low']],ax=axes2)
plt.title("2015年上证指数开盘价，收盘价，最高价，最低价走势图")
plt.show()