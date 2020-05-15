import os
from pathlib import Path
import shutil
import time


def create_folder(folder_name):
    """create folders specified in argument"""
    print('\n_* def create_folder():  INPUT == ', folder_name, '\n')
    try:
        os.mkdir(folder_name)
        print(folder_name, ' -> ++ folder successful created')
    except:
        print(folder_name, ' -> -- folder already created')
    return folder_name


def move_files(extension, folder):
    """move files with extension to specyfic folder"""
    print('\n_* def move_files():  INPUT ==  ext==', extension, " folder==", folder)
    sourcepath = Path().absolute()
    sourcefiles = os.listdir(sourcepath)
    destination = str(sourcepath) + "\\" + folder

    print("list of all files: \n", sourcefiles)

    print("source:", sourcepath)
    print("destination:", destination)

    for file in sourcefiles:
        if file.endswith(extension):
            shutil.move(os.path.join(sourcepath, file), os.path.join(destination, file))


def remove_delete_download():
    """delete folders with all content from: !delete, !download"""
    print('\n')
    try:
        shutil.rmtree('!delete')
    except:
        print('---')
    try:
        shutil.rmtree('!download')
    except:
        print('---')


move_files('.wav', create_folder('!delete'))

move_files('.part', create_folder('!delete'))

remove_delete_download()
