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
#初始化df
df=pd.DataFrame()
#提前确定公司及其对应的股票代码
stocks={'平安银行':'000001.SZ','万科A':'000002.SZ','国农科技':'000004.SZ','世纪星源':'000005.SZ'}
for stock_code in stocks.values():
    df_stock = pro.daily(ts_code=stock_code, start_date='20210101')
    df = pd.concat([df,df_stock],ignore_index=True)
df.to_csv('stocks.csv')
df.head()
