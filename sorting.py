# -*- coding: utf-8 -*-

import os, time, shutil


class FolderMaker:

    def __init__(self, folder_path, new_folder_path):
        self.folder_path = folder_path
        self.new_folder = new_folder_path

    def sort(self):
        for dirpath, dirnames, filenames in os.walk(self.folder_path):
            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                seconds = os.path.getctime(full_file_path)
                file_time = time.gmtime(seconds)
                file_year = file_time[0]
                file_month = file_time[1]
                new_path = os.path.join(self.new_folder, '{}'.format(file_year), '{}'.format(file_month))
                if os.path.exists(new_path):
                    shutil.copy2(full_file_path, new_path)
                else:
                    os.makedirs(new_path)
                    shutil.copy2(full_file_path, new_path)


user_input1 = input('Please enter the path to the folder that need to be sorted')
path = os.path.normpath(user_input1)
new_folder = os.path.normpath(os.path.join(os.path.dirname(path), 'SORTED FILES'))
folder = FolderMaker(path, new_folder)
folder.sort()
