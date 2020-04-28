import json
from pprint import pprint
from os import listdir
import os
from os.path import isfile, join

mypathOrig = '/Users/yagyanshbhatia/code2seq/data/'
dirs = ['test', 'train', 'valid']

for dir in dirs:
    mypath = mypathOrig + dir

    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f[-5:]=='jsonl']

    for f in onlyfiles:
        with open(os.path.join(mypath, f), 'r') as f:
            sample_file = f.readlines()
        
        for index, sample in enumerate(sample_file):
            code = json.loads(sample)['code']
            filename = dir + '_' + str(index) + '.java'
            with open(os.path.join(mypath, filename), 'w') as f:
                f.write(code)
