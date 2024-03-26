""" Command Line Diary App """
import os
import datetime

def render_interface(today: str, content: list = []):
    os.system('cls')
    print(f'Date: {today}')
    print("Enter with your notes, type 'exit' to save and exit.\n")
    if len(content) == 0:
        print("You don't have any notes\n")
    else:
        for num, line in enumerate(content):
            print(f"{num} - {line}")
        print("\n")
    

def get_notes(filename):
    try:
        with open(f"{filename}.txt", 'r', encoding='utf-8') as file:
            content = file.read()
        notes = content.strip().split('\n')
        return notes
    except FileNotFoundError:
        open(f"{filename}.txt", 'w', encoding='utf-8').close()
        return []


def save_data(notes, filename):
    try:
        with open(f"{filename}.txt", 'w', encoding='utf-8') as file:
            for note in notes:
                file.write(note + "\n")
    except:
        raise FileNotFoundError("Could not find file")
    print(f"Your notes was saved in {filename}.txt")
    
    
if __name__ == "__main__":
    close = True
    today = datetime.datetime.now().strftime("%Y_%m_%d")
    notes = get_notes(today)
    try:
        while close:
            render_interface(today, notes)
            new_notes = input("-> ")
            if new_notes != "exit":
                notes.append(new_notes)
            else:
                close = False
        save_data(notes, today)
    except Exception as err:
        print('Exception: %s' % err)
        