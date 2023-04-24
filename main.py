
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
                df_AI[year] += 1
    with pd.ExcelWriter('Result.xlsx') as writer: #初始化一个Writer 输出器 用来输出文件
        df_AI.to_excel(writer) #写入目标文件 格式为
    return

#计算创新和作者的权重 这个版本是用循环去做 速度会比较慢
def Count_Weight():
    df_ID_Title = pd.read_excel("StatisticalWordsFrequency\\ID-Title.xlsx")
    df_ID_Weight = pd.read_excel("StatisticalWordsFrequency\\ID-Weight.xlsx")
    df_Innov_Weight = pd.read_excel("StatisticalWordsFrequency\\Innov-Weight.xlsx")

    #1.对作者权重进行统计
    for i in df_ID_Weight.index:
        print("ID : " + str(i))  # 用于查看处理到第几行了
        ID = df_ID_Weight.iloc[i,0].lower()#获取作者

        weight = df_ID_Title[(df_ID_Title['ID'].str.lower() == ID)].size
        df_ID_Weight.iloc[i,1] = df_ID_Title[(df_ID_Title['ID'].str.lower() == ID)].size

    #2.对创新权重进行统计
    for i in df_Innov_Weight.index:
        print("Innov : " + str(i))
        innov = df_Innov_Weight.iloc[i,0]

        df_Innov_Weight.iloc[i,1] = df_ID_Title['Title'].str.contains(innov, na=False,case = False).size

    #3.输出我们所要的结果
    with pd.ExcelWriter("StatisticalWordsFrequency\ID-Weight-Result.xlsx") as writer: # 写出作者权重表
        df_ID_Weight.to_excel()
    with pd.ExcelWriter("StatisticalWordsFrequency\Innov-Weight-Result.xlsx") as writer:  # 写出作者权重表
        df_ID_Weight.to_excel()

#计算作者的权重 这个版本是用pandas的批量化操作 运行得更快 在循环中使用pandas会比较慢  如dataFrame的groupby()
def Count_ID_Weight():
    id_title_df = pd.read_excel("StatisticalWordsFrequency\\ID-Title.xlsx")
    id_weight_df = pd.read_excel("StatisticalWordsFrequency\\ID-Weight.xlsx")


    #处理作者权重
    id_weight_df_unordered = id_title_df.groupby(['ID']).size().to_frame() #根据id_title表的id列来分组 实际上id_title表和id_weight表id列所拥有的值域应该是一样的
    id_weight_merged_df = pd.merge(id_weight_df,id_weight_df_unordered,how = 'left', on = 'ID')#以左边的源作者权重表 为准 与新计算出权重的表合并

    with pd.ExcelWriter("StatisticalWordsFrequency\InnovWeightFullRes.xlsx") as writer:
        id_weight_merged_df.to_excel(writer)

#计算创新词的权重
def Count_Innov_Weight():
    id_title_df = pd.read_excel("StatisticalWordsFrequency\\ID-Title.xlsx")
    innov_weight_df = pd.read_excel("StatisticalWordsFrequency\\Innov-Weight.xlsx")
    innov_list = innov_weight_df.iloc[:, 0].tolist()

    innov_weight_list = [id_title_df['Title'].str.contains(innov, na=False, case=False).sum() for innov in innov_list]#
    innov_weight_df.iloc[:, 1] = innov_weight_list

    with pd.ExcelWriter("StatisticalWordsFrequency\Innov-Weight-Result.xlsx") as writer:
        innov_weight_df.to_excel(writer)

def filter():
    au_df = pd.read_excel("3.Filter\\作者节点.xlsx")
    au_inn_year_df = pd.read_excel("3.Filter\\作者-创新-历年频次.xlsx")
    edge_df = pd.read_excel("3.Filter\\边数据（作者-创新-频次）.xlsx")

    part_au_inn_year_df = au_inn_year_df[au_inn_year_df['Author'].isin(au_df['Label'])]
    part_edge_df = edge_df[edge_df['Source'].isin(au_df['Label'])]

    with pd.ExcelWriter("3.Filter\\作者-创新-历年频次_part.xlsx") as writer:
        part_au_inn_year_df.to_excel(writer)
    with pd.ExcelWriter("3.Filter\\边数据（作者-创新-频次）_part.xlsx") as writer:
        part_edge_df.to_excel(writer)

def AddStartEnd():
    edge_df = pd.read_excel("3.Filter\\边数据.xlsx")
    au_inn_year_df = pd.read_excel("3.Filter\\作者-创新-历年频次1.xlsx")
    au_inn_year_part_df = pd.read_excel("3.Filter\\作者-创新-历年频次_part.xlsx")

    au_inn_year_ndarray = au_inn_year_df.values #转成ndarray 循环时比较高效
    print(type(au_inn_year_ndarray))
    start_series = pd.series()
    end_series = pd.series()
    for row in au_inn_year_ndarray:
         min = 0
         max = 0
         for i in range(4,67) :
            if np.isnan(row[i]) :
                max = row[0]
                if(min == 0) : min = row[0]
            start_series = min
            end_series = max
    au_inn_year_ndarray['Start'] = start_series
    au_inn_year_ndarray['End'] = end_series

AddStartEnd()