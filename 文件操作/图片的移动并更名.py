'''
    作者：Yuan-小江
    功能：图片的批量移动，到指定的文件夹
    版本号：1.0
    日期：2017/12/16
'''
import os

import shutil
import random
def main():
    moveimage(r'F:\恒华\2017年\贵阳\贵阳低压集抄项目\图片',r'F:\恒华\2017年\贵阳\贵阳低压集抄项目\金石供电所图')
def moveimage(imagepath,file):
    image_num = int(len(os.listdir(imagepath)))
    imagelist = os.listdir(imagepath)

    x = 0
    n = 0
    while x < image_num:
        for i in os.listdir(file):
            if len(os.listdir(os.path.join(file,i)))<3:
                movefile = os.path.join(file,i)
                if x >= image_num:
                    x = 0
                    n += 1
                    if n > 3:
                        break
                shutil.copy(os.path.join(imagepath,imagelist[x]),movefile)
                print('第{}张,第{}轮'.format(x+1,n+1))
                x += 1

if __name__ == '__main__':
    main()