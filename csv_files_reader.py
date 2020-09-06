# author: Rafael Tedesco
# Date: 06/09/2020
# Program to read all csv files from a directory to use in data projects

import os
import json
from tkinter import Tk, filedialog
import time

    
root = Tk()
root.withdraw()
directory = filedialog.askdirectory()
DIR = 'data'
FILE = 'files_data.json'


def check_exists():
    data = {}
    for root, dirs, files in os.walk(directory):

        for f in files:
            if FILE in f:
                with open(os.path.join(root, FILE), 'r') as f:
                    data = json.load(f)
                    msg = f'There are {len(data)} data files in '
                    if (len(data) == 1):
                        msg = msg.replace('s','').replace('There are', 'There is')
                    msg += f'{os.path.join(root, FILE)}\n'

                    print(msg)
    return data
                        

def fetch_files(data):
    new_files = 0
    print('Fetching files...')
    
    for root, dirs, files in os.walk(directory):

        for file in files:
            if 'csv' in file.split()[-1]:
                if file.lower() not in data.keys():
                    data[file.lower()] = os.path.join(root, file)
                    print(f'WOW!!! There is a new file named {file}\n')
                    new_files += 1
                else:   
                    print(f'File founded: {file} was already included\n')

    return (data, new_files)


def write_files(data, new_files):
    if not data or new_files == 0:
        print('Cannot found any csv file or you already have included all csv files in your data')

    else:
        print(f"Writing files...")
        print(data)
        time.sleep(1)
        
        if not os.path.exists(DIR):
            os.mkdir(DIR)
            with open(os.path.join(DIR,FILE), 'w') as f:
                json.dump(data, f, indent=4)

        print(f'Data stored with success in {os.path.join(DIR,FILE)}!')
            

data = check_exists()
data, new_files = fetch_files(data)
write_files(data, new_files)



