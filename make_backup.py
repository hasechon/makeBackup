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
        else:
            pass
  
    return False

# カレントディレクトリの中身を取得
files = os.listdir("./")

# バックアップファイルの存在を確認。存在すればtrue.
backupDirExist = checkExistBackupDir(files)

# "backup"フォルダが無ければ作成
if backupDirExist == False:
    os.mkdir("backup")

# 時間の取得
backupTime = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
print("try making backup file at: "+backupTime)

# ファイルネームの作成
backupFileName = "Backup_lib_system-" + backupTime + ".txt"

# ファイルのコピー
shutil.copyfile("./copies_tes.txt","./backup/" + backupFileName)

# ファイルの存在確認
filesInBackup = os.listdir("./backup")
for file in filesInBackup:
    # print(file)
    if file == backupFileName:
        print("backup successed")

sleep(3) 