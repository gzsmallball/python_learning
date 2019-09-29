import threading
import queue
import time

exitFlag = 0 

class myThread(threading.Thread):
	def __init__(self,threadID,name,q):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.q = q
	
	def run(self):
		print('start thread : ' + self.name)
		process_data(self.name,self.q)		
		print('exit thread : ' + self.name)

def process_data(name,q):
	try:
		while not exitFlag:
			queueLock.acquire()
			if not q.empty():
				data = q.get()
				queueLock.release()
				print('%s processing %s' %(name,data))
			else:
				queueLock.release()
	except AttributeError:
		queueLock.release()
	
	time.sleep(1)

threadList = ['t1','t2','t3','t4','t5']
nameList = ['1','2','3','4','5','6','7','8','9']

queueLock = threading.Lock()
workQueue = queue.Queue(10)

threads = []
threadID = 1

for tName in threadList:
	thread = myThread(threadID,tName,workQueue)
	thread.start()
	threads.append(thread)
	threadID += 1
	
queueLock.acquire()
for word in nameList:
	workQueue.put(word)
queueLock.release()

while not workQueue.empty():
	pass

exitFlag = 1

for t in threads:
	t.join()


print('\n')
print('exit main thread')
	
	
	
	