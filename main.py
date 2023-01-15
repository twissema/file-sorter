import os
import shutil
import logging
import glob
srcVar = input("Please input the target folder: \n")
src = glob.glob(srcVar + "/**/*.*", recursive=True)
fileloc = ''
tfile = ''
tfolder = ''


# main function that takes the current trajectory and renames and moves files to the proper folder
def main():
    try:
        for i in src:
            if i.endswith("Default_Extended.txt"):
                dirsplit = i.split('/')
                global tfile
                global tfolder
                global fileloc
                fileloc = i
                tfile = dirsplit[-1]
                tfolder = dirsplit[-2]
                RenameAndMove()
                DeleteOldFolders()
    except:
        logging.exception("try again, sweaty")
        return


# renames the file to cohort standards
def RenameAndMove():
    folder = tfolder.split('-')
    AAWsplit = folder[0].split(' ')
    annotiationsplit = folder[-1].split(' ')
    try:
        path = os.path.join(srcVar, f'{srcVar}/{AAWsplit[0]}')
        if not os.path.exists(path):
            os.mkdir(path)
        if AAWsplit[-1].startswith('AAW'):
            shutil.move(fileloc, f'{srcVar}/{AAWsplit[0]}/{AAWsplit[0]}-P{annotiationsplit[-1]}')
        else:
            shutil.move(fileloc, f'{srcVar}/{AAWsplit[0]}/{AAWsplit[0]}-M{AAWsplit[-1]}_{annotiationsplit[-1]}')
    except:
        logging.exception('exception while renaming your files')

def DeleteOldFolders():
    walk = list(os.walk(srcVar))
    for path, _, _ in walk[::-1]:
        if len(os.listdir(path)) == 0:
            os.rmdir(path)

if __name__ == '__main__':
    main()
