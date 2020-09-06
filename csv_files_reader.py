# author: Rafael Tedesco
# Date: 06/09/2020
# Program to read all csv files from a directory to use in data projects

import os
import json
from tkinter import Tk, filedialog
import time

    

class csvReader():

    def __init__(self, DIR='data', FILE='files_data.json'):
        self.data = {}
        self._DIR = DIR
        self._FILE = FILE
        self._directory = ''

    def __check_exists(self):
        data = {}
        wn = Tk()
        wn.withdraw()
        self._directory = filedialog.askdirectory()

        for root, dirs, files in os.walk(self._directory):

            for f in files:
                if self._FILE in f:
                    with open(os.path.join(root, self._FILE), 'r') as f:
                        self.data = json.load(f)
                        msg = f'There are {len(data)} data files in '
                        if (len(self.data) == 1):
                            msg = msg.replace('s','').replace('There are', 'There is')
                        msg += f'{os.path.join(root, self._FILE)}\n'

                        print(msg)
                        

    def __fetch_files(self):
        new_files = 0
        print('Fetching files...')
        
        for root, dirs, files in os.walk(self._directory):

            for file in files:
                if 'csv' in file.split()[-1]:
                    if file.lower() not in self.data.keys():
                        self.data[file.lower().split('.')[0]] = os.path.join(root, file)
                        print(f'WOW!!! There is a new file named {file}\n')
                        new_files += 1
                    else:   
                        print(f'File founded: {file} was already included\n')

        return new_files


    def __write_files(self, new_files):
        if not self.data or new_files == 0:
            print('Cannot found any csv file or you already have included all csv files in your data')

        else:
            print(f"Writing {new_files} file(s)...")
                
            for idx, f in enumerate(self.data):
                print(f'{idx+1} - {f}')
                time.sleep(0.05)
            
            if not os.path.exists(self._DIR):
                os.mkdir(self._DIR)
                with open(os.path.join(self._DIR,self._FILE), 'w') as f:
                    json.dump(self.data, f, indent=4)

            print(f'Data stored with success in {os.path.join(self._DIR,self._FILE)}!')

    def load_data(self):
        """return your data file as a python dictionary to use with pandas!"""
        f_data = filedialog.askopenfile()
        self.data = json.load(f_data)
            

    def get_files(self):
        self.__check_exists()
        new_files = self.__fetch_files()
        self.__write_files(new_files)


    




