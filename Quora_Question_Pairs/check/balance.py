import os
import sys

sys.path.insert(0, 'D:\\SJTU\\研二\\助教  自然语言处理前沿技术\\NLP-Final-Project')


def balance(filename):
    with open(filename, 'r', encoding='utf8') as fin:
        lines = fin.read().split('\n')
    lines = lines[1:-1]
    total = len(lines)
    cnt = {'0': 0, '1': 0}
    for line in lines:
        try:
            target = line.split('\t')[-1]
            cnt[target] += 1
        except:
            continue
    print("There are {} is 0, {} is 1".format(cnt['0'], cnt['1']))


if __name__ == "__main__":
    balance('./Quora_Question_Pairs/data/filted.all.csv')
