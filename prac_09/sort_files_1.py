"""sort files by file type"""
import os
import shutil


def main():
    os.chdir("FilesToSort")
    for filename in os.listdir("."):
        # extension = filename.split('.')[-1]

        folder_name = find_file_type(filename)
        try:
            os.mkdir(folder_name)
        except FileExistsError:
            pass
        shutil.move(filename, folder_name)


def find_file_type(filename):
    """Determines the type of a file"""
    extension_index = filename.find(".") + 1
    file_type = filename[extension_index:]
    return file_type


main()
