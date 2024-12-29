import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import datetime as dt
import tushare as ts
plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus']=False
ts.set_token("e3956f941d9ee613075ff03d85b50499687b6a646e7337e493dcf657")
pro=ts.pro_api()
df_sz = pro.daily(ts_code='000001.SZ', start_date='19901220', end_date='20211231')
df_sh = pro.daily(ts_code='000001_SH', start_date='19901220', end_date='20211231')
print(df_sz)
df_sz.to_csv("SH_SZ.csv",index=False,float_format='%.2f')
#df_sh.to_csv("SH_SZ.csv",mode='a',header=False,float_format='%.2f')

#读取通过tushare库获取的股票数据，以及数据的基础信息，如占用内存和数据类型
data=pd.read_csv("SH_SZ.csv")
data.info()
#trade_date()列是object类型，因此需要转化为datetime类型
data['trade_date']=pd.to_datetime(data.trade_date)
print("................")
print(data['trade_date'].dtype)
#展示数据的前五行
data.head()
