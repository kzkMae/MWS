#coding:utf-8

import argparse

#自作関数をインポート
from Argument.CheckArgument import *
from CopyJson.CopyJsonFile import *

#引数や-hのオプションを定義
parser = argparse.ArgumentParser(prog='MWS課題，動的解析の機能検索用プログラム',description='オプションと引数の説明',
                                epilog='以上')
parser.add_argument('-v','--version', action='version', version='%(prog)s version')
parser.add_argument('CopyFolder',type=str, help='コピー元のフォルダを指定, 型：%(type)s，String')
parser.add_argument('SendFolder',type=str, help='コピー先のフォルダを指定, 型：%(type)s，String')
parser.add_argument('CSVFile',type=str, help='探すJsonファイルのリストを格納したCSVファイルを指定, 型：%(type)s，String')


#引数格納
arguMain = parser.parse_args()

#コピー元フォルダを格納
copyfolder = arguMain.CopyFolder
#宛先フォルダを格納
sendfolder = arguMain.SendFolder
#CSVファイルを指定
csvfile = arguMain.CSVFile

#フォルダのチェック
checkNumber = isDirCheck(copyfolder, sendfolder)
#エラーチェック
deadErrorEnd(checkNumber)

#ファイルのチェック
checkNumber = isCsvFile(csvfile)
#エラーチェック
deadErrorEnd(checkNumber)

#csvファイルの読み出し
jsonlist = readCsvfile(csvfile)
#print jsonlist

copyJsonsFile(copyfolder, sendfolder, jsonlist)

print "無問題☆"
