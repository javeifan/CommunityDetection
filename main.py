

import pandas as pd
import numpy as np

def process(): #处理过程
    df_AI = pd.read_excel("AIW.xlsx")#读入 AIW.xlsx
    df_ATTA = pd.read_excel("ATTA.xlsx")#读入 ATTA.xlsx
    for i in df_AI.index:
        print(i)
        author = df_AI.iloc[i,0] #选取作者列
        innov = df_AI.iloc[i,1] #选取创新列
        #找出 有作者是author 并且 标题或摘要中有该创新词 的 文章 ↓ case = False 大小写不敏感 na = False 无视空行
        df_thisAuthor =  df_ATTA[df_ATTA['Authors'].str.contains(author, case=False, na=False)]
        partResult = df_thisAuthor[(df_thisAuthor['Title'].str.contains(innov,case= False,na=False) | df_thisAuthor['Abstract'].str.contains(innov,case = False,na = False))]
        for j in partResult.index:
            year = partResult['Publication Year'][j]
            num = df_AI[year][i]
            if num != num:
                df_AI[year][i] = 1
            else:
                df_AI[year] += 1;
    with pd.ExcelWriter('Result.xlsx') as writer:
        df_AI.to_excel(writer)
    return

process()#执行