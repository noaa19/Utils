import pandas as pd
import xlrd
from xlutils.copy import copy

# 读excel
def readExcel():
    df = pd.read_excel(r'resource/read-excel.xls')
    for i in df.values:
     print(i[1])
    print(df.values[0])
    print(df.values[0][1])

readExcel()

# 追加写exxcel
def writeExcel():
    # 打开表格
    wb = xlrd.open_workbook("resource/write-excel.xls")
    # 将xlrd对象copy转化为xlwt对象
    newWb = copy(wb)
    # 获取转换后的第一个sheet
    newSheet = newWb.get_sheet(0)
    # 追加写入数据
    for i in range(0, 10):
        newSheet.write(i + 1, 3, "你好")
        # 保存表格
        newWb.save("resource/write-excel.xls")
writeExcel()
