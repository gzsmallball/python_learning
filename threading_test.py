import threading
import time

exitflag = 0

class mythread(threading.Thread):
	def __init__(self,threadID,name,counter,delay):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
		self.delay = delay
	
	def run(self):
		print('start thread : ' + self.name)
		print_time(self.name,self.counter,self.delay)
		print('exit thread : ' + self.name)
	
def print_time(threadName,counter,delay):
	while counter:
		if exitflag:
			threadName.exit
		
		time.sleep(delay)
		print('%s : %s' %(threadName,time.ctime(time.time())))
		counter -= 1

thread1 = mythread(1,'thread-1',2,3)
thread2 = mythread(2,'thread-2',2,2)

thread1.start()
thread2.start()

thread1.join(2)
thread2.join()

print('exit the main process : ' + threading.currentThread().getName())