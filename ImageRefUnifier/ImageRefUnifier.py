import os
import re
import sys

# there are tow types of reference of image in old markdown files
default_pattern = re.compile(r'!\[.*?]\(.*?\)')
html_pattern = re.compile(r'<img.*?src=.*?>')


# function to get the path to the folder containing the images to be unified
def getUserInput():
    print("Please enter the path to the folder containing the images to be unified:")
    path = input()

    while not os.path.exists(path):
        print("The path you entered does not exist. Please try again.")
        path = input()

    return path


# def file or dir item of file-tree
class FileOrFolder:
    def __init__(self, name, is_dir):
        self.name = name
        self.is_dir = is_dir
        self.children = []

    def addChild(self, child):
        self.children.append(child)

    def print_structure(self, indent=0):
        prefix = "| " * indent
        type_prefix = "[D]" if self.is_dir else "[F]"
        print(f"{prefix} - {type_prefix} - {self.name}")
        if self.is_dir:
            for child in self.children:
                child.print_structure(indent + 1)

    def hierachyFunc(self, func):
        func(self)
        for child in self.children:
            child.hierachyFunc(func)


# build file tree based on given path
def buildFileTree(path):
    if not os.path.isdir(path):
        return FileOrFolder(path, False)
    root_path = FileOrFolder(path, True)

    for sub_path in os.listdir(path):
        sub_file_path = os.path.join(path, sub_path)
        root_path.addChild(buildFileTree(sub_file_path))

    return root_path


# judge whehter the given item is markdown file
def isMarkdownFile(cur_item):
    if (cur_item.is_dir or (".md" not in cur_item.name)):
        return False
    return True


# show the way of image reference in current file
def showImageReferenceWay(cur_item):
    if not isMarkdownFile(cur_item):
        return

    file = open(cur_item.name, "r")
    if (file == None):
        print("open file failed")
        sys.exit(-1)
    content = file.read()
    file.close()

    # find all image reference
    image_refs_1 = default_pattern.findall(content)
    image_refs_2 = html_pattern.findall(content)

    # show the way of image reference
    for imageRef in image_refs_1:
        print(imageRef)
    print("\n--------------------------------------------------\n")
    for imageRef in image_refs_2:
        print(imageRef)


# calculate the level of directory
def directoryLevel(file_name):
    # print(f"file name is {file_name}")
    notebook_top_level = file_name.find("Typora files")
    length = len(file_name) - 1
    index = notebook_top_level + len("Typora files") + 1
    # print(f"current index is {index}, {file_name[index]}, {file_name[index+1]}")
    directory_levels = 0
    while index != length:
        if file_name[index] == "/":
            directory_levels += 1
        index += 1
    return directory_levels


# fix each line of image reference
def defaultFixLine(line, file_name):
    if "http" in line:
        return line

    fix_line = line.replace("\\", "/")
    if "../" in fix_line:
        return fix_line
    if "图库" in fix_line:
        pre_fix = "../" * directoryLevel(file_name)
        return re.sub(r"\(.*Typora files/", "(" + pre_fix, fix_line)
    return fix_line

def htmlFixLine(line, file_name):
    if "http" in line:
        return line

    fix_line = line.replace("\\", "/")
    if "../" in fix_line:
        return fix_line
    if "图库" in fix_line:
        pre_fix = "../" * directoryLevel(file_name)
        return re.sub(r"src=.*Typora files/", "src=\"" + pre_fix, fix_line)
    return fix_line


#  check and fix the reference of image for given file
def fixImageReference(cur_item):
    if not isMarkdownFile(cur_item):
        return

    write_lines = []
    with open(cur_item.name, "r") as file:
        for line in file:
            if default_pattern.match(line):
                new_line = defaultFixLine(line, cur_item.name)
                # print(f"previous line is [{line}],and new line is [{new_line}] ")
                write_lines.append(new_line)
                # print("-----------------------------------\n")
            elif html_pattern.match(line):
                new_line = htmlFixLine(line, cur_item.name)
                # print(f"previous line is [{line}],and new line is [{new_line}] ")
                write_lines.append(new_line)
                # print("-----------------------------------\n")
            else:
                write_lines.append(line)
    with open(cur_item.name, "w") as file:
        file.writelines(write_lines)


if __name__ == '__main__':

    unifiedPath = getUserInput()
    fileTree = buildFileTree(unifiedPath)
    # fileTree.print_structure()
    # fileTree.hierachyFunc(showImageReferenceWay)

    fileTree.hierachyFunc(fixImageReference)

    print("Done!")



