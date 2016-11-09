#!/usr/bin/env python
#FileName:backup_clean.py
#author luo1fly

import sys
import os
import os.path
import datetime
import shutil

path = '/img_bak'
filelist = os.listdir(path)
count = 0
period = 90

if len(filelist)==0:
	print '"'+path+'"'+" is empty"
	sys.exit(1)

for i in filelist:
        mtime = os.path.getmtime(path+os.sep+i)
        #print mtime
        formatMtime = datetime.datetime.fromtimestamp(mtime)
	#print formatMtime
        nowTime = datetime.datetime.now()
        #print nowTime
        delta = (nowTime - formatMtime).days
        if delta <= period:
                #print delta
		try:
			shutil.rmtree(path+os.sep+i)
			print "directory "+i+" has been removed"
		except:
			os.remove(path+os.sep+i)	
			print "file "+i+" has been removed"
		count+=1
        else:
		pass 
print "total remove "+str(count)+" backups"