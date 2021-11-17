import numpy as np
from numpy.core.fromnumeric import mean, take
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import kstest,normaltest,shapiro,f_oneway,f,kruskal
from scipy.stats.stats import tsem


# # 使用pandas和numpy生成一组仿真数据
s = pd.DataFrame(pd.read_excel('data.xlsx'))
 
# # 创建自定义图像
# # fig = plt.figure(figsize=(100, 60))
# fig = plt.figure()
# # 创建子图1
# ax1 = fig.add_subplot(2,1,1)
# # 绘制散点图
# x = list(s.index)
# y = list(s['平均年龄'])
# ax1.scatter(x,y)
# plt.grid()      # 添加网格
 
# # 创建子图2
# ax2 = fig.add_subplot(2, 1, 2)
# # 绘制直方图
# s['平均年龄'].hist(bins=30,alpha=0.5,ax=ax2)
# # 绘制密度图
# s['平均年龄'].plot(kind='kde', secondary_y=True,ax=ax2)     # 使用双坐标轴
# plt.grid()      # 添加网格
 
# # 显示自定义图像
# plt.show()


# u = s['平均年龄'].mean()
# # 计算标准差
# std = s['平均年龄'].std()  # 计算标准差
# print('scipy.stats.kstest统计检验结果：----------------------------------------------------')
# print(kstest(s['平均年龄'], 'norm', (u, std)))
# print('scipy.stats.normaltest统计检验结果：----------------------------------------------------')
# print(normaltest(s['平均年龄']))
# print('scipy.stats.shapiro统计检验结果：----------------------------------------------------')
# print(shapiro(s['平均年龄']))

m = []


from collections import defaultdict
task2 = defaultdict(list)
for idx,i in enumerate(s['群类别']):
    task2[i].append(s['平均年龄'][idx])
for i in task2.keys():
    temp = pd.Series(task2[i])
    u = temp.mean()
    m.append((u,len(temp)))
    std = temp.std() 


    print('分类',i,'的scipy.stats.kstest统计检验结果：----------------------------------------------------')
    print(kstest(temp, 'norm', (u, std)))
    print('分类',i,'的标准差：')
    print(std)
    print('分类',i,'的方差：')
    print(temp.var())
num = 0
print(m,mean(m,axis=0)[0])
u = s['平均年龄'].mean()

for i in m:
    print(i[1],i[0],u)
    num += i[1]*(i[0]-u)**2

print('Sb=',num)
msb = num/4
print('MSb=',msb)
num = 0
for key in task2.keys():
    temp = pd.Series(task2[key])
    u = temp.mean()
    for item in task2[key]: 
        num += (item-u)**2

print('Sw=',num)
msw = num/2035
print('MSw=',msw)
print('F=',msb/msw,'P=',f_oneway(task2[1],task2[2],task2[3],task2[4],task2[5]))
print('α = 0.05，F-crit为',f.ppf(0.95,4,2035))

# import pdb;pdb.set_trace()
task4 = ['消息数','稠密度','性别比']
task4_cls = defaultdict(list)

for item in task4:
    task4_cls.clear()
    for idx,i in enumerate(s['群类别']):
        task4_cls[i].append(s[item][idx])
    for i in task4_cls.keys():
        temp = pd.Series(task4_cls[i])
        std = temp.std()
        print(item,i,'标准差 = ', std)
    u1 = s[item].mean()
    std1 = s[item].std()  # 计算标准差
    print(item,'scipy.stats.kstest统计检验结果：----------------------------------------------------')
    print(kstest(s[item], 'norm', (u1, std1)))
    print(item,'标准差 = ', std1)

for idx,i in enumerate(s['性别比']):
    if i == 0:
        s['性别比'][idx] = 0.0000001


# 性别比中有0.0,为了后续对数转换，特此做处理
for i in task4 :
    s[i+'_log'] = s[i].map(lambda x : np.log(x)) 
    df_log = s.loc[:,s.columns.str.contains('log')]

# for i in task4:
#     fig = plt.figure()
#     # 创建子图1
#     ax1 = fig.add_subplot(2,1,1)
#     # 绘制散点图
#     x = list(df_log.index)
#     y = list(df_log[i+'_log'])
#     ax1.scatter(x,y)
#     plt.grid()      # 添加网格
    
#     # 创建子图2
#     ax2 = fig.add_subplot(2, 1, 2)
#     # 绘制直方图
#     df_log[i+'_log'].hist(bins=30,alpha=0.5,ax=ax2)
#     # 绘制密度图
#     df_log[i+'_log'].plot(kind='kde', secondary_y=True,ax=ax2)     # 使用双坐标轴
#     plt.grid()      # 添加网格
    # plt.show()
for item in df_log:
    task4_cls.clear()
    for idx,i in enumerate(s['群类别']):
        task4_cls[i].append(df_log[item][idx])
    for i in task4_cls.keys():
        temp = pd.Series(task4_cls[i])
        std = temp.std()
        print(item,i,'标准差 = ', std)
    u = s[item].mean()
    # 计算标准差
    std = s[item].std()  # 计算标准差

    # print(item,'scipy.stats.kstest统计检验结果：----------------------------------------------------')
    # print(kstest(s[item], 'norm', (u, std)))
    # print(item,'标准差 = ', std)
import pdb;pdb.set_trace()
from collections import defaultdict
task5 = defaultdict(list)
for key in task4:
    m = []
    task5.clear()
    
    print(key,':')
    for idx,i in enumerate(s['群类别']):
        task5[i].append(s[key][idx])

    # fig = plt.figure()    
    # for i in task5.keys():
    #     temp = pd.Series(task5[i])        
    #     # 绘制直方图
    #     # temp.hist(bins=30,alpha=0.5)
    #     # 绘制密度图

    #     temp.plot(kind='kde', secondary_y=True)     # 使用双坐标轴
    #     plt.grid()
    # plt.legend(task5.keys())
    # plt.show()


    # for i in task5.keys():
    #     temp = pd.Series(task5[i])
    #     u = temp.mean()
    #     m.append((u,len(temp)))
    #     std = temp.std() 


        # print('分类',i,'的scipy.stats.kstest统计检验结果：----------------------------------------------------')
        # print(kstest(temp, 'norm', (u, std)))
        # print('分类',i,'的标准差：')
        # print(std)
    # num = 0
    # # print(m,mean(m,axis=0)[0])
    # u = s[key].mean()
    # print(key,'整体平均',u)
    # for i in m:
    #     # print(i[1],i[0],u)
    #     num += i[1]*(i[0]-u)**2

    # print('Sb=',num)
    # sb = num
    # msb = num/4
    # print('MSb=',msb)
    # num = 0
    # for key in task5.keys():
    #     temp = pd.Series(task5[key])
    #     u = temp.mean()
    #     for item in task5[key]: 
    #         num += (item-u)**2

    # print('Sw=',num)
    # sw = num
    # msw = num/2035
    # print('MSw=',msw)
    # print('total ss',sb+sw)
    # print('F=',msb/msw,'P=',kruskal(task5[1],task5[2],task5[3],task5[4],task5[5]))
    # print('α = 0.05，F-crit为',f.ppf(0.95,4,2035))
    