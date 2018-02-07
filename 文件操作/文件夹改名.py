'''
    作者：Yuan-小江
    功能：图片的批量移动，到指定的文件夹
    版本号：1.0
    日期：2017/12/16
'''
import os,shutil
def changename(file):
    names = os.listdir(file)
    n = 0
    for name in names:

        childname = os.path.join(file,name)
        if '现场图片' in os.listdir(childname):
            # n += 1
            old_name = os.path.join(childname,'现场图片')
            new_name =os.path.join(r'F:\恒华\2017年\贵阳\贵阳低压集抄项目\金石现场', childname.split('\\')[-1])
            # os.rename(old_name,new_name)
            shutil.move(old_name,new_name)
            # print(new_name)
def copy_documents():
    copy_1 = r'F:\城东\128、安井片区I1组团1#配电室1#居照及商业变\2、安井片区I1组团1#配电室1#居照及商业变平面布置图.dwg'
    for paste in os.listdir(r'f:\python'):
        paste = os.path.join(r'f:\python',paste,'2、{}平面布置图.dwg'.format(paste[4:]))
        shutil.copy(copy_1,paste)
        print(paste)
def main():
    # changename(r'F:\恒华\2017年\贵阳\贵阳低压集抄项目\贵阳低压集抄施工资料2017.11.26\2017年第二批贵阳局花溪供电局低压集抄改造工程\【图纸】\金石供电所')
    copy_documents()
if __name__ == '__main__':
    main()