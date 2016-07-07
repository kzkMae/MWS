#coding:utf-8
import sys
import os.path
#引数チェック用の関数



#強制終了用の関数
def deadErrorEnd(checkNumber):
    if not (checkNumber == 0):
        print "終了します"
        sys.exit()
    return 0

#指定したフォルダの有無をチェック
def isDirCheck(copyFolder, sendFolder):
    checkNum = 0
    if not (os.path.isdir(copyFolder)):
        checkNum += 1
        print "Copy元のフォルダは存在しないよ"
    if not (os.path.isdir(sendFolder)):
        checkNum += 1
        print "送り先のフォルダは存在しないよ"
    return checkNum

#指定したCSVファイルの有無をチェック
def isCsvFile(csvFile):
    checkNum = 0
    if not(os.path.isfile(csvFile)):
        checkNum = 1
    return checkNum