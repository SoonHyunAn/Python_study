# 제목 : 파이썬 특강 신청합니다.
# 본문 : 닉네임/전화번호 뒤 4자리 (Random)
#    (예) 나도코딩/1234


from imap_tools import MailBox


EMAIL_ADDRESS = "ash7106@gmail.com" # 주소
EMAIL_PASSWORD = "eoir tpwf akzh chpm" # 앱 비밀번호

applicant_list = [] # 지원자 리스트

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    index = 1 # 순번
    for msg in mailbox.fetch('(SENTSINCE 19-Sep-2023)'): # 2023년 10월 19일 이후로 온 메일 조회
        if "파이썬 특강" in msg.subject:
            nickname, phone = msg.text.strip().split("/") #공백 제거 후 "/"기준으로 잘라서 저장
            print("순번 : {} /닉네임 : {} /전화번호 : {}".format(index, nickname, phone))
            applicant_list.append((msg, index, nickname, phone))
            index += 1

# for applicant in applicant_list:
#     print(applicant)
