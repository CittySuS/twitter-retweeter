import keep_alive
import time, os
import threading
def d():
  while True:
    os.system("python tw.py")
    time.sleep(450)

t1 = threading.Thread(target=d, args=())
t1.start
keep_alive.keep_alive()
