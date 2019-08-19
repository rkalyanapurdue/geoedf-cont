#!/usr/bin/env python3

import random,sys,csv

#job run directory
#RUN_DIR = str(sys.argv[1])
RUN_DIR = '/tmp'

#create a few dummy csv files
num_csvs = random.randint(0,5)

print('creating %d csv files' % num_csvs)

colors = ['red','blue','brown','black','orange','cyan','green','white','purple']

num_colors = len(colors)

for i in range(0,num_csvs):

    size = random.randint(1,len(colors))
    input_file = '%s/sing_input_%d.csv' % (RUN_DIR,i)
    print('writing csv file ',input_file)
    with open(input_file,'w') as csvfile:
        input_writer = csv.writer(csvfile)
        for j in range(0,size):
            indx = random.randint(0,num_colors-1)
            input_writer.writerow([j,colors[indx]])






