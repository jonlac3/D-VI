import smtplib
 
def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    
sendemail(from_addr    = 'enter email>', 
        to_addr_list = ['enter email>'],
        cc_addr_list = ['enter email>'], 
        subject      = 'This is a test', 
        message      = 'This is the message for the test', 
        login        = '<enter email>', 
        password     = '<enter password>')
