import pandas as pd
import numpy as np

#############Xóa################
# s = pd.Series([1, 2, np.nan, 4])
# print(s)
# s.dropna(inplace=True)
# print(s)
# print()
# df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
#                    "toy": [np.nan, 'Batmobile', 'Bullwhip'],
#                    "born": [pd.NaT, pd.Timestamp("1940-04-25"),
#                             pd.NaT]})

# print(df)
# print()
# # Xóa một dòng mà nếu có 1 phần tử bị khuyết thuyết
# print(df.dropna())
# print()
# # Xóa cột mà nếu có 1 phần tử bị khiếu thiếu
# print(df.dropna(axis =1))
# print()
# print(df.dropna(how='all'))
# print()

# # Xóa dòng nếu có 2 phần tử bị khuyết thiếu trở lên
# print(df.dropna(thresh=2))
# print()
# # Xóa hàng bị khuyết thiếu được xác định trên cột

# print(df.dropna(subset=["name" ,"toy"]))

#############Thay thế################

df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                   [3, 4, np.nan, 1],
                   [np.nan, np.nan, np.nan, 5],
                   [np.nan, 3, np.nan, 4]],
                  columns=list("ABCD"))

print(df)
