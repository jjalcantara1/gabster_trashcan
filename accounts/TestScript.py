import smtplib

server = None  # Initialize server outside the try block

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('randomgab123@gmail.com', 'gice gboo dgbk hafi')
    print("SMTP Connection Successful")
except Exception as e:
    print("SMTP Connection Failed:", e)
finally:
    if server is not None:
        server.quit()
