import smtplib
import getpass
import ssl

print("Welcome to mass mailer!")
path=input("Enter email file list: ")
f=open(path, "r")
emails=f.read().splitlines()

email=input("Enter your email: ")
port=input("Enter it's smtp port[Gmail has it's smtp port 587]: ")
host=input("Host server[Gmail's smtp server is smtp.gmail.com]: ")
print("Password of your email[You will have to either allow secure apps or set an app password if you are using gmail]: ")
password=getpass.getpass()

name=input("What do you want your name to be shown as?: ")
subject=input("Enter subject: ")
body=input("Enter message: ")

go=True

context=ssl.create_default_context()

while go:
	try:
		server=smtplib.SMTP(host,port)
		server.ehlo()
		print("Successfully connected to the server..")
		server.starttls(context=context)
		server.ehlo()
		print("Encryption with TLS sucessful..")
		server.login(email, password)
		go=False
	except Exception as e:
		print(f"Login failed. Error:\n {e}")
		go=True
		print("Trying again..")
print("Login successful!")

for i in emails:
	msg=f"""
From: {name} <{email}>
To: {i}
Subject: {subject}
Body: {body}
"""
	server.sendmail(email, i, msg)
server.close()




