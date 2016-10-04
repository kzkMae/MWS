#coding:utf-8

#import
import os.path
import json


def x():
    return 0

#droppedファイルの中身を読む
def getJsondropped(foldername):
    #print os.path.isfile(foldername+"\\dropped.json")
    with open(foldername+"\\dropped.json","r") as f:
        jsonData = json.load(f)
        #print type(jsonData)
    return jsonData

#droppedファイルにあるsha1タグの中身が同じものを検索
def searchSHA1(jsonData, fileHash):
    sha1S = "sha1"
    #print len(jsonData),
    #print fileHash,
    #print jsonData
    for i in jsonData:
        if sha1S in i:
            if i[sha1S] == fileHash:
                #print 1
                return [fileHash, 1]
    return [fileHash, 0]