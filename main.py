

import pandas as pd

def process(): #处理过程
    df_AI = pd.read_excel("AIW.xlsx").iloc[:10,0]#读入 AIW.xlsx
    df_ATTA = pd.read_excel("ATTA.xlsx")#读入 ATTA.xlsx
    result = pd.DataFrame()  # 存放结果 最后输出成excel 查看结果是否正确
    for i in range(0,len(df_AI),1):
        author = df_AI.iloc[i,0] #选取作者列
        innov = df_AI.iloc[i,1] #选取创新列
        #找出 有作者是author 并且 标题或摘要中有该创新词 的 文章 ↓ case = False 大小写不敏感 na = False 无视空行
        partResult = df_ATTA[df_ATTA['Author'].str.contains(author) & (df_ATTA['Title'].str.contains(innov) | df_ATTA['Abstract'].str.contains(innov))]
        result = pd.concat([result,partResult])
    result.to_excel('Result.xlsx');
    return
process()#执行