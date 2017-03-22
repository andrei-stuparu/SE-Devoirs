"""
Le premier prgramme en Python
* utilisation des arguments de la lignne de commande
* les processus
* le logger
@author Stuparu Andrei
@date 22.mar.2017
"""

import time
import random
import logging
import sys, os
import multiprocessing
from multiprocessing import Process, Queue, current_process, freeze_support


def worker(input, output):
    for func, args in iter(input.get, 'STOP'):
        result = execute_function(func, args)
        output.put(result)

def execute_function(func, args):
    result = func(args)
    return '%s says that %s %s = %s' % \
        (current_process().name, func.__name__, args, result)

def dites_bonjour(personne):
    return "Bonjour " + personne + " !"
    
def utilisation():
    NUMBER_OF_PROCESSES = 4
    TASKS1 = []
    TASKS2 = []
    TASKS3=[]
    
    task_queue = Queue()
    done_queue = Queue()

    file =  open("Liste_Noms.txt", 'r')
    
    for ligne in file:
        if ligne[0:2] == "M.":
            TASKS3.append((dites_bonjour, (ligne.strip(' \r\n'))))
        if ligne[0:4] == "Mme.":
            TASKS2.append((dites_bonjour, (ligne.strip(' \r\n'))))
        if ligne[0:5] == "Mlle.":
            TASKS1.append((dites_bonjour, (ligne.strip(' \r\n'))))
    

def main(argv=None):
    working_dir = os.path.dirname(os.path.abspath(__file__)) + os.path.sep
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                        filename=working_dir + 'process.log',
                        level=logging.INFO)
    logging.info("Main start")

    if argv is None:
        argv = sys.argv

    if len(argv) == 1:
        utilisation()
        return 0
    
    NUMBER_OF_PROCESSES = 4
    TASKS1 = []
    TASKS2 = []
    TASKS3=[]
    
    task_queue = Queue()
    done_queue = Queue()

    with open(working_dir+argv[1], 'r') as f:
         for ligne in f:
            if ligne[0:2] == "M.":
               TASKS3.append((dites_bonjour, (ligne.strip(' \r\n'))))
            if ligne[0:4] == "Mme.":
                TASKS2.append((dites_bonjour, (ligne.strip(' \r\n'))))
            if ligne[0:5] == "Mlle.":
                TASKS1.append((dites_bonjour, (ligne.strip(' \r\n'))))
                
   
    for task in TASKS1:
        logging.info(task)
        task_queue.put(task)

    for i in range(NUMBER_OF_PROCESSES):
        Process(target=worker, args=(task_queue, done_queue)).start()

    for i in range(len(TASKS1)):
        logging.info(done_queue.get())

        

    for task in TASKS2:
        logging.info(task)
        task_queue.put(task)

    for i in range(len(TASKS2)):
        logging.info(done_queue.get())

        
    
    for task in TASKS3:
        logging.info(task)
        task_queue.put(task)
        
    for i in range(len(TASKS3)):
        logging.info(done_queue.get())

    for i in range(NUMBER_OF_PROCESSES):
        task_queue.put('STOP')
        
    logging.info("Main stop")
    return 0

if __name__ == '__main__':
    freeze_support()
    sys.exit(main())
