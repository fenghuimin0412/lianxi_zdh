import yaml
def get_yaml_data(fileDir):
    resList = [] #存放结果
    # 1,读取文件操作---从磁盘读取文件到内存里
    fo = open(fileDir,'r',encoding="utf-8")
    # 2.使用yaml方法获取数据
    res = yaml.load(fo,Loader=yaml.FullLoader)
    fo.close()
    for i in res:
        resList.append((i['data'],i['resp']))
    return resList

if __name__ == '__main__':
    filepath = ('../data/loginCase.yaml')
    res = get_yaml_data(filepath)
    for i in res:
        print(i)