'''
    作者：Yuan-小江
    功能：根据指定内容建立文件夹
    版本号：1.0
    日期：2017/12/18
'''
import os

def read(file):
    with open(file, 'r') as f:
        names = f.read().split('\n')
    for x, name in enumerate(names):
        if name == '':
            names.pop(x)

    return names

def makedir(names):
    for name in names:
        if not os.path.exists(name):
            os.makedirs(name)

def main():
    names = read(r'F:\python\123.txt')
    os.chdir(r'F:\python')
    makedir(names)

if __name__ == '__main__':
    main()
# 105-111