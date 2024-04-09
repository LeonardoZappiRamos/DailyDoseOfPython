import os
import sys
from datetime import datetime

ROOT_PATH = os.path.join(os.path.dirname(__file__))
FILES_PATH = os.path.join(ROOT_PATH,'files')

if __name__ == '__main__':
    date = datetime.now().strftime('%Y-%m-%d')
    directory = os.path.join(ROOT_PATH, sys.argv[1])
    if os.path.isdir(directory):
        files = os.listdir(directory)
        if len(files) == 0:
            raise FileExistsError("Nenhum arquivo encontrado.")
        else:
            for file in files:
                file_path = os.path.join(directory, file)
                new_file_path = os.path.join(directory, f"{file.split('.')[0]}-{date}.txt")
                os.rename(file_path, new_file_path)
    else:
        raise FileExistsError(f"Não foi encontrado o diretório {directory}.")