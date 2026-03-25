import threading 
def display():
    print("hello from thread")
t1=threading.Thread(target=display)
t1.start()
t1.join()
print("thread end")