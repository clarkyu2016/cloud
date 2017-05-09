
from random import randint
import codecs

def getmemo():
    memo =[]
    name = []
    f = codecs.open('memo.txt', 'r', 'UTF-8')
    for line in f:
        if len(line) > 10 and len(line)<100:
            memo.append(line)
    f.close()

    memo_num = randint(0,len(memo)-1)

    return memo[memo_num]
