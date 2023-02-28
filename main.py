

import pandas as pd

def process(): #处理过程
    df_AI = pd.read_excel("AIW.xlsx").iloc[:10]#读入 AIW.xlsx
    df_ATTA = pd.read_excel("ATTA.xlsx")#读入 ATTA.xlsx
    for i in df_AI.index:
        author = df_AI.iloc[i,0] #选取作者列
        innov = df_AI.iloc[i,1] #选取创新列
        #找出 有作者是author 并且 标题或摘要中有该创新词 的 文章 ↓ case = False 大小写不敏感 na = False 无视空行
        partResult = df_ATTA[df_ATTA['Authors'].str.contains(author,case = False,na = False) & (df_ATTA['Title'].str.contains(innov,case= False,na=False) | df_ATTA['Abstract'].str.contains(innov,case = False,na = False))]
        for j in partResult.index:
            year = partResult['Publication Year'][j]
            num = df_AI[year][i]
            if num == "":
                df_AI[year][i] = 1
            else:
                df_AI[year] += 1;
        print("index : "+i)
    return
    df_AI.to_excel('Result.xlsx')
process()#执行