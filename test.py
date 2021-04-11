from datetime import datetime
import time
import os

cls = lambda: os.system('cls')


while True:
    now = datetime.now()
    
    if (now.month==1 and now.day==25 and now.hour==21 and now.minute==21 and now.second==00):
        cls()
        print('Happy Birthday', end='', flush=True)
        break
    print("\r%s:%s:%s" % (now.hour, now.minute, now.second), end='',flush=True)
    time.sleep(1)

