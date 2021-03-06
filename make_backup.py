# -*-coding:utf-8-*-
import shutil
import os
from datetime import datetime
from time import sleep

# カレントディレクトリに"backup"フォルダがあればtrue,なければfalseを返す
def checkExistBackupDir(files):
    for file in files:
        if file == "backup":
            return True
    return False

def checkBackupComplete():
    filesAfterBackup = os.listdir("./backup")
    for file in filesAfterBackup:
        # print(file)
        if file == backupFileName:
            print("backup successed")
            return
    print("backup failed")
    print("try again")
    return 

# カレントディレクトリの中身を取得
files = os.listdir("./")

# "backup"フォルダの存在を確認し、無ければ作成
if checkExistBackupDir(files) == False:
    os.mkdir("backup")

# 時間の取得
backupTime = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
print("try making backup file at: "+backupTime)

# ファイルネームの作成
backupFileName = "Backup_lib_system-" + backupTime + ".txt"

# ファイルのコピー
shutil.copyfile("./tes.txt","./backup/" + backupFileName)

# ファイルの存在確認
checkBackupComplete()

sleep(3) 
