import json
from pprint import pprint
from os import listdir
import os
from os.path import isfile, join

mypath = '/home/gpudata/yagyansh/yagyansh/code2seq/data/valid'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f[-5:]=='jsonl']

for f in onlyfiles:
    with open(os.path.join(mypath, f), 'r') as f:
        sample_file = f.readlines()
    
    for sample in sample_file:
        code = json.loads(sample)['code']
        print(code)
        print()
        print()
        print()
