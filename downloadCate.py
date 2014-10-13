 #!/bin/python
 #-*-coding:utf-8-*- 
import os
import os.path
import urllib 
#import urllib2 
#import requests
import socket

socket.setdefaulttimeout(20.0)   #设定链接超时

rootdir = 'C:\\Users\\chickenfucker\\Desktop\\url\\'    #指明被遍历的文件夹
downdir = 'http://img.taotaosou.cn/'    #指明图片下载的地址
savedir = 'E:\\taotaosou.com\\product_pic\\'    #指明图片保存的地址
a=0; b=0; c=0; d=0      #文件名计数器

cateClassify = {
    'A': lambda: 'Cloths\\',
    'B': lambda: 'Pants\\',
    'C': lambda: 'Shoes\\',
    'D': lambda: 'Bags\\'
    }
    
def processfile(url, cate, name):    #处理文件的函数
    savecate = cateClassify[cate]()
    
    print "downloading with urllib"     #使用urllib下载链接文件 
    try:
        urllib.urlretrieve(url, savedir+savecate+str(name)+'.jpg')
    except Exception as e:
        print ("show error info:",e)
        pass
        
    #print "downloading with urllib2"   #使用urllib2下载链接文件
    #f = urllib2.urlopen(url) 
    #data = f.read()
    #with open("code2.zip", "wb") as code:     
    #    code.write(data)
    
    #print "downloading with requests"      #使用requests下载链接文件
    #r = requests.get(url) 
    #with open("code3.zip", "wb") as code:
    #     code.write(r.content)

def addmeA():
    global a
    a += 1
    return a
def addmeB():
    global b
    b += 1
    return b    
def addmeC():
    global c
    c += 1
    return c
def addmeD():
    global d
    d += 1
    return d

for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for dirname in dirnames:    #遍历目录下的子文目录
        for parent,dirnames,filenames in os.walk(rootdir+dirname):      #遍历子目录下的文件         
            for filename in filenames[1:-1]:
                f = open(rootdir + dirname + '\\' + filename)      #打开文件
                while True:     #逐行读取文件
                    line = f.readline()
                    if not line: break 
                    cate = line[0]     #读取图片的分类
                    imagedir = line[2:-1]     #读取图片地址
                
                    nameImage = {
                        'A': lambda: addmeA(),
                        'B': lambda: addmeB(),
                        'C': lambda: addmeC(),
                        'D': lambda: addmeD()
                        }[cate]()       #给图片文件命名
                    processfile(downdir + imagedir, cate, nameImage)
                f.close()
            
print "finish job!"