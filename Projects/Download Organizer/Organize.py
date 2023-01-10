"""

This is a program that is designed to organize the contents of a folder 
by assigning files with specific Extensions to specific folders. The program 
is made with the purpose of organizing the windows download-folder, but it 
can be used for any folder by changing the DirectoriesPath variable. The Directories 
dictionary in the main specifies the names of the folders as well as the file Extensions 
that should be assigned to those folders. You can change this dictionary to suit your needs.


"""

import os
import shutil
import sys
from time import sleep


def CreateFolders(Directories, DirectoriesPath):
    """
    The CreateFolders function creates the folders in directory_path 
    where the files will be moved to. It takes in a dictionary of directories 
    containing the names of the sorted folders and the extensions that correspond 
    to those folders and a string directory_path of the path to the directory that 
    is to be sorted. It creates a folder for each key in directories if it does not 
    already exist in directory_path and creates a folder called "OTHER" if it does not 
    already exist.
    """

    for Key in Directories:
        if Key not in os.listdir(DirectoriesPath):
            os.mkdir(os.path.join(DirectoriesPath, Key))
    if "OTHER" not in os.listdir(DirectoriesPath):
        os.mkdir(os.path.join(DirectoriesPath, "OTHER"))


def OrganizeFolders(Directories, DirectoriesPath):
    """
    The OrganizeFolders function organizes the files in the specified folder into folders. 
    It takes in a dictionary of directories containing the names of the sorted folders and 
    the extensions that correspond to those folders and a string directory_path of the path 
    to the directory that is to be sorted. It iterates through the files in directory_path 
    and checks if each file ends with an extension in directories. If it does, it moves the 
    file to the corresponding folder.
    """

    for file in os.listdir(DirectoriesPath):
        if os.path.isfile(os.path.join(DirectoriesPath, file)):
            SRCPath = os.path.join(DirectoriesPath, file)
            for Key in Directories:
                Extension = Directories[Key]
                if file.endswith(Extension):
                    DestinationPath = os.path.join(DirectoriesPath, Key, file)
                    shutil.move(SRCPath, DestinationPath)
                    break


def OrganizeRemainingFiles(DirectoriesPath):

    """
    The OrganizeRemainingFiles function assigns the files that do not have a 
    corresponding folder to the "OTHER" directory. It takes in a string directory_path 
    of the path to the directory that is to be sorted. It iterates through the files in 
    directory_path and moves them to the "OTHER" folder.
    """

    for file in os.listdir(DirectoriesPath):
        if os.path.isfile(os.path.join(DirectoriesPath, file)):
            SRCPath = os.path.join(DirectoriesPath, file)
            DestinationPath = os.path.join(DirectoriesPath, "OTHER", file)
            shutil.move(SRCPath, DestinationPath)


def OrganizeRemainingFolders(Directories, DirectoriesPath):

    """
    The OrganizeRemainingFolders function assigns the folders within the specified directory 
    to the "FOLDERS" directory. It takes in
    """

    list_dir = os.listdir(DirectoriesPath)
    organized_folders = []

    for folder in Directories:
        organized_folders.append(folder)

    organized_folders = tuple(organized_folders)
    for folder in list_dir:
        if folder not in organized_folders:
            SRCPath = os.path.join(DirectoriesPath, folder)
            DestinationPath = os.path.join(DirectoriesPath, "FOLDERS", folder)
            try:
                shutil.move(SRCPath, DestinationPath)
            except shutil.Error:
                shutil.move(SRCPath, DestinationPath + " - copy")
                print("That folder already exists in the destination folder."
                      "\nThe folder is renamed to '{}'".format(folder + " - copy"))


if __name__ == '__main__':

    DirectoriesPath = "C:/Users/dhruv/Downloads"
    Directories = {

        

        "IMAGES":       (".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",".heif", ".psd"),

        "VIDEOS":       (".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob",  ".mng", ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"),
        
        "DOCUMENTS":    (".pdf", ".txt", ".in", ".out", ".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", "pptx"), "HTML": (".html5", ".html", ".htm", ".xhtml"),
        
        "ARCHIVES":     (".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xar", ".zip"),
        
        "AUDIO":        (".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"),
        
        "PYTHON":       (".py"),
        
        "EXE":          (".exe"),
        
        "OTHER":        (""),
        
        "FOLDERS":      ("")
    }
    
    try:
        print("Organizing Download Folder...")
        CreateFolders(Directories, DirectoriesPath)
        OrganizeFolders(Directories, DirectoriesPath)
        OrganizeRemainingFiles(DirectoriesPath)
        OrganizeRemainingFolders(Directories, DirectoriesPath)
        sleep(2)
        print("Download Folder Organized")
    except shutil.Error:
        print("There was an error trying to move an item to its destination folder")
