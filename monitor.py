#!/usr/bin/python
#-*- coding:UTF-8 -*-
import wmi,smtplib,time
from email.mime.text import MIMEText
from email.header import Header

worker={tuple(range(1,100)):'SGSCLD-PX65N0',tuple(range(1,11)):'SGSCLD-MX65N0',tuple(range(1,9)):'SGSCLD-OX65N0'}
sender = 'xxxxxxxx@send-example.com'
receiver = 'xxxxxxxx@rec-example.com'
subject = 'Citrix Wrong'
smtpserver = 'smtp.139.com'
port=25
username = 'username'
password = 'password'

def send_mail(message):
    try:
        msg = MIMEText(message,'text','utf-8') 
        msg['Subject'] = Header(subject, 'utf-8') 
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver,port)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.close()
        return True
    except:
        return None

def get_disk(compute=None):
    try:
        Process=wmi.WMI(compute)
        disks=Process.win32_LogicalDisk(Name='D:')
        UseSpace=float(disks[0].Size) - float(disks[0].FreeSpace)
        Useage=100*UseSpace/float(disks[0].Size)
        return '%.2f' %Useage
    except:
        return None

def wrong():
    for group in worker:
        for num in group:
            compute=worker[group]+'%02d' %num
            if float(get_disk(compute)) >= 90:
                message='Server %s WriteCache disk usage wrong .... ' % compute
                send_mail(message)

if __name__ == '__main__':
    wrong()