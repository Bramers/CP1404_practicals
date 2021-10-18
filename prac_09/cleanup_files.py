"""rename files to be consistent"""

import os


def main():
    """Demo os module functions."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            new_name = get_fixed_filename(filename)
            full_name = os.path.join(directory_name, filename)
            full_corrected_name = os.path.join(directory_name, new_name)
            os.rename(full_name, full_corrected_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    try:
        for i, character in enumerate(new_name):
            if new_name[i].islower() or new_name[i].isupper():
                if new_name[i + 1].isupper():
                    new_name = new_name[:i + 1] + "_" + new_name[i + 1:]
    except IndexError:
        pass
    return new_name.title()


main()


# try:
#     for i, character in enumerate(filename):
#         new_name += character
#         if filename[i].islower():
#             if filename[i + 1].isupper():
#                 new_name += "_"
# elif filename[i] == " ":
# new_name += character.replace(" ", "_")
# except IndexError:
#     print("index")
# corrected_name = new_name.replace(".TXT", ".txt")
