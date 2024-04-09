import os
import re


SAMPLE_PATH = os.path.join(os.path.dirname(__file__), 'sample.txt')


if __name__ == '__main__':
    file_content = open(SAMPLE_PATH, 'r').read()
    print('\n', file_content, '\n')
    find_email = re.findall("[a-z]+@[a-z]+.[a-z]+", file_content)
    find_telefone = re.findall("\([0-9]{3}\)[ .-][1-9]{3}[ .-][0-9]{4}|[0-9]{3}[ .-][0-9]{3}[ .-][0-9]{4}", file_content)
    print(find_email) 
    print(find_telefone) 