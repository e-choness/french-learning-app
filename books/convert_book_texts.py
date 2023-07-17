import os
from os import listdir


file_dir = "./books/"
output_dir = "./books/Text/"
file_lists = listdir(file_dir)


def find_book_content(book_texts):
    splitted = book_texts.split('***')
    content = splitted[2].strip()
    return content

def open_file(file_path):
    
    with open(file_path,'r', encoding='utf-8', errors='ignore') as f:
        book_texts = f.read()
        content = find_book_content(book_texts)
    return content

def save_content(file, output_dir, content):
    output_file = os.path.join(output_dir, file)
    with open(output_file, "w", encoding='utf-8', errors='ignore') as f:
        f.write(content)
    print("Content saved to: {0}".format(output_file))

def read_book_texts(file_lists, file_dir, output_dir):
    for file in file_lists:
        if file.endswith(".txt"):

            file_path = os.path.join(file_dir,file)
            content = open_file(file_path)
            save_content(file, output_dir, content)


read_book_texts(file_lists, file_dir, output_dir)

