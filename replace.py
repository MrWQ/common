import os

# 文件中 某些字符替换为其他字符
def oldToNew(path,oldstr,newstr):
    oldFile = open(path,'r+')
    textInOld = oldFile.read()
    print(textInOld)
    textInOld = textInOld.replace(oldstr,newstr)
    oldFile.write('\n')
    oldFile.write(textInOld)
    print('\n')
    print(textInOld)
    oldFile.close()