import csv
from tabulate import tabulate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import database
def Mail() :
    listinfo=[]
    list= database.MongoData()
    for oneInfo in list :
        listinfo.append(oneInfo)
    title=['ID:','COLLEGE','URL','APPLICATION LAST DATE']
    listinfo.insert(0,title)
    #print(listinfo)
    me = 's.mukul0306@gmail.com'
    password = 'mukuls6480'
    server = 'smtp.gmail.com:587'
    you = 'kabita@iiitmanipur.ac.in'
    data= "Title  Date  URL \n IIITManipur  30 may 2019  iiitmanipur.ac.in \n"
    text = """

    
    Internship Details:
    
    {table}
    
    Regards,
    
    Me"""

    html = """
    <html><body><p></p>
    <p><b>InternInfo:</b></p>
    {table}
    <p>Regards,</p>
    <p>Me</p>
    </body></html>
    """



    text = text.format(table=tabulate(listinfo, headers="firstrow", tablefmt="grid"))
    html = html.format(table=tabulate(listinfo, headers="firstrow", tablefmt="html"))


    message = MIMEMultipart(
        "alternative", None, [MIMEText(text), MIMEText(html,'html')])

    message['Subject'] = "Internship Information"
    message['From'] = me
    message['To'] = you
    server = smtplib.SMTP(server)
    server.ehlo()
    server.starttls()
    server.login(me, password)
    server.sendmail(me, you, message.as_string())
    server.quit()

