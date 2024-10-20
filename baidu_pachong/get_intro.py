
##此文件用于输入名字并获取其百度词条中的个人简介

import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import urllib.parse
import build_input


static_str='https://baike.baidu.com/item/'


# 定义一个函数来读取文件
def read_file_to_array(filename):
    # 初始化一个空列表
    lines = []
    
    # 使用 with 语句打开文件，确保文件在处理后自动关闭
    with open(filename, 'r', encoding='utf-8') as file:
        # 遍历文件中的每一行
        for line in file:
            # 去掉行尾的换行符，并将行添加到列表中
            lines.append(line.strip())
    
    return lines

#将一个名字转换为编码
def re_encode(string):
   encode_str=urllib.parse.quote(string)
   return encode_str

#访问网站并返回html文件
def collect(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0'
    }
    res=requests.get(url=url,headers=headers).content.decode('utf-8')
    return res


file_path = 'input.text'  # 文件路径
Name_array = read_file_to_array(file_path)

##for  Name in Name_array:
    #将名字翻译为Unicode编码
##    name_code=re_encode(Name)

    #将固定地址加上名字编码做出新的url
url='https://baike.baidu.com/item/%E6%AF%9B%E5%B3%B0/64699894'

    #执行方程获取html文件
res=collect(url)

    #对html的标签进行操作
bs=BeautifulSoup(res,'html.parser')
tag=bs.findAll('span',class_='text_H038s')

    #写入文件
with open('output.text','a',encoding='utf-8') as file:
    for fil in tag:
        file.write(fil.get_text())
        file.write('\n')
    
with open('output.text','a',encoding='utf-8') as file:
        file.write('\n')
