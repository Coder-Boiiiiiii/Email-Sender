import smtplib

sender_email = str(input("Please enter your email: "))
print(" ")
password = str(input("Please enter your email password: "))
print(" ")

Receiver_Email = str(input("Please enter the email of the reciever: "))
print(" ")
message = str(input("Please enter the message you want to deliver: "))
print(" ")

server = smtplib.SMTP("smtp.gmail.com", 587)
print("Connecting...")
server.starttls()
print("Connected!")
server.login(sender_email, password)
print("Logging you in...")
print("Logged in!")

server.sendmail(sender_email, Receiver_Email, message)
print("Email sent!")
