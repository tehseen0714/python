import threading
def show():
 print(threading.current_thread().name)
t1=threading.Thread(target=show,name="mythread")
t1.start()
t1.join()