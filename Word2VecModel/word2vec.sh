#!/bin/bash
# 安裝元件
apt install axel -y
apt install opencc -y
apt install python3-pip -y
pip3 install -U gensim
pip3 install -U jieba

# 判斷目錄是否存在
if [ ! -d "./word2vec" ]; then
    git clone https://github.com/zake7749/word2vec-tutorial.git word2vec
fi
cd word2vec

# 清除殘留的檔案
rm -f zhwiki-latest-pages-articles.xml.bz2* wiki_texts.txt wiki_zh_tw.txt s2tw.json

# 下載資料
axel -n 3 -o zhwiki-latest-pages-articles.xml.bz2 https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2

# 進行資料轉換
python3 wiki_to_txt.py zhwiki-latest-pages-articles.xml.bz2
opencc -i wiki_texts.txt -o wiki_zh_tw.txt -c s2tw.json

# 進行分詞與學習
python3 segment.py
python3 train.py

# 呼叫範例測試
python3 demo.py
