
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df_Cs=pd.read_excel('CsData.xlsx')
df_Dmg=pd.read_excel('DmgData.xlsx')
df_Gpm=pd.read_excel('GpmData.xlsx')
df_Kda=pd.read_excel('KdaData.xlsx')
df_Played=pd.read_excel('PlayedData.xlsx')#从excel表格中读取数据，存入dataframe

df_total=df_Cs
df_total=df_total.merge(df_Dmg)
df_total=df_total.merge(df_Gpm)
df_total=df_total.merge(df_Kda)
df_total=df_total.merge(df_Played)#将dataframe矩阵按照index值等值连接组合

df_total=df_total.set_index("英雄")

print(df_total)
#print(df_Kda)

font={'family':'SimHei'}
matplotlib.rc('font',**font)#添加画布字体信息，使得支持中文
fig=plt.figure()
from pylab import *
#subplots_adjust(left=0.0,bottom=0.0,top=1,right=3,hspace=0.5,wspace=0.1)#自定义画布的一些属性
plt.hist(df_total['伤害/分钟'].apply(float),bins=117,color='pink')#将字符串转至float并且创建图
plt.title("英雄伤害分布")
plt.xlabel('dps')
plt.ylabel('个数')
plt.legend()#显示图例说明标签
plt.show()#展示图形
df_total=df_total.sort_values(by='使用次数',ascending=False)#按照使用次数对数据进行降序排列
tem_use_count=df_total['使用次数'][:20]#切片选取前20个数据
#subplots_adjust(left=0.0,bottom=0.0,top=1,right=2,hspace=0.5,wspace=0.1)
plt.pie(tem_use_count,labels=tem_use_count.index,autopct='%.3f%%'
        ,startangle=90)#绘制饼图，将index作为标签，将图逆时针旋转90°后绘制
plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 1))#防止标签互相覆盖
plt.title('出场次数最高的20名英雄的出场对比')
plt.show()


df_total=df_total.sort_values(by='伤害/分钟',ascending=False)
tem=df_total['伤害/分钟'][:20]
tem.plot(kind='bar',title='伤害最高的前20个英雄',color='pink')#使用dataframe的方法绘制条形图
plt.xticks(rotation=360)#将x轴标签水平放置，易于直接观察
plt.legend()
plt.show()


df_total=df_total.sort_values(by='胜率',ascending=False)
tem=df_total['胜率'][:20]
tem.plot(kind='bar',title='胜率最高的前20个英雄',color='pink')
plt.xticks(rotation=360)
plt.legend()
plt.show()


font={'family':'SimHei'}
matplotlib.rc('font',**font)
fig=plt.figure()

fig.add_subplot(121)
y=df_total['胜率'].hist(bins=117,color='pink')#bins为直方图的竖直条条数
plt.title("英雄胜率分布")
plt.xlabel('胜率')
plt.ylabel('个数')
plt.show()


#subplots_adjust(left=0.0,bottom=0.0,top=1,right=3,hspace=0.5,wspace=0.1)
df_total=df_total.sort_values(by='使用次数',ascending=False)
tem=df_total['使用次数'][:20]
tem.plot(kind='bar',title='使用次数最高的前20个英雄',color='pink')
plt.xticks(rotation=360)
plt.legend()
plt.show()


#(left=0.0,bottom=0.0,top=1,right=3,hspace=0.5,wspace=0.1)
df_total=df_total.sort_values(by='建筑伤害/分钟',ascending=False)
tem=df_total['建筑伤害/分钟'][:20]
tem.plot(kind='bar',title='建筑伤害/分钟最高的前20个英雄',color='pink')
plt.xticks(rotation=360)
plt.legend()
plt.show()

#(left=0.0,bottom=0.0,top=1,right=3,hspace=0.5,wspace=0.1)
df_total=df_total.sort_values(by='经济/分钟',ascending=False)
tem=df_total['经济/分钟'][:20]
tem.plot(kind='bar',title='经济/分钟最高的前20个英雄',color='pink')
plt.xticks(rotation=360)
plt.legend()
plt.show()

#(left=0.0,bottom=0.0,top=1,right=3,hspace=0.5,wspace=0.1)
df_total=df_total.sort_values(by='经验/分钟',ascending=False)
tem=df_total['经验/分钟'][:20]
tem.plot(kind='bar',title='经验/分钟最高的前20个英雄',color='pink')
plt.xticks(rotation=360)
plt.legend()
plt.show()


tem_xpm=df_total['经验/分钟']
tem_gpm=df_total['经济/分钟']
tem_dps=df_total['伤害/分钟']
tem_rate=df_total['胜率']
tem_kill=df_total['击杀']
df_total['伤害/经济']=tem_dps/tem_gpm#取数据集的数据，进行新数据的计算创建
df_total['伤害/胜率']=tem_dps/tem_rate
df_total['击杀/胜率']=tem_kill/tem_rate
#(left=0.0,bottom=0.0,top=1,right=3,hspace=0.5,wspace=0.1)
df_total=df_total.sort_values(by='伤害/经济',ascending=False)
tem=df_total['伤害/经济'][:20]
tem.plot(kind='bar',title='伤害/经济最高的前20个英雄',color='pink')
plt.xticks(rotation=360)
plt.legend()
plt.show()


#(left=0.0,bottom=0.0,top=1,right=3,hspace=0.5,wspace=0.1)
df_total=df_total.sort_values(by='伤害/胜率',ascending=False)
tem=df_total['伤害/胜率'][:20]
tem.plot(kind='bar',title='伤害胜率相关图例',color='pink')
plt.xticks(rotation=360)
plt.legend()
plt.show()


#(left=0.0,bottom=0.0,top=1,right=3,hspace=0.5,wspace=0.1)
tem=df_total['胜率'][:20]
tem.plot(kind='bar',title='关于"伤害胜率相关图例"中20个英雄的胜率图例',grid=True,color='pink')
plt.xticks(rotation=360)
plt.legend()
plt.show()


#(left=0.0,bottom=0.0,top=1,right=3,hspace=0.5,wspace=0.1)
df_total=df_total.sort_values(by='击杀/胜率',ascending=False)
tem=df_total['击杀/胜率'][:20]
tem.plot(kind='bar',title='击杀胜率相关图例',color='pink')
plt.xticks(rotation=360)
plt.legend()
plt.show()


tem=df_total['胜率'][:20]
tem.plot(kind='bar',title='关于"击杀胜率相关图例"中20个英雄的胜率图例',grid=True,color='pink')
plt.xticks(rotation=360)
plt.legend()
plt.show()


df_total=df_total.sort_values(by='击杀',ascending=False)
tem=df_total['击杀'][:20]
tem.plot(kind='bar',title='击杀相关图例',color='pink')
plt.xticks(rotation=360)
plt.legend()
plt.show()


#(left=0.0,bottom=0.0,top=1,right=3,hspace=0.5,wspace=0.1)
tem=df_total['胜率'][:20]
tem.plot(kind='bar',title='关于"击杀相关图例"中20个英雄的胜率图例',grid=True,color='pink')
plt.xticks(rotation=360)
plt.legend()
plt.show()

#(left=0.0,bottom=0.0,top=1,right=3,hspace=0.5,wspace=0.1)
tem=df_total['伤害/经济'][:20]
tem.plot(kind='bar',title='关于"击杀相关图例"中20个英雄的伤害/经济图例',grid=True,color='pink')
plt.xticks(rotation=360)
plt.legend()
plt.show()