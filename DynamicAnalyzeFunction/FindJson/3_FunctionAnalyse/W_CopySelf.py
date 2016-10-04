#coding:utf-8

import argparse
import csv

#自作関数をインポート
from DynamicAnalyzeFunction.FindJson.CopyJson.CopyJsonFile import *
from DynamicAnalyzeFunction.FindJson.Argument.CheckArgument import *
from AllFunction import *

#引数や-hのオプションを定義
parser = argparse.ArgumentParser(prog='動的解析 自分自身のコピー探索用プログラム',description='オプションと引数の説明',
                                epilog='以上')
parser.add_argument('-v','--version', action='version', version='%(prog)s version')
#parser.add_argument('CopyFolder',type=str, help='コピー元のフォルダを指定, 型：%(type)s，String')
parser.add_argument('csvFile',type=str, help='Jsonファイル名を格納したCSVファイルを指定, 型：%(type)s，String')

#引数格納
arguMain = parser.parse_args()
#CSVファイルを指定
csvfile = arguMain.csvFile

#ファイルのチェック
checkNumber = isCsvFile(csvfile)
#エラーチェック
deadErrorEnd(checkNumber)
#csvファイルの読み出し
jsonlist = readCsvfile(csvfile)
print jsonlist

#リスト作成
list = []

for i in jsonlist:
    folderName, ext = os.path.splitext(i)
    #print folderName
    jsonData = getJsondropped(folderName)
    #print jsonData
    #print len(jsonData)
    #print type(jsonData)
    #if not len(jsonData) == 0:
    #    print "sha1" in jsonData[0]
    list.append(searchSHA1(jsonData, folderName))

#csvファイルに書き込み
with open("W_selfCopyCheck.csv", "wb") as f:
    csvWriter = csv.writer(f)
    for i in range(len(list)):
        csvWriter.writerow(list[i])


