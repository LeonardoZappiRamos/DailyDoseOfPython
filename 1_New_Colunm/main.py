""" Your task for this project is to create a Python program that alters an Excel file by adding a new column to it. """
import pandas as pd


PATH_FILES = 'assets/files/'


def read_excel_file(filename: str = 'input.xlsx'):
    file = PATH_FILES + filename
    df_input = pd.read_excel(file) 
    return df_input
    

def add_column(file_content):
    file_content['Total'] = file_content['Price'] * file_content['Quantity'] 
    return file_content


if __name__ == '__main__':
    file_content = read_excel_file()
    new_file_content = add_column(file_content)
    new_file_content.to_excel(PATH_FILES+'output.xlsx')
    print("Code finished.")