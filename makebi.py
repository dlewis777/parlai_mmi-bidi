import sys

f1 = open('nbest.txt', 'r')
f2 = open('newbi.txt', 'w+')
f3 = open('../ParlAI/data/Persona-Chat/personachat/valid_self_original.txt','r')

cur = f3.readline()
counter = 1
for line in f1:
    if line == '--\n':
        cur = f3.readline()
    else:
        line = line.strip()
        tgt = ' '.join(cur.split('\t')[0].split(' ')[1:]).strip()
        newline = str(counter) + ' ' + line + '\t' + tgt
        f2.write(newline + '\n')
        counter += 1

