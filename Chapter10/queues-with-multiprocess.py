# Process
# Implement queues
# dishes.py
import multiprocessing as mp
import os


def washer(dishes, queue):
    print("Process %s (washer)" % (os.getpid()))
    for dish in dishes:
        print('Washing', dish, 'dish')
        queue.put(dish)


def dryer(queue):
    print("Process %s (dryer)" % (os.getpid()))
    while True:
        dish = queue.get()
        print('Drying', dish, 'dish')
        queue.task_done()


# Create a queue
dish_queue = mp.JoinableQueue()

# Init dryer
dryer_proc = mp.Process(target=dryer, args=(dish_queue,))
dryer_proc.daemon = True
dryer_proc.start()


# Init washer
dishes = ['salad', 'bread', 'entree', 'dessert']
washer(dishes, dish_queue)
dish_queue.join()




