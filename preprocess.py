# 预处理程序 使用numpy和pandas对一维、二维表进行处理
import numpy as np
import pandas as pd

DF_AIW = pd.read_excel('AIW-test.xlsx')#DataFrame of Author-Innovation-Weight


DF_ATTA = pd.read_excel("ATTA.xlsx")#DataFrame of Author-Title-Time-Abstract
DF_AI_part = DF_AIW[['Author','Innov']]#截取一部分拿来试验 拿几百条出来试验 我把中文列名都改成英文了 我怕出错
DF_ATTA_part = DF_ATTA.head(82887);#作者-标题..表的部分数据
result = pd.DataFrame();#创建一个用于输出的结果集

for i in range(0, len(DF_AI_part), 1):#遍历全部 作者-创新
    df_thisAuthor =DF_ATTA_part.loc[DF_ATTA_part.Authors.str.contains(DF_AI_part['Author'][i],na = False)] #从作者-标题..表中取出所有该作者的作品
    for index,row in df_thisAuthor.iterrows() :
        temp_df = df_thisAuthor.loc[index]
        result = pd.concat([result,temp_df],sort = False,axis=0,)

#导出到新Result.xlsx中
writer = pd.ExcelWriter("Result.xlsx")
result.to_excel(writer)
writer.save()
