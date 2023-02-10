# 预处理程序 使用numpy和pandas对一维、二维表进行处理
import numpy as np
import pandas as pd

DF_AIW = pd.read_excel('AIW-test.xlsx')#DataFrame of Author-Innovation-Weight
DF_ATTA = pd.read_excel("ATTA-test.xlsx")#DataFrame of Author-Title-Time-Abstract
DF_AI = DF_AIW[['Author','Innov'][0:10]]#截取一部分拿来试验 拿几百条出来试验 我把中文列名都改成英文了 我怕出错
for i in range(0, len(DF_AI), 1):
    print(DF_AI['Author'][i],end=',')
    print(DF_AI['Innov'][i])
    print(i)

