# coding: UTF-8
#InImpasse 2020.04.14修改
import os.path#规避可能发生的找不到文件问题
import json
import os
import time
import pyperclip#调用pyperclip模块

#读取用户自定设置
scriptpath = os.path.dirname(__file__)
userfilename = os.path.join(scriptpath, 'user.json')
userjson =open(userfilename, encoding = "utf-8", mode="r")
userjson1 = userjson.read()
userJsonDict = json.loads(userjson1)
rolltime = userJsonDict["rolltime"]

while True:
    #解析JSON文件
    filename = os.path.join(scriptpath, 'ThisDataPacketBody.json')
    openfile = open(filename, encoding = "utf-8", mode="r")
    GetJson = openfile.read()
    JsonDict = json.loads(GetJson)
    Data = JsonDict['data']#选取源json文件中data部分，继续解析
    #输出部分
    if 'options' in Data:
        lenth=len(Data['options'])
        for i in range(0,lenth):
            answer = str(Data['options'][i]['answer'])
            if answer == 'True':
                print("正确答案是：",Data['options'][i]['content'])
        print('--------------------------------------------------') 
    if 'answer_content' in Data:
        if 'stem' in Data:
            print("正确答案是：",Data['answer_content'])
            print('--------------------------------------------------') 
            pyperclip.copy(Data['answer_content'])#复制答案到剪贴板
    time.sleep(3)#刷新时间为3s，可修改