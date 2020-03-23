import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-f','--file',required=True,type=str)

args = parser.parse_args()
f1 = open(args.file,'r')
f2 = open(args.file + '.st','w+')
for line in f1:
    line = line.strip()
    if len(line.split('\t')) == 2:
        num = line.split(' ')[0]
        s = line.split('\t')[0]
        s = ' '.join(s.split(' ')[1:])
        t = line.split('\t')[1]
        f2.write(num + ' ' + t + '\t' + s + '\n')

    else:
        f2.write('\n')

