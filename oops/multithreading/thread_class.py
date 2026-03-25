import threading 
class mythread(threading.Thread):
    def run(self):
        print("thread using class")

t1=mythread()
t1.start()
t1.join()
