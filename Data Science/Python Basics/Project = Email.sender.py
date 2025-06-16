import smtplib
try:
    server = smtplib.SMTP("smtp.gmail.com",port=587)
    server.starttls() #sever start karne ke liye function hai
    
    ##receiver email
    receiver_mail = input("Enter the receiver email : ")
    
    #email credentials
    sender_email = "naitiksharma2403@gmail.com"
    password = ("qhpv fgtq wlsq sgzp") #crome app password se one time ke liye password add kiya 

    #Login
    server.login(sender_email,password)

    #sending email
    subject = input("Enter the subject:")
    body = input("Enter the body:")
    message = f"subject : {subject} \n\n {body}"
    server.sendmail(sender_email,receiver_mail,message)
    print("mail sent successfully")

    server.quit()
except Exception as e:
     print("An error accured",e)
