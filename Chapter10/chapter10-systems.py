import os
import shutil
import stat
import glob
import subprocess
import multiprocessing
import time
import calendar


def main():
    print('#### main function ###')
    print('############################## Files')
    fout = open('oops.txt', 'wt')
    print('Oops, I created a file.', file=fout)
    # Check Existence with exists()
    print(os.path.exists('oops.txt'))  # True
    print(os.path.exists('oops.txt'))  # True
    print(os.path.exists('waffles.txt'))  # False
    print(os.path.exists('..'))  # True
    print(os.path.exists('../..'))  # True
    # Check Type with isfile()
    print(os.path.isfile('oops.txt'))  # True
    # check whether file path is an absolute pathname
    print(os.path.isabs('/home/gio10'))  # True
    print(os.path.isabs('oops.txt'))  # False

    # copy and move files
    shutil.copy('oops.txt', 'oops2.txt')
    # os.link('oops.txt', 'yikes.txt')
    print(os.path.isfile('yikes.txt'))  # True
    print(os.path.islink('yikes.txt'))  # True
    # os.symlink('oops.txt', 'jeepers.txt')
    print(os.path.islink('jeepers.txt'))  # True
    os.rename('oops2.txt', 'new-oops2.txt')

    # Change Permissions with chmod()
    # For instance, only readable by its owner
    # os.chmod('oops.txt', '0o400')
    # change owner
    uid = 5
    gid = 10
    # os.chown('oops.txt', uid, gid)
    # get pathname with abspath()
    print(os.path.abspath('new-oops2.txt'))
    print(os.path.realpath('jeepers.txt'))

    # Delete files
    os.remove('new-oops2.txt')
    print(os.path.exists('new-oops2.txt'))  # True
    print('############################## Directories')
    # create directories
    if not os.path.exists('poems'):
        os.mkdir('poems')
    print(os.path.exists('poems'))  # True
    # os.rmdir('poems')
    print(os.path.exists('poems'))  # False

    # list content of one directory
    if not os.path.exists('poems'):
        os.mkdir('poems')
    # print(os.listdir('poems'))  # [], None
    if not os.path.exists('poems/mcintyre'):
        os.mkdir('poems/mcintyre')
    print(os.listdir('poems'))
    fout = open('poems/mcintyre/the_good_man', 'wt')
    fout.write('''
    Cheerful and happy was his mood,
    He to the poor was kind and good,
    And he oft' times did find them food,
    Also supplies of coal and wood,
    He never spake a word was rude,
    And cheer'd those did o'er sorrows brood,
    He passed away not understood,
    Because no poet in his lays
    Had penned a sonnet in his praise,
    'Tis sad, but such is world's ways.
    ''')
    fout.close()
    print(os.listdir('poems/mcintyre'))
    os.chdir('poems')
    print(os.listdir('..'))

    # list matching files with glob()
    print(glob.glob('m*'))

    # Process
    pid = os.getpid()
    print(pid)
    gid = os.getgid()
    print(gid)

    ret = subprocess.getoutput('ls')
    print(ret)

    # run linux commands from python
    ret = subprocess.getoutput('date -u | wc')
    print(ret)
    # another method "check_output"
    ret = subprocess.check_output(['date', '-u'])
    print(ret)
    # show status of the process/program
    ret = subprocess.getstatusoutput('date')
    print(ret)
    # run program with arguments in two ways
    # 1st way
    ret = subprocess.call('date -u', shell=True)
    print(ret)
    # 2st way
    ret = subprocess.call(['date', '-u'])
    print(ret)

    # Calendars and clocks
    print(calendar.isleap(1990))
    print(calendar.isleap(1996))


if __name__ == '__main__':
    main()
