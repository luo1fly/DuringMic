#!/usr/bin/env python
#FileName:ping.py
#author:luo1fly

import urllib2
import subprocess
import smtplib
from email.mime.text import MIMEText

#ping host
cmd = 'ping -c4 116.6.101.196 >/dev/null 2>&1'
#send list
mailto_list=["yifei.luo@epro.com.cn",]

#MTA config
mail_host = "mail.epro.com.cn"
mail_user = ""
mail_pass = ""
mail_postfix="epro.com.cn"

#mail send func
def send_mail(to_list, sub, content):
	me = mail_user + "<"+mail_user+"@"+mail_postfix+">"
	msg = MIMEText( content,_charset="utf-8" )
	msg['Subject'] = sub
	msg['From'] = me
	msg['To'] = ";".join(to_list)
	try:
		send_smtp = smtplib.SMTP()
		send_smtp.connect(mail_host)
		send_smtp.login(mail_user, mail_pass)
		send_smtp.sendmail(me, to_list, msg.as_string())
		send_smtp.close()
		return True
	except Exception, e:
		print str(e)
		return False


if __name__ == '__main__':
	retcode = subprocess.call(cmd,shell=True)
	if not retcode:
		pass
        else:
                text = 'shenzhen server room ping status(%d) abnormal, please double check manually!' % retcode
                sub = 'ping sz warning'
                send_mail(mailto_list,sub,text)