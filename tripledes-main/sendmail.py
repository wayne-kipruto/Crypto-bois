
import yagmail
username = "wayneroberto777" #Personal Email
password = "stpm uwcu itdm eosu" # App Key from email
def mail_send(receiver_email,content):
    yag = yagmail.SMTP(username,password)
    yag.send(receiver_email, 'subject', content)






# # Alternatively, with a simple one-liner:
# yagmail.SMTP('wayneroberto777').send('wayneroberto777@gmail.com', 'subject', contents)
