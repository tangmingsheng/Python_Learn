
import pandas as pd
data = pd.read_excel(r"C:\Users\13580\Desktop\data1119.xlsx")
rows = data.shape[0]  # 获取行数 shape[1]获取列数
department_list = []

for i in range(rows):
    temp = data["事业部"][i]
    if temp not in department_list:
        department_list.append(temp)  # 将事业部的分类存在一个列表中

for department in department_list:
    new_df = pd.DataFrame()

    for i in range (0, rows):
        if data["事业部"][i] == department:
            new_df = pd.concat([new_df, data.iloc[[i] ,:]], axis = 0, ignore_index = True)

    new_df.to_excel(str(department ) +".xls", sheet_name=department, index = False)
