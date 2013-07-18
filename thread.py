import os
import datetime
from multiprocessing import Process, Queue
from Queue import Empty
import time

curdate = str(datetime.datetime.now())
curdate = curdate[:10].replace("-", "")

logFile = '/data/yelp/logs/store_'+curdate+'.log'


#state = ('nv',)		
state = ('nv','ne','nd','nc','nm','ny','nj','nh','de','ri','la','ma','md','me','mt','mn','mi','ms','mo','vt','va','sd','sc','id','ia','ar','ak','az','al','or','ok','oh','wy','wa','wv','wi','ut','in','il','ga','ks','ca','ky','ct','co','tn','tx','pa','fl','hi')


def do_work(q, loc):
	
	z = 0
	
	while z<500:
		try:
			
			f = open(logFile, 'a')
	
			url_params = '-l="'+loc+'" -q="food" --offset='+str(z)

			#Log				
			f.write(loc+'\t'+str(z)+'\n')
		
			#Json
			os.system('python yelp.py '+url_params+' >> /data/yelp/store/'+loc+'.json')
	
			z+=1
			time.sleep(0.1)
			
		except Empty:
			break
	
		finally:
			f.close()

if __name__ == '__main__':
	work_queue = Queue()
	
	for i in range(1,50):
		work_queue.put(i)
	
	processes = [Process(target=do_work, args=(work_queue, loc, )) for loc in state]
	
	for p in processes:
		p.start()
		
	for p in processes:	
		p.join()
