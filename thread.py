import os, sys
import datetime
from multiprocessing import Process, Queue
from Queue import Empty
import time

curdate = str(datetime.datetime.now())
curdate = curdate[:10].replace("-", "")




state = ('nv',)		
#state = ('nv','ne','nd','nc','nm','ny','nj','nh','de','ri','la','ma','md','me','mt','mn','mi','ms','mo','vt','va','sd','sc','id','ia','ar','ak','az','al','or','ok','oh','wy','wa','wv','wi','ut','in','il','ga','ks','ca','ky','ct','co','tn','tx','pa','fl','hi')


def do_work(q, term, loc):
	
	z = 0
	logFile = '/data/yelp/logs/'+term+'_'+curdate+'.log'
	
	while z<1:
	#while z<500:
		try:
			
			f = open(logFile, 'a')
	
			url_params = '-l="'+loc+'" -q="'+term+'" --offset='+str(z)

			#Log				
			f.write(loc+'\t'+str(z)+'\n')
		
			#Json
			o = '/data/yelp/json/'+term+'_'+loc+'_'+str(z)+'.json'
			os.system('python yelp.py '+url_params+' >> '+o)
	
			z+=1
			time.sleep(0.1)
			
		except Empty:
			break
	
		finally:
			f.close()
			

def init_file(term):
	
	for loc in state:
		
		f = '/data/yelp/json/'+term+'_'+loc+'.json'
		print f
		os.system('rm '+f)
		
		"""
		try:
            os.system('rm /data/yelp/json/'+term+'_'+loc+'.json')
        except IOError:
            pass
        """
			
"""
def isNumber(s):
    try:
        float(s)
		return True
	except ValueError:
		return False
"""   
   
if __name__ == '__main__':
	
	term = ""
	
	if len(sys.argv) == 1:
	    print "Select option - 'restaurant' or 'food' ?"
	    exit(0)
	
	term = sys.argv[1]
		
	#init_file(term)
	
	work_queue = Queue()
	
	for i in range(1,50):
		work_queue.put(i)
	
	processes = [Process(target=do_work, args=(work_queue, term, loc, )) for loc in state]
	
	for p in processes:
		p.start()
		
	for p in processes:	
		p.join()
