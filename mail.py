# -*- coding: utf-8 -*-
# python 发邮件简单demo, 只有安装了sendmail才能work
from os import path
import sys
import subprocess
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os


def send_mail(sender, receiver, title, body):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = title
    msg.attach(MIMEText(body,'html','utf-8'))

    #send 调用了系统的/usr/lib/sendmail 发邮件
    proc = subprocess.Popen(['/usr/lib/sendmail','-t'],stdin = subprocess.PIPE)
    proc.stdin.write(str(msg))
    proc.stdin.close()

def main():
    sender = 'xsb_test@test.com'
    date = os.popen('date').read()
    title = 'xsb test mail'
    receiver = 'xishengbo@baidu.com'
    body = '<h1>fuck you</h1>'
    send_mail(sender, receiver, title, body)


if __name__ == '__main__':
    main()