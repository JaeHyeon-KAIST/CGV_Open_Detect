import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

def job_function():
    url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20220515'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    list = soup.select('.info-hall')

    if ('스트레인지' in html and '20220515' in html and 'IMAX' in str(list)):
        print('예매 오픈!')
        msg = MIMEText('예매 오픈!')
        msg['Subject'] = Header('예매 오픈', 'utf-8')
        msg['From'] = 'alvinlog@naver.com'
        msg['To'] = 'alvinlog@naver.com'

        with smtplib.SMTP_SSL('smtp.naver.com') as smtp:
            smtp.login('alvinlog','32673267okK')
            smtp.send_message(msg)

    day_list = []
    tmp = 0
    for i in soup.select('.day strong'):
        temp = str(i).replace("<strong>", "").replace("</strong>", "").lstrip()
        day_list.append(temp)
        temp = int(temp)
        if (tmp + 1 == temp or tmp > temp or tmp == 0):
            tmp = temp

    print(str(day_list))
    print(tmp)

    current_time = datetime.now()

    if (int(current_time.minute) % 10 == 0 and int(current_time.second) <= 5):
        msg = MIMEText(str(day_list) + '\n' + url)
        msg['Subject'] = Header('정상 작동 : 마지막 날짜' + str(tmp), 'utf-8')
        msg['From'] = 'alvinlog@naver.com'
        msg['To'] = 'alvinlog@naver.com'

        with smtplib.SMTP_SSL('smtp.naver.com') as smtp:
            smtp.login('alvinlog', '32673267okK')
            smtp.send_message(msg)

sched = BlockingScheduler()

sched.add_job(job_function, 'interval', seconds=5, max_instances=10)
sched.start()