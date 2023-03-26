import pandas as pd
import numpy as np


def Count_Year():  # 处理过程
    # 读入 AIW.xlsx
    df_AI = pd.read_excel("AIW.xlsx")
    # 读入 ATTA.xlsx
    df_ATTA = pd.read_excel("ATTA.xlsx")
    #循环处理每一条作者和创新
    for i in df_AI.index: #遍历每一条index
        print(i)
        # 选取作者列
        author = df_AI.iloc[i, 0] # 选取该行的作者
        innov = df_AI.iloc[i, 1]  # 选取该行的创新
        # 找出 有作者是author 并且 标题或摘要中有该创新词 的 文章 ↓ case = False 大小写不敏感 na = False 无视空行
        df_thisAuthor = df_ATTA[df_ATTA['Authors'].str.contains(author, case=False, na=False)]  #用str.contains来进行条件查询 查到该作者的
        partResult = df_thisAuthor[
            (df_thisAuthor['Title'] + df_thisAuthor['Abstract']).str.contains(innov, case=False, na=False)]
        for j in partResult.index:
            year = partResult['Publication Year'][j]
            num = df_AI[year][i]
            if np.isnan(num) :
                df_AI[year][i] = 1
            else:
                df_AI[year] += 1;
    with pd.ExcelWriter('Result.xlsx') as writer: #初始化一个Writer 输出器 用来输出文件
        df_AI.to_excel(writer) #写入目标文件 格式为
    return

def Count_Weight():
    df_ID_Title = pd.read_excel("StatisticalWordsFrequency\ID-Title.xlsx");
    df_ID_Weight = pd.read_excel("StatisticalWordsFrequency\ID-Weight.xlsx");
    df_Innov_Weight = pd.read_excel("StatisticalWordsFrequency\Innov_Weight.xlsx");

    #1.对作者权重进行统计
    for i in df_ID_Title.index:
        print("ID : " + i) # 用于查看处理到第几行了
        ID = df_ID_Title.iloc[i,0] #获取作者

        df_ID_Weight_row = df_ID_Weight[df_ID_Weight['ID'].str.toLower() == ID] # 从作者权重表中找到那一行 精确匹配 且 大小写敏感为否

        weight = df_ID_Weight_row.iloc['Weight'][df_ID_Weight_row.index[0]] # 获取其权重 权重已经预处理初始化为0
        weight += 1 #自增1

        df_ID_Weight_row.iloc['Weight'][df_ID_Weight_row.index[0]] = weight;# 赋值

    #2.对创新权重进行统计
    for i in df_Innov_Weight.index:
        print("Innov : " + i)
        innov = df_Innov_Weight.iloc[i,0]

        df_Innov_Weight.iloc[i,1] = df_ID_Title['Title'].str.contains(innov, na=False,case = False).size

    #3.输出我们所要的结果
    with pd.ExcelWriter("StatisticalWordsFrequency\ID-Weight-Result.xlsx") as writer: # 写出作者权重表
        df_ID_Weight.to_excel()
    with pd.ExcelWriter("StatisticalWordsFrequency\Innov-Weight-Result.xlsx") as writer:  # 写出作者权重表
        df_ID_Weight.to_excel()