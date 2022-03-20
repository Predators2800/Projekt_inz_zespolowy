from datetime import datetime
import os

#dir(os)                        # return attributes and methods of an 'os' module

#os.getcwd()                    # return current working directory

#os.chdir('type path here')     # change current working directory

#os.listdir()                   # return list of all files and directories in the specified directory - can specify path as parameter

#os.makedir()                   # create a directory
#os.makedirs()

#os.rmdir()
#os.removedirs()

#os.rename()

#os.stat('requirements.txt')    # return file/folder attributes and statistics
#mod_time = os.stat('requirements.txt').st_mtime
#print(datetime.fromtimestamp(mod_time))

#os.walk()
for dirpath, dirnames, filenames in os.walk('C:\\Users\\lukas\\IPZ'):
    for filename in filenames:
        print('Current path:', dirpath + '\\' + filename)
#     print('Directories: ', dirnames)
#     print('Files: ', filenames, '\n')

