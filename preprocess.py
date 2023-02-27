# 预处理程序 使用numpy和pandas对一维、二维表进行处理
import numpy as np
import pandas as pd

df_AI = pd.read_excel("AIW.xlsx");
author = pd.read_excel("AIW.xlsx").iloc[25, 0]  # 第26行 第2列 这是一个str
innov = pd.read_excel("AIW.xlsx").iloc[25, 1]
print(author + ";" + innov )
df_ATTA = pd.read_excel("ATTA.xlsx")
partResult = df_ATTA[df_ATTA['Authors'].str.contains(author,case = False) & (df_ATTA['Title'].str.contains(innov,case = False) | df_ATTA['Abstract'].str.contains(innov,case = False))]
print(partResult)

