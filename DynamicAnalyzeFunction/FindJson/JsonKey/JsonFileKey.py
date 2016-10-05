#coding:utf-8
import json
import os
#Jsonファイル内のKeyを操作
def x():
    return 0

#Jsonファイルのキーを取得
def getJsonKeyList(fileList):
    #Jsonファイルの読み込み
    i = fileList[0]
    f = open(i,'r')
    jsonData = json.load(f)
    #print json.dumps(jsonData, sort_keys=True, indent=4)
    #Jsonファイルのキーをリスト化
    keyList = jsonData.keys()
    #print keyList[1]
    print keyList
    f.close()
    return keyList

def keyJsonData(fileList,keyList, keyNum):
    for i in fileList:
        f = open(i, 'r')
        jsonData = json.load(f)
        iname,ext = os.path.splitext(i)
        #Jsonファイル名と同じフォルダを作成
        if not(os.path.isdir(iname)):
            os.mkdir(iname)

        for j in keyNum:
            key = keyList[j]
            jsonData_Key = jsonData[key]
            with open(iname + '\\' + key + '.json', 'w') as newjf:
                json.dump(jsonData_Key, newjf, indent=4)
        f.close()
    return 0