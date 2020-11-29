import os
import shutil
from termcolor import colored, cprint

# FILE NOMENCLATURE: [CLASS] [#]-[Assignment Name]_[desc].[filetype]

FILETYPES = {"photos": [".jpeg", ".jpg", ".png"],
             "microsoft": [".docx", ".ppt", ".xlsx"],
             "pdf": [".pdf"],
             "plain": [".txt"]}

# Variable to keep track of how many files are moved
number_of_files = 0
# Enter in directory of school projects
base_directory = f"/Users/***insertuserhere***/Documents/"


def mv_file(file_name: str, path: str) -> None:
    """
    Moves the designated file to the designated path
    :param file_name: The file that you wish to move
    :param path: the path of the file
    :return: str
    """
    global number_of_files
    if file_name.startswith("."):
        pass
    else:
        for extensions in file_formats_list:
            if file_.endswith(extensions):
                shutil.move(desktop + "/" + file_, path)
                print(f"moving {colored(file_name, 'yellow')} to {path}")
                number_of_files += 1
            else:
                pass


def split_file(document: str):
    """
    Splits the name of the document into class name and
    assignment name
    :param document: Passes the name of the file to split
    :return: class name, assignment name
    """
    class_name, sep, assignment_name = document.partition("-")
    try:
        assignment_name = assignment_name.split('.')[0].split('_')[0]
    except TypeError:
        pass
    return class_name, assignment_name


def check_classes(class_name: str) -> str:
    """
    Checks the current year/semester directory and sees if the class name
    exists. If it does not, create a new path
    :param class_name: name of the class
    :return: directory to the class name
    """
    classes_list = []
    class_directory = base_directory
    # Print out all classes in teh class_directory
    for i in os.listdir(class_directory):
        if i.startswith("."):
            pass
        else:
            # Append name off classes to the list
            classes_list.append(i)
            # Check to see if the name of the class is in the list
    if class_name in classes_list:
        current_directory = os.path.join(base_directory, class_name, "/")
        return current_directory
    else:
        cprint(f"{class_name} is not a class, creating new folder", "red")
        new_directory = os.path.join(class_directory, class_name)
        os.mkdir(new_directory)
        cprint(f"path {new_directory} created", "red")
        return new_directory


def check_assignment(path: str, assignment_name: str) -> str:
    """
    Checks class directory and sees if assignment name is listed. If it
     does not, create a new path
    :param path: class directory
    :param assignment_name: name of the assignment
    :return: directory of assignment
    """
    assignment_list = []
    assignment_directory = path
    for value in os.listdir(assignment_directory):
        if value.startswith('.'):
            pass
        else:
            assignment_list.append(value)
    if assignment_name in assignment_list:
        current_directory = os.path.join(path, assignment_name)
        return current_directory
    else:
        cprint(f"{assignment_name} is not a listed assignment, "
               f"creating a new folder", "red")
        new_directory = os.path.join(path, assignment_name)
        os.mkdir(new_directory)
        cprint(f"path {new_directory} made", "red")
        return new_directory


# Returns list of file formats
file_formats_list = [format_ for types_, ext in FILETYPES.items() for format_ in ext]

# Directories
# Enter in the path for your desktop (where the files should be stored)
desktop = "/Users/***insteruserhere***/Desktop"

print("moving files...")
# List files in Desktop
files_in_directory = os.listdir(desktop)
for file_ in files_in_directory:
    # Check to see if file ends with any of the formats in  `file_formats_list`
    for x in file_formats_list:
        if file_.endswith(x):
            # If file starts with a "." ignore it
            if file_.startswith("."):
                pass
            else:
                className, assignmentName = split_file(file_)
                newPath = check_classes(className)
                finalPath = check_assignment(newPath, assignmentName)
                mv_file(file_, finalPath)
print(f"{number_of_files} files moved")
