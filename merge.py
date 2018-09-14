import os
import re
import sys
from tqdm import tqdm

def has_sentence(line):
    line = line.strip('\n')
    if  line == '':
        return False
    if re.match('<doc.*>',line):
        return False
    if re.match('</doc>',line):
        return False
    return True

def get_all_file(root):
    all_files=[]
    subdirs = os.listdir(root)
    subdirs.sort()
    for subdir in subdirs:
        dir_path = os.path.join(root, subdir)
        files = os.listdir(dir_path)
        files.sort()
        for file in files:
            file_path = os.path.join(dir_path, file)
            all_files.append(file_path)

    return all_files

root = sys.argv[1]
merge_path = sys.argv[2]

out_file= open(merge_path, 'w')

files = get_all_file(root)
for file in tqdm(files):
    with open(file, 'r') as f:
        for line in f:
            if has_sentence(line):
                line = line.strip('\n')
                print (line, file=out_file)
out_file.close()
