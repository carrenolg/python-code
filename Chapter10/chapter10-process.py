import os
import subprocess
import multiprocessing
import time


# create a Process with multi-processing
def do_this(what):
    whoami(what)


def whoami(what):
    print("Process %s says: %s" % (os.getpid(), what))


def loopy(name):
    whoami(name)
    start = 1
    stop = 1000000
    for item in range(start, stop):
        print("\tNumber %s of %s. Honk!" % (item, stop))
        time.sleep(1)


if __name__ == '__main__':
    whoami("I'm the main program")
    for n in range(4):
        p = multiprocessing.Process(target=do_this, args=("I'm function %s" % n,))
        p.start()

    # kill process
    whoami('main')
    p2 = multiprocessing.Process(target=loopy, args=("loopy",))
    p2.start()
    time.sleep(5)
    p2.terminate()
