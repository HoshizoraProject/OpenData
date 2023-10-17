import re, hashlib, os, tarfile, zipfile
from urllib.request import urlopen

# 來源資料
unsafelist_url = "https://raw.githubusercontent.com/HoshizoraProject/OpenData/main/unsafelist/unsafelist.txt"

# 定義輸出檔案名稱
fileFolder = "unsafelist"
fileName = "unsafelist"

try:
    # 建立目錄
    try:
        os.mkdir(fileFolder)
    except Exception:
        pass

    # 開啟檔案準備進行寫入
    with open(f'{fileFolder}/{fileName}.txt', 'w') as f:
        try:
            # 從網路開啟檔案
            with urlopen(unsafelist_url) as wf:
                print(line, file=f)
                
            except Exception:
                print(f"issue: {unsafelist_url}")

    # 產出 zip 壓縮檔
    with zipfile.ZipFile(f'{fileFolder}/{fileName}.zip',
                         mode='w',
                         compression=zipfile.ZIP_DEFLATED) as f:
        f.write(f'{fileFolder}/{fileName}.txt', arcname=f'{fileName}.txt')

    # 產出 tar.gz 壓縮檔
    with tarfile.open(f'{fileFolder}/{fileName}.tar.gz', 'w:gz') as f:
        f.add(f'{fileFolder}/{fileName}.txt', arcname=f'{fileName}.txt')

    # 產出 tar.xz 壓縮檔
    with tarfile.open(f'{fileFolder}/{fileName}.tar.xz', 'w:xz') as f:
        f.add(f'{fileFolder}/{fileName}.txt', arcname=f'{fileName}.txt')

    # 產出 tar.zb2 壓縮檔
    with tarfile.open(f'{fileFolder}/{fileName}.tar.bz2', 'w:bz2') as f:
        f.add(f'{fileFolder}/{fileName}.txt', arcname=f'{fileName}.txt')

    # 刪除原始下載文件
    os.remove(f'{fileFolder}/{fileName}.txt')
    
except Exception as ex:
    print(f"issue: {ex}")
