
# 读txt
def readTxt():
    file = 'resource/read-txt.txt'
    with open(file, 'r') as f:  # 可读可写二进制，文件若不存在就创建
        data = f.readlines()  # 读取文本所有内容，并且以数列的格式返回结果，一般配合for in使用
        print(data[0])