class Queue:
    def __init__(self):
        self.queue = list()

    def addtoq(self,dataval):
        if dataval not in self.queue():
            self.queue.insert(0,dataval)
            return True
        return False
    
    def size(self):
        return len(self.queue)


TheQueue = Queue()
TheQueue.addtoq("mon")
TheQueue.addtoq("tue")
TheQueue.addtoq("wed")
print(TheQueue.size())
    