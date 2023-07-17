import os
from os import listdir

file_dir = "./"
file_lists = listdir(file_dir)
for file in file_lists:
    if file.endswith(".meta"):
        os.remove(os.path.join(file_dir, file))