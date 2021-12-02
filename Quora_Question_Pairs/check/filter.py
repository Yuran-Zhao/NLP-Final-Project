import sys

sys.path.insert(0, 'D:\\SJTU\\研二\\助教  自然语言处理前沿技术\\NLP-Final-Project')

import pdb


def filter(filename):
    with open(filename, 'r', encoding='utf8') as fin:
        lines = fin.read().split('\n')
    lines = lines[1:-1]
    final = []
    for line in lines:
        tmp = line[1:-1].split('","')
        if len(tmp) < 6:
            continue
        final.append('\t'.join(tmp[-3:]))
    # pdb.set_trace()
    with open('./Quora_Question_Pairs/data/filted.all.csv',
              'w',
              encoding='utf8') as fout:
        # fout.write(','.join(lines[0].split(',')[-3:]))
        for line in final:
            fout.write(line + '\n')


if __name__ == '__main__':
    filter('./Quora_Question_Pairs/data/all.csv')