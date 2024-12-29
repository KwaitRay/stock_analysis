# 一.项目简介
  本项目主要利用python进行数据分析以及可视化，包括利用tushare库获取特定股票数据，利用pandas进行股票数据读取以及numpy进行股票相关指数分析，利用seaborn库以及matplotlib库进行可视化，最终利用折线图以及条形图等形式直观的表现对应股票的收益率以及风险分析结果
此项目包含以下文件
- [stock_analysis.py](stock_analysis.py)
- [trend_analysis.py](trend_analysis.py)
- [factor_trend_fig.py](factor_trend_fig.py)
- [Individual_stock_analysis.py](Individual_stock_analysis.py)
- [Individual_stock_analysis1.py](Individual_stock_analysis.py)
- [SH_SZ.csv](SH_SZ.csv)
- [stocks.csv](stocks.csv)
  其中，前三个文件是对000001.SZ(即平安银行)进行交易量走势图，开盘价，收盘价，最高价，最低价走势图进行分析绘制，SH_SZ.csv是利用tushare获取的交易数据,四五两个文件是选取了['平安银行':'000001.SZ','万科A':'000002.SZ','国农科技':'000004.SZ','世纪星源':'000005.SZ']等四支股票进行收益率以及风险分析的结果，并绘制了相应图表
# 二.项目实现
## 1.技术栈以及相关库
### （1）tushare库
tushare能够为用户方便快捷的获取大量可以用于金融分析的数据，数据内容将扩大到包含股票、基金、期货、债券、外汇、行业大数据，同时包括了数字货币行情等区块链数据的全数据品类的金融大数据平台，为各类金融投资和研究人员提供适用的数据和工具。
### （2）pandas库
### （3）numpy库
### （4）seaborn库
seaborn库是基于matplotlib库开发的高级数据可视化库，可以直接读取pandas数据框（DataFrame）,避免了matplotlib需要进行解包数据列等复杂操作，因此可以快速便捷的生成美观的统计图表，容易上手
### （5）matplotlib库
