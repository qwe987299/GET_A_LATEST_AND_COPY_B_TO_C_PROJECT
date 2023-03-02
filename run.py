import os
import shutil

# 取得最新一筆檔案的修改時間
latest_time = 0
for file_name in os.listdir("C:\\Users\\user\\Desktop\\TEST\\A"):
    file_path = os.path.join("C:\\Users\\user\\Desktop\\TEST\\A", file_name)
    if os.path.isfile(file_path):
        file_time = os.path.getmtime(file_path)
        if file_time > latest_time:
            latest_time = file_time

# 複製符合條件的檔案到目的地
for file_name in os.listdir("C:\\Users\\user\\Desktop\\TEST\\B"):
    file_path = os.path.join("C:\\Users\\user\\Desktop\\TEST\\B", file_name)
    if os.path.isfile(file_path):
        file_time = os.path.getmtime(file_path)
        if file_time >= latest_time:
            shutil.copy2(file_path, "C:\\Users\\user\\Desktop\\TEST\\C")