#!/usr/bin/env python
# coding: utf-8

# Q1: shutil.copy(): copies a file & shutil.copytree(): copies the whole folder and whatever inside it.

# Q2: rename()

# Q3: send2trash will send the file to recycle bin while shutil will permanently delete the file.

# Q4: The zipfile. ZipFile() function is equivalent to the open() function; the first argument is the filename, and the second argument is the mode to open the ZIP file in (read, write, or append).

# Q5: import os, shutil
# 
# def selectiveCopy(folder, extensions, destFolder):
# 	folder = os.path.abspath(folder)
# 	destFolder = os.path.abspath(destFolder)
# 	print('Looking in', folder, 'for files with extensions of', ', '.join(extensions))
# 	for foldername, subfolders, filenames in os.walk(folder):
# 		for filename in filenames:
# 			name, extension = os.path.splitext(filename)
# 			if extension in extensions:
# 				fileAbsPath = foldername + os.path.sep + filename
# 				print('Coping', fileAbsPath, 'to', destFolder)
# 				shutil.copy(fileAbsPath, destFolder)
# 
# extensions = ['.php', '.py']
# folder = 'randomFolder'
# destFolder = 'selectiveFolder'
# selectiveCopy(folder, extensions, destFolder)
