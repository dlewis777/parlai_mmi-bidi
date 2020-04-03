import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--infile', type=str)

args = parser.parse_args()

f1 = open(args.infile,'r')
f2 = open('final.txt','w+')

fline = f1.readline().strip().split('\t')
cur_src = fline[0]
cur_tgt = fline[1]
cur_best = float(fline[2])
for line in f1:
    line = line.strip().split('\t')
    #if same src
    print('LINE:', line[0])
    print('CUR', cur_src)
    if line[0] == cur_src:
        if float(line[-1]) < cur_best:
            cur_best = float(line[-1])
            cur_tgt = line[1]
    #if not same src
    else:
        #save best
        f2.write(cur_src + '\t' + cur_tgt + '\n')
        cur_src = line[0]
        cur_tgt = line[1]
        cur_best = float(line[2])

f2.write(cur_src + '\t' + cur_tgt + '\n')

