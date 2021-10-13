import zipfile
import os

input_dir = os.path.join(os.curdir, "scripts", "root")
output_dir = os.path.join(os.curdir,"build")

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def zipfolder(input_dir_path,output_dir_path,archive_name):
    output_dir_path = os.path.join(output_dir_path,archive_name)
    zipobj = zipfile.ZipFile(output_dir_path + '.zip', 'w', zipfile.ZIP_DEFLATED)
    rootlen = len(input_dir_path) + 1
    for  dirpath, dirnames, filenames in os.walk(input_dir_path):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            file_path_inside_archive = file_path[rootlen:]
            zipobj.write(file_path, file_path_inside_archive)

for folder in os.listdir(input_dir):
    folder_path = os.path.join(input_dir,folder)
    if not os.path.isdir(folder_path):
        continue
    print(folder_path)
    zipfolder(folder_path,output_dir,folder)

