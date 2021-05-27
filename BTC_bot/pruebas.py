import schedule
import time

def job():
    print("I'm working...")

# minutes = list(range(0,61,2))
# print(minutes)
# for minute in minutes:
#     if minute < 10:
#         h = ':0' + str(minute)
#     else:
#         h = ':'+str(minute)
#     print(h)
#     schedule.every().hour.at(h).do(job)
schedule.every(2).minutes.do(job)

# schedule.every().hour.at(":25").do(job)
# schedule.every().day.at("13:25").do(job)
# # schedule.every().minute.at(":").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)