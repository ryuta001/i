pip install schedule
サンプルコード
import datetime
import schedule
import time

def job():
  print(datetime.datetime.now())
  print("I'm working...")  

schedule.every().day.at("06:25").do(job)
  
while True:
  schedule.run_pending()
  time.sleep(60)
