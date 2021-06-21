def mail():
    
    import smtplib as s
    ob=s.SMTP("smtp.gmail.com",587)

    ob.starttls()

    ob.login("smankind333@gmail.com","SHAILESH@1234")

    subject="sending email using python"
    body="I am Shailesh"

    message="subjest:{}\n\n{}".format(subject,body)
    listOfAddress=["gondshailesh0000@gmail.com"]
    ob.sendmail("smankind333",listOfAddress,message)
    print("Send Successful")
    ob.quit()          
    
