import os
# прооверка файла на существование и вытаскивание инфы о файле
file_exists = os.path.exists("req1.py")
print("file exists:", file_exists)

file_info = os.stat("req1.py")
print("file size:", file_info.st_size, "bytes")
print("last modified:", file_info.st_mtime)
