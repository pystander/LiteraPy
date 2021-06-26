# Import libraries
import re
import codecs
from pathlib import Path

# Read character file; create if not exist
if Path('char.txt').is_file():
    f = open('char.txt','r',encoding='utf-8')
    ch_txt = f.read()
    ch_dict = list(ch_txt)
else:
    print("沒有找到char文字檔，重新創建中……")
    char()

# Define functions
def char():
    start,end = (0x4E00, 0x9FA5)
    with codecs.open("chinese.txt", "wb", encoding="utf-8") as f:
        for codepoint in range(int(start),int(end)):
        f.write(chr(codepoint))
