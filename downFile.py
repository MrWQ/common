import requests

#  图片下载
def downloadFile(url,name,type):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.61 Safari/537.36'}
    # 设置20秒timeout
    picture = requests.get(url=url, headers=headers, timeout=20)
    # 写入文件
    f = open(str(name) + str(type), 'wb')
    f.write(picture.content)
    f.close()
