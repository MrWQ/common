
# 将文件编码改为utf-8
# 改变文件编码utf-8 防止gbk编码文件无法打开
def encodeFile(path):
    # 改变文件编码utf-8 防止gbk编码文件无法打开
    fp = open(path, 'rb')
    fps = fp.read()
    fp.close()
    try:
        fps = fps.decode('utf-8')
        print('当前文件编码为 utf-8,无需修改编码')
    except:
        fps = fps.decode('gbk')
        print('当前文件编码为 gbk,正在修改编码...')
    fps = fps.encode('utf-8')
    fp = open(path, 'wb')
    fp.write(fps)
    fp.close()
    print('当前文件编码为 utf-8')