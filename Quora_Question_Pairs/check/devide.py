import sys

sys.path.insert(0, 'D:\\SJTU\\研二\\助教  自然语言处理前沿技术\\NLP-Final-Project')

import random


def devide(filename):
    with open(filename, 'r', encoding='utf8') as fin:
        lines = fin.read().split('\n')
    lines = lines[:-1]
    idx = list(range(len(lines)))
    train_size = int(0.7 * len(idx))
    valid_size = int(0.2 * len(idx))
    random.shuffle(idx)
    train_idx = idx[:train_size]
    valid_idx = idx[train_size:train_size + valid_size]
    test_idx = idx[train_size + valid_size:]

    train_lines = [lines[idx] for idx in train_idx]
    write('./Quora_Question_Pairs/data/train.txt', train_lines)

    valid_lines = [lines[idx] for idx in valid_idx]
    write('./Quora_Question_Pairs/data/valid.txt', valid_lines)

    test_lines = [lines[idx] for idx in test_idx]
    write('./Quora_Question_Pairs/data/test.txt', test_lines)


def write(filename, lines):
    with open(filename, 'w', encoding='utf8') as fout:
        # fout.write(','.join(lines[0].split(',')[-3:]))
        for line in lines:
            fout.write(line + '\n')


if __name__ == "__main__":
    devide('./Quora_Question_Pairs/data/filted.all.csv')
