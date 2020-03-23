import sys
import argparse
import re

parser = argparse.ArgumentParser()

parser.add_argument('-f','--file', required=True, type=str)
parser.add_argument('-t','--top',required=True,type=str)
args = parser.parse_args()

f1 = open(args.file,'r')
f2 = open(args.file + '.filter','w+')

topf = open(args.top,'r')

topk = []

for line in topf:
    topk.append(line.strip())

curconv = []
bad = False

regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

numlines = 0

for line in f1:
    numlines += 1
f1.close()
print(numlines)
trigrams = {}
print('tri')
curnum = 0

'''
f1 = open(args.file,'r')

for line in f1:
    curnum += 1
    if curnum % 1000 == 0:
        print(str(curnum))
    if len(line.split('\t')) < 2:
        pass
    else:

        r = line.split('\t')[1]
    
        if len(r) < 3:
            pass
        else:
            for i in range(len(r) - 2):
                r1 = r[i]
                r2 = r[i+1]
                r3 = r[i+2]

                tri = r1 + ',' + r2 + ',' + r3

                if tri in trigrams.keys():
                    trigrams[tri] += 1
                else:
                    trigrams[tri] = 1
 
f1.close()
'''
f1 = open(args.file,'r')
print('reading...')
curline = 0
for line in f1:
    curline += 1
    if curline % 10000 == 0:
        print(curline)
    if line == '\n':
        # dont write lines with any bad stuff
        if bad == True:
            pass
        else:
            print('HERE')
            for x in curconv:
                f2.write(x)

            f2.write('\n')
        curconv = []
        bad = False
    elif len(line.strip().split('\t')) < 2:
        bad = True
    else:
        # Top 50 words
        seen = False
        
        # ends in qm
        #if line.split('\t')[0][-1] != '?':
        #    bad = True
        #    continue
        # bad line
        if line.strip().split('\t')[1] == '':
            bad = True
            continue
        for w in line.strip().split('\t')[1].split(' '):
            if w in topk:
                seen = True
        if seen == False:
            bad = True

        # Website
        if 'www' in line or 'http' in line or '.com' in line:
            bad = True

        # special characters
        elif regex.search(line) != None:
            bad = True

        # over 200
        elif len(line.split(' ')) >= 200:
            bad = True
        '''
        # trigram
        res = line.strip().split('\t')[1].split(' ')
        count = 0
        amm = 0
        for i in range(len(res) - 2):
            tri = res[i] + ',' + res[i+1] + ',' + res[i+2]
            if trigrams[tri] > 1000:
               amm += 1
            count += 1
        if float(amm) / count > 90:
            bad = True
        '''
        curconv.append(line)
