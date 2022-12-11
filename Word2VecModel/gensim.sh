#!/bin/bash
apt install axel -y
apt install opencc -y
apt install python3-pip -y
pip3 install -U gensim
pip3 install -U jieba
rm -f zhwiki-latest-pages-articles.xml.bz2* wiki_texts.txt wiki_zh_tw.txt s2tw.json
axel -n 3 -o zhwiki-latest-pages-articles.xml.bz2 https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2
python3 wiki_to_txt.py zhwiki-latest-pages-articles.xml.bz2
opencc -i wiki_texts.txt -o wiki_zh_tw.txt -c s2tw.json
python3 segment.py
python3 train.py
python3 demo.py
