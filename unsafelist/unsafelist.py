import sys, getopt, os, tarfile, zipfile
from urllib.request import urlopen

# 設定基礎使用的設定
baseUrl = 'https://unsafelist.opendata-hoshizora.xyz'
baseFileName = 'unsafelist'

def main(argv):
    # 讀取的檔案類型(預設抓最小的 tar.zx)
    filetype = 'tar.xz'
    # 儲存的目錄(預設在 importData)
    filefolder = 'importData'

    # 嘗試取得輸入參數
    try:
        opts, args = getopt.getopt(argv,"ht:f:",["ftype=","folder="])
    except getopt.GetoptError:
        print('unsafelist.py -t <filetype>[txt|zip|tar.gz|tar.bz2|tar.xz] -f <folder>')
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h':
            print('unsafelist.py -t <filetype>[txt|zip|tar.gz|tar.bz2|tar.xz] -f <folder>')
            sys.exit(0)
        elif opt in ("-t", "--ftype"):
            filetype = arg
        elif opt in ("-f", "--folder"):
            filefolder = arg

    # 根據輸入參數取得相關檔案
    if filefolder != '':
        if not os.path.exists(filefolder):
            os.mkdir(filefolder)

    # 取得線上 md5 檔案
    with urlopen(f'{baseUrl}/{baseFileName}.md5') as webf:
        # 讀取線上 md5 檔案
        web_md5 = webf.read().decode("utf-8")

        # 判斷本地 md5 是否存在
        if os.path.exists(f'{filefolder}/{baseFileName}.md5'):
            # 讀取本地 md5 檔案
            with open(f'{filefolder}/{baseFileName}.md5', 'r') as f:
                local_md5 = f.read()

                # 比對 md5 內容是否相同, 相同則輸出 md5 值, 並返回正常結束
                if web_md5 == local_md5:
                    print(web_md5, end='')
                    sys.exit(0)

        # 本地 md5 檔案不存在, 則寫入並輸出 md5 值
        with open(f'{filefolder}/{baseFileName}.md5', 'w') as f:
            print(web_md5, file=f, end='')
            print(web_md5, end='')

    # 根據不同檔案類型進行處理
    try:
        match(filetype):
            case 'txt':
                with urlopen(f'{baseUrl}/{baseFileName}.txt') as webf:
                    with open(f'{filefolder}/{baseFileName}.txt', 'wb') as f:
                        f.write(webf.read())
        
            case 'zip':
                with urlopen(f'{baseUrl}/{baseFileName}.zip') as webf:
                    with open(f'{filefolder}/{baseFileName}.zip', 'wb') as f:
                        f.write(webf.read())
                with zipfile.ZipFile(f'{filefolder}/{baseFileName}.zip', 'r') as f:
                    f.extractall(f'{filefolder}')
                os.remove(f'{filefolder}/{baseFileName}.zip')

            case 'tar.gz':
                with urlopen(f'{baseUrl}/{baseFileName}.tar.gz') as webf:
                    with open(f'{filefolder}/{baseFileName}.tar.gz', 'wb') as f:
                        f.write(webf.read())
                    with tarfile.open(f'{filefolder}/{baseFileName}.tar.gz', 'r:gz') as f:
                        f.extractall(f'{filefolder}')
                os.remove(f'{filefolder}/{baseFileName}.tar.gz')

            case 'tar.xz':
                with urlopen(f'{baseUrl}/{baseFileName}.tar.xz') as webf:
                    with open(f'{filefolder}/{baseFileName}.tar.xz', 'wb') as f:
                        f.write(webf.read())
                    with tarfile.open(f'{filefolder}/{baseFileName}.tar.xz', 'r:xz') as f:
                        f.extractall(f'{filefolder}')
                os.remove(f'{filefolder}/{baseFileName}.tar.xz')

            case 'tar.bz2':
                with urlopen(f'{baseUrl}/{baseFileName}.tar.bz2') as webf:
                    with open(f'{filefolder}/{baseFileName}.tar.bz2', 'wb') as f:
                        f.write(webf.read())
                    with tarfile.open(f'{filefolder}/{baseFileName}.tar.bz2', 'r:bz2') as f:
                        f.extractall(f'{filefolder}')
                os.remove(f'{filefolder}/{baseFileName}.tar.bz2')

            case _:
                raise Exception(f'unsupported file type: {filetype}')
    except Exception:
        sys.exit(1)

    # 程式正常結束    
    sys.exit(0)

if __name__ == "__main__":
   main(sys.argv[1:])
