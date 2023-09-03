import os
import sys


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


def buildFileTree(path):
    if not os.path.isdir(path):
        return FileOrFolder(path, False)
    root_path = FileOrFolder(path, True)

    for sub_path in os.listdir(path):
        sub_file_path = os.path.join(path, sub_path)
        root_path.addChild(buildFileTree(sub_file_path))

    return root_path


if __name__ == '__main__':
    unifiedPath = getUserInput()
    fileTree = buildFileTree(unifiedPath)
    fileTree.print_structure()
