import threading
import time

class mythread(threading.Thread):
	def __init__(self,threadID,name,counter,delay):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
		self.delay = delay
	
	def run(self):
		print('start thread : ' + self.name)
		threadLock.acquire()
		print_time(self.name,self.counter,self.delay)
		threadLock.release()
		print('exit thread : ' + self.name)
		
	
def print_time(threadName,counter,delay):
	while counter:
		time.sleep(delay)
		print('%s : %s' %(threadName,time.ctime(time.time())))
		counter -= 1

threadLock = threading.Lock()
threads = []

thread1 = mythread(1,'thread-1',2,3)
thread2 = mythread(2,'thread-2',2,3)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for t in threads:
	t.join()

print('exit the main process')