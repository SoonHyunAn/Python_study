import smtplib
from account import *
from email.message import EmailMessage

EMAIL_ADDRESS = "ash7106@gmail.com" # 주소
EMAIL_PASSWORD = "eoir tpwf akzh chpm" # 앱 비밀번호

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다" # 제목
msg["From"] = EMAIL_ADDRESS # 보내는 사람
msg["To"] =  EMAIL_ADDRESS # 받는 사람
msg.set_content("다운로드 하세요")

#MIME Type
#msg.add_attachment() 첨부파일 등록
with open("test.png", "rb") as f:
    msg.add_attachment(f.read(), maintype="image", subtype="png", filename=f.name)

with open("test.pdf", "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=f.name)

with open("test.xlsx", "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename=f.name)

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)