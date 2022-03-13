import json
import boto3
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

SNS_client = boto3.client('sns')


def EmailMessageString(FullEvent):
    eventName = FullEvent['detail']['eventTypeCode']
    startTime = FullEvent['detail']['startTime']
    Description = FullEvent['detail']['eventDescription'][0]['latestDescription']
    EmailMessageString0 = " Hi Team, <br> <br>"
    EmailMessageString1 = " This is an informational message from Personal Health Dashboard.\n <br> <br> "
    EmailMessageString2 = " Event [ " + str(eventName) +  "] is scheduled at [" + str(startTime) + "] and the description as follows, \n <br> <br> <br>" 
    EmailMessageString3 =  str(Description) 
    EmailMessageString = EmailMessageString0 + EmailMessageString1 + EmailMessageString2 + EmailMessageString3
    print(EmailMessageString)
    return EmailMessageString 

def lambda_handler(event, context):
    EventMessage = EmailMessageString(event)
    sender = os.environ["sender"]
#    receivers = ['individual_mailid@optum.com','distribution_List@ds.uhc.com']
    mail_receivers = os.environ["mail_receivers"]
    receivers = mail_receivers
    print(receivers)
    msg = MIMEMultipart()
    msg['Subject'] = 'Personal Health Dashboard Notification'
    msg_body = EventMessage
    msg.preamble = 'Multipart message.\n'
    part = MIMEText(str(msg_body), 'html')
    msg.attach(part)
    
    print("--> Function started")
    print(event)
    
    print (EventMessage)
    smtpObj = smtplib.SMTP("omail.o360.cloud", 587)
    smtpObj.starttls()

    ssm = boto3.client('ssm')
    credentials = ssm.get_parameter(Name='AzureSMTP', WithDecryption=True)
    cred = credentials['Parameter']['Value']
    
    x = cred.split(":")
    username = x[0]
    password = x[1]
#   smtpObj.login("Azure SMTP user name","Azure SMTP password")    
    
    smtpObj.login(username,password)
    smtpObj.sendmail(sender, receivers, msg.as_string())
    smtpObj.quit()
    print ("Successfully sent email")
    print("--> Function Ran Successfully")
