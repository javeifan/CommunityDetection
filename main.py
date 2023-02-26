

import pandas as pd


df_AI = pd.read_excel("AIW.xlsx");
df_AI_str = pd.read_excel("AIW.xlsx").iloc[25, 0]  # 第26行 第2列 这是一个str
df_ATTA = pd.read_excel("ATTA.xlsx")
# print(df[df['Author'].str.contains('A')][['Author','Innovation']])
#print(df_AI_str)
df_result = df_ATTA[df_ATTA['Authors'].str.contains(df_AI_str,na = False)]  # Notice contains should ignore na
df_result.to_excel('testR.xlsx')#也可以用流

def process(): #处理过程
    df_AI = pd.read_excel("AIW.xlsx").iloc[:10,0]#读入 AIW.xlsx
    df_ATTA = pd.read_excel("ATTA.xlsx")#读入 ATTA.xlsx
    for i in range(0,len(df_AI),1):
        author = df_AI.iloc[i,0] #选取作者列
        innov = df_AI.iloc[i,1] #选取创新列
        #找出 有作者是author 并且 标题或摘要中有该创新词 的 文章 ↓
        partResult = df_ATTA[df_ATTA['Author'].str.contains(author) & (df_ATTA['Title'].str.contains(innov) | df_ATTA['Abstract'].str.contains(innov))]
    return


process()#执行