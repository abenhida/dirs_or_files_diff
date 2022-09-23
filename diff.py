import os
import sys
from difflib import Differ


def compareDirs(dir1path, dir2path):
    # Determine the items that exist in both directories.
    dir1_contents = set(os.listdir(dir1path))
    dir2_contents = set(os.listdir(dir2path))

    MissingIndir2 = [x for x in dir1_contents if x not in dir2_contents]
    MissingIndir1 = [x for x in dir2_contents if x not in dir1_contents]
    HaveInCommon = [x for x in dir1_contents if x in dir2_contents]

    print(f'Error, Files not in {dir1path}:{MissingIndir1}')
    print(f'Error, File not in {dir2path}:{MissingIndir2}')
    print(f'HaveInCommon:{HaveInCommon}')
    return MissingIndir2, MissingIndir1, HaveInCommon
    # return  HaveInCommon


'''
compare the content of files in two directories
'''


def compareFilesInTwoDirs(HaveInCommon, dir1path, dir2path):
    cwd = os.getcwd()
    os.chdir(dir1path)
    for f in HaveInCommon:
        with open(f'{dir1path}/{f}') as f1, open(f'{dir2path}/{f}') as f2:
            differ = Differ()
            diff_result = f2has = []
            for line in differ.compare(f1.readlines(), f2.readlines()):
                diff_result.append(line)

            print(f'--------- ---------  ---------  ---------  --------- ---------')
            print(f'--------->  {dir1path}/{f}, missing ')
            [print(l) for l in diff_result if l.startswith("+")]
            print(f'--------->  {dir2path}/{f}, missing ')
            [print(l) for l in diff_result if l.startswith("-")]
        f1.close()
        f2.close()

    os.chdir(cwd)


'''
compare two files and report if they have same content (lines order does not matter
'''


def compareTwoFiles(path_to_file1, path_to_file2):
    with open(f'{path_to_file1}') as f1, open(f'{path_to_file2}') as f2:
        differ = Differ()
        diff_result = f2has = []
        for line in differ.compare(f1.readlines(), f2.readlines()):
            diff_result.append(line)

        print(f'--------- x --------- x --------- x --------- ')
        print(f'--------->  {path_to_file1}, missing ')
        [print(l) for l in diff_result if l.startswith("+")]
        print(f'--------->  {path_to_file2}, missing ')
        [print(l) for l in diff_result if l.startswith("-")]
    return diff_result



def readInput(type, n):
    if type == "file":
        path_to_file = input(f'Enter file Name #{n} path -- two \\ instead of one \:')

        if not os.path.isfile(path_to_file):
            print(f'you entered wrong file:{path_to_file}')
            sys.exit(0)
        return path_to_file

    if type == "dir":
        path_to_dir = input(f'Enter dir #{n} path:')
        if not os.path.isdir(path_to_dir):
            print(f'you entered wrong dir path:{path_to_dir}')
            sys.exit(0)
        return path_to_dir

    return 0


# -----------
if input('Compare Files or 2 Dirs? (f/d) -- two \\ instead of one \:').upper() == 'F':
    path_to_file1 = readInput("file", 1)
    path_to_file2 = readInput("file", 2)
    compareTwoFiles(path_to_file1, path_to_file2)
else:
    path_to_dir1 = readInput("dir", 1)
    path_to_dir2 = readInput("dir", 2)
    MissingIndir2, MissingIndir1, HaveInCommon = compareDirs(path_to_dir1, path_to_dir2)
    compareFilesInTwoDirs(HaveInCommon, path_to_dir1, path_to_dir2)
