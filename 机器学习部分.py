
import  pandas as pd
from  sklearn.cluster import  KMeans
from  sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

def loadData():
    """
    从excel表格中加载数据存入dataframe中
    :param data:None
    return:爬取所得的数据
    """
    df_Cs=pd.read_excel(open('CsData.xlsx','rb'))
    df_Dmg=pd.read_excel(open('DmgData.xlsx','rb'))
    df_Gpm=pd.read_excel(open('GpmData.xlsx','rb'))
    df_Kda=pd.read_excel(open('KdaData.xlsx','rb'))
    df_Played=pd.read_excel(open('PlayedData.xlsx','rb'))

    df_total=df_Cs
    df_total=df_total.merge(df_Dmg)
    df_total=df_total.merge(df_Gpm)
    df_total=df_total.merge(df_Kda)
    df_total=df_total.merge(df_Played)

    tem_xpm=df_total['经验/分钟']
    tem_gpm=df_total['经济/分钟']
    tem_dps=df_total['伤害/分钟']
    tem_rate=df_total['胜率']
    tem_kill=df_total['击杀']
    df_total['伤害/经济']=tem_dps/tem_gpm
    df_total['伤害/胜率']=tem_dps/tem_rate
    df_total['击杀/胜率']=tem_kill/tem_rate

    df_total=df_total.set_index("英雄")
    return df_total
    

def km_hero(data):
    """
    使用英雄比赛数据对英雄主流位置进行聚类
    :param data: 数据
    :return: None
    """
    # 数据筛选
    print(data)
    data = data.loc[:,["正补/10分钟","击杀"]]
    
    # 进行K-means聚类
    km = KMeans(n_clusters=4) # 构建估计器实例
    km.fit(data) # 训练数据
    y_predict = km.predict(data) # 进行预测
    
    
    data['英雄类型']=y_predict
    return data,y_predict


def hero_pos_score(data,y_predict):
    """
    进行聚类结果评估
    :param data:筛选后的英雄数据 
    :param y_predict: 预测结果
    :return: score
    """
    score = silhouette_score(data,y_predict)

    return score

def scatter_hero(data,y_predict):
    """
    绘图分析
    :param data: 筛选后的英雄数据
    :param y_predict: 预测结果
    :return: None
    """
    color =["red","green","blue","pink","yellow"]
    colors = []

    for c in y_predict:
        colors.append(color[c])

    # 创建画布
    plt.figure()
    plt.rcParams['font.sans-serif'] = 'SimHei'  # 默认不支持中文，设置这行代码进行支持中文
    plt.rcParams['axes.unicode_minus'] = False  # 默认不支持负数，设置这行代码进行支持负数
    # 绘图
    x = data["正补/10分钟"]
    y = data["击杀"]
    # 绘制散点图
    plt.scatter(x,y,color=colors)
    # 增加横轴标签
    plt.xlabel("正补/10分钟")
    # 增加纵轴标签
    plt.ylabel("击杀")
    #增加标题
    plt.title("英雄击杀以及补刀关系图")
    # 增加网格曲线
    plt.grid(b= True)
    # 图形展示
    plt.show()

def main():
    df=loadData()
    df,y_predict=km_hero(df)
    scatter_hero(df,y_predict)
    score = hero_pos_score(df,y_predict)
    print(score)
    
    print(df.loc[df['英雄类型']==0])
    print(df.loc[df['英雄类型']==1])
    print(df.loc[df['英雄类型']==2])
    print(df.loc[df['英雄类型']==3])
    



main()