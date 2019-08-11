#!/usr/bin/env python3

import sys,csv
import socket

# input csv file
INPUT = str(sys.argv[1])
OUTPUT = '%s.count' % INPUT

# dummy filtering of colors to retain black, brown, and red

approved_list = ['red','black','brown']

with open(OUTPUT,'w') as outfile:
    count = 0
    with open(INPUT,'r') as csvfile:
        input_reader = csv.reader(csvfile)
        for row in input_reader:
            if row[1] in approved_list:
                count += 1
    outfile.write('count %d' % count)
    outfile.write('hostname %s' % socket.gethostname())
