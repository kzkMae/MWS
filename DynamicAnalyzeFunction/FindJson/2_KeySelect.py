#coding:utf-8

import argparse

#自作関数をインポート
from CopyJson.CopyJsonFile import *
from Argument.CheckArgument import *
from JsonKey.JsonFileKey import *

#引数や-hのオプションを定義
parser = argparse.ArgumentParser(prog='MWS課題，動的解析の機能検索用プログラム',description='オプションと引数の説明',
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
#print jsonlist

#JSONファイルのキーリストを取得
keyList = getJsonKeyList(jsonlist)
print keyList
#keyList.sort()
#作成するKeyの番号（編集おすすめ）
keyNum = [0,2,3,4,5,6,9]
keyJsonData(jsonlist, keyList, keyNum)