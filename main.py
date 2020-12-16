import schedule
import time
from datetime import datetime


def job():
    print(datetime.now().strftime('%H:%M:%S | %d-%m-%Y'))


def job2():
    print("Diaria")

print("Iniciou rotinas.")
schedule.every().minute.at(":30").do(job)
schedule.every().day.at("22:51").do(job2)

# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
