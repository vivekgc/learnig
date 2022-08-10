from operator import le
import sqlite3
from time import process_time_ns


class Queue:
    def __init__(self) -> None:
        self.queue = list()
    
    def addtoq(self,dataval):
        if dataval not in self.queue:
            self.queue.insert(0,dataval)
            return True
        return False
    
    def removeq(self):
        if len(self.queue)>0:
            return self.queue.pop()
        return ("No element in que")

    def size(self):
        return len(self.queue)

TheQueue = Queue()
TheQueue.addtoq("Mon")
TheQueue.addtoq("Tue")
TheQueue.addtoq("Wed")
print(TheQueue.size())
print(TheQueue.removeq())
print(TheQueue.removeq())
print(TheQueue.size())