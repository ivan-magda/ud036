import os


def rename_files():
    folder_path = os.getcwd() + "/prank"
    os.chdir(folder_path)

    file_list = os.listdir(folder_path)
    print(file_list)

    for file_name in file_list:
        new_file_name = ''.join(i for i in file_name if not i.isdigit())
        print("New file name " + new_file_name)
        os.rename(file_name, new_file_name)

    os.chdir(os.getcwd())


rename_files()
