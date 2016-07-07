#coding:utf-8
import csv
import shutil

#指定したJsonファイルをコピーする


#CSVファイルの読み出し
def readCsvfile(csvfile):
    readList = []
    f = open(csvfile, 'rb')
    csvReader = csv.reader(f)
    for row in csvReader:
        #リストに格納
        readList.append(row[0])
        #print row[0]
        #print '\n'
    f.close()
    return readList


#ファイルのコピー
def copyJsonsFile(copyFolder, sendFolder, jsonsList):
    for row in jsonsList:
        shutil.copyfile(copyFolder+row, sendFolder+row)
    return 0


