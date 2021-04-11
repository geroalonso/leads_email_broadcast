import csv
import smtplib, ssl
import time 


with open("leads.csv", "r") as f:
	reader = csv.DictReader(f)
	contact_info = list(reader)

print(contact_info)



for i in contact_info:
	try:
		message = ''' Hello ''' + i['firstname'] + ''', Im writting as I have updates and a special offer regarding the office spaces
		in Plantation Inn Plaza in which you were interested. We have added and remodelled a new wing with available executive suites.
		The offices have access to a shared waiting lounge, include utilities and internet, and medical uses as well as beauty salons are 
		welcome! We are offering two months of rent abatement period. If you are still searching for a space, let me know and we'll arrange a showing
		at your convenience. \n Veronica.


		'''



		port = 465  # For SSL
		smtp_server = "smtp.gmail.com"
		sender_email = "leasingibericmalls@gmail.com"  # Enter your address
		email = i['emailaddress']
		password = ''
		phone_number = i['phonenumber']


		context = ssl.create_default_context()
		with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
			server.login(sender_email, password)
			server.sendmail(sender_email, email, message)

		print(email, message)
		time.sleep(5)

	except:
		continue










