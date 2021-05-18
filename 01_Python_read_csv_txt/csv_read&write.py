import csv,codecs
from itertools import islice

# ！介绍：此文件满足读取.csv文件的部分需求
# ！注意：此文件中存在代码互斥的情况，请删除不需要的功能以避免互斥

def readCSV():
    # 文本文件用r
    # 二进制文件用rb
    with open('resource/test-data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in islice(reader, 0, 4): #从第0行开始读取，截止第三行

            # 1--所有数据
            allData = row

            # 2--按列索引读取数据
            rowByIndex = row[0]

            # 3--按列索引拆开数据 row[0]==张三 row[0][0]==张
            rowSplit = row[0][0]

            # 4--查询第一列为"张三"的行数据
            if row[0] == "张三":
                selectData = row

            # 5--过滤第一列为"李四"的行数据
            if row[0] == "李四":
                continue
            selectData = row

            # 6--当第一列为"王五"时停止读取
            if row[0] == "王五":
               break
            selectData = row

# readCSV()

def writeCSV():

    # a:写文件的方式为追加
    # w:写文件的方式为覆盖
    file = open('resource/write-csv.csv', 'a',newline='') # 创建resource/write-csv.csv文件
    writer = csv.writer(file)

    # 1--写一行数据
    writer.writerow(['abcd', 'efg',"hijk"])
    file.close()

    # 2--循环写数据
    # writer.writerow(['abcd', 'efg', "hijk"])
    for i in range(0,20):
        writer.writerow(["你好aaa","hello"])
    file.close()

# writeCSV()