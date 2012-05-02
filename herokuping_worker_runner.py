from iron_worker import *

payload = {'herokuping':{'hosts':  ['over-op-sepa.herokuapp.com','mimispeelgoed.herokuapp.com','young-leaf-7580.herokuapp.com']}}

worker = IronWorker(config='config.ini')

name = "heroku-pinger"
zipFile = IronWorker.createZip(files=["herokuping_worker.py"],
        destination="herokuping_worker.zip", overwrite=True)
ret = worker.postCode(name=name, runFilename="herokuping_worker.py",
        zipFilename="herokuping_worker.zip")

print str(ret)

ret = worker.postSchedule(name=name,  
        delay=10, run_every=900, run_times=300000,
        payload=payload)

print "postTask returned:  %s" % ret
#task_id = ret['tasks'][0]['id']
