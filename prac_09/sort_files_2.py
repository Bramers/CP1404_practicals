import os


def main():
    file_type_to_category = {}
    os.chdir("FilesToSort")
    for filename in os.listdir("."):
        if os.path.isdir(filename):
            continue

        file_type = find_file_type(filename)
        if file_type not in file_type_to_category:
            category = input(f"What category would you like to sort {file_type} files into? ")
            file_type_to_category[file_type] = category

            try:
                os.mkdir(category)
            except FileExistsError:
                pass

        os.rename(filename, f"{file_type_to_category[file_type]}/{filename}")


def find_file_type(filename):
    extension_index = filename.find(".") + 1
    file_type = filename[extension_index:]
    return file_type


main()
