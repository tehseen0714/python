import threading
def task(name):
    print("executing:",name)
t1=threading.Thread(target=task,args=("thread 1",))
t2=threading.Thread(target=task,args=("thread 2",))
t1.start()
t2.start()
t1.join()
t2.join()