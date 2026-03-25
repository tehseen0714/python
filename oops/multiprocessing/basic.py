from multiprocessing import Process
def print_numbers():
    for i in range(5):
        print("numbers:",i)
 
if __name__=="__main__":
    p=Process(target=print_numbers)
    p.start()
    p.join
    print("process finished")