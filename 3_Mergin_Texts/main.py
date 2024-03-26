""" Merged files in order """
# Imports
import os


# Constants
ROOT_PATH = os.path.dirname(__file__)
SPLIT_FILES_PATH = os.path.join(ROOT_PATH, 'input')
MERGED_FILES_PATH = os.path.join(ROOT_PATH, 'output')


# Main and Functions
def get_files() -> list:
    """ Return a list of filenames """
    try:
        _is_dir = os.path.isdir(SPLIT_FILES_PATH)
        if _is_dir:
            filenames = os.listdir(SPLIT_FILES_PATH)
            filenames.sort()
            return filenames
    except:
        raise ValueError('Could not find the input files.')
    
if __name__ == '__main__':
    """ Main function """
    os.system('cls')
    merge_content = ''
    print("Running: Reading Files.")
    filenames = get_files()
    try:
        print("Running: Merging Files.")
        for filename in filenames:
            filepath = os.path.join(SPLIT_FILES_PATH, filename)
            with open(filepath, 'r', encoding='utf8') as f:
                content = f.read()
                merge_content += content
        print("Running: Saving Files.")
        with open(os.path.join(MERGED_FILES_PATH, 'output.txt'), 'a', encoding='utf8') as f:
            f.write(merge_content)
        os.system('cls')
        print("File Created")
    except Exception as e:
        print("Error: %s" % e)