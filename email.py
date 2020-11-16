#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:34:48 2020

@author: rajkumar
"""


import smtplib
sender_mail = input("Enter your gmail:")
receivers_mail = input("Enter receivers gmail:")
message = """From: From Person %s
To:To Person %s
Subject: Sending SMTP e-mail
This is a test e-mail message.
"""%(sender_mail,receivers_mail)
try:
    password = input('Enter the password: ');
    smtpObj = smtplib.STMP('gmail.com',587)
    smtobj.login(sender_mail,password)
    smtObj.sendmail(sender_mail, receivers_mail, message)
    print("Successfully sent mail")
    
except Exception:
    print("Error: unable to send email")