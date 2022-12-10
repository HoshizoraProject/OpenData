# UnsafeList
根據公開資料源產出的不安全網域清單

## 主要資料網址
https://unsafelist.opendata-hoshizora.xyz

## 使用前請服用下列事項
* 請把 unsafelist.py 抓去用
* 請注意 unsafelist.py 內使用了 match, 需要 Python >= 3.10 版本, 否則請自行改為 if else 結構

## Python 使用上的範例
```
import subprocess, re
from urllib.parse import urlparse

# 定義 unsafelist
unsafelist = []
unsafelist_md5 = ''


# 呼叫 unsafelist 更新系統
def func_check_unsafelist():
    global unsafelist, unsafelist_md5

    # 執行自動檢查程序
    proc = subprocess.run(['python3', 'unsafelist.py'],
                          stdout=subprocess.PIPE)
    if (proc.returncode != 0):
        print("執行 unsafelist.py 發生異常!")
        return

    # 取得 MD5 資料
    md5 = proc.stdout.decode("utf-8")

    # 比對 MD5是否相同
    if md5 == unsafelist_md5:
        print(f'檢查 unsafelist 完成，本次無需更新!')
        return

    # md5 不相同, 開始重新讀取檔案
    try:
        with open(f'importData/unsafelist.txt') as f:
            unsafelist = f.read().splitlines()

        unsafelist_md5 = md5
        print(f'更新 unsafelist 成功! MD5: {unsafelist_md5}')
    except Exception:
        print("讀取 unsafelist 發生異常!")


# 執行程式
func_check_unsafelist()

# 要測試的網域 (預設抓黑名單第一行)
domain = unsafelist[0]

# 測試用訊息
content = f"黑名單網域測試 http://{domain}/123 喵喵"

# 顯示測試用的訊息
print(content)

# 建立網址使用的正規表達式
pattern = re.compile(r"((https?):((//)|(\\\\))+[\w\d:#@%/;$()~_?\+-=\\\.&]*)",
                     re.MULTILINE | re.UNICODE)

# 取得所有訊息中的網址
urls = re.findall(pattern, content)

# 對所有網址進行判斷
for url in urls:
    # URL 資訊拆分
    url_parse = urlparse(url[0])

    # 判斷是否在黑名單內, 並顯示 (實際上你不用顯示, 而是做事)
    print(f'{url_parse.netloc in unsafelist}: {url_parse.netloc}')

```
## License
[GNU Lesser General Public License v3.0](https://www.gnu.org/licenses/lgpl-3.0.en.html)
