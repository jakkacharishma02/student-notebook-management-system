# mail_password='ztan enwt cacu scbo'
import smtplib
from email.message import EmailMessage #to format mail
def send_mail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465) #creating server object using port number
    server.login('jakkacharishma02@gmail.com','ztan enwt cacu scbo')
    msg=EmailMessage()
    msg['FROM']='jakkacharishma02@gmail.com'
    msg['TO']=to
    msg['SUBJECT']=subject
    msg.set_content(body)
    server.send_message(msg) #using send_message method to send otp
    print('msg sent')
    server.close()