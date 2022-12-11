# Word2Vec Mode
向量化NLP中文語意資料

## 資料來源
* [維基百科資料庫](https://dumps.wikimedia.org/zhwiki/latest/) 使用 `pages-articles.xml.bz2` 結尾的檔案
* [直接下載](https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2)

## 最後更新
2022-12-11 08:00 UTC+8

## 自行訓練
[下載](https://github.com/HoshizoraProject/OpenData/raw/main/Word2VecModel/word2vec.sh) `word2vec.sh`
```
chmod +x word2vec.sh
./word2vec.sh
```
將會在當前目錄下建立 `word2vec` 並開始安裝及抓取箱官元件後開始訓練

## 參考引用
https://github.com/zake7749/word2vec-tutorial

## License
[Apache License, Version 2.0](https://opensource.org/licenses/Apache-2.0)
