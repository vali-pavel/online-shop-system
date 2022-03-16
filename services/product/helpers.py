import os


def create_folder(folder_name: str):
    try:
        os.mkdir(folder_name)
    except FileExistsError:
        pass
