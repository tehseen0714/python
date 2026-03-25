from multiprocessing import Process
def square(n):
    print(f"square of {n} is P{n*n}")

if __name__=="__main__":
    processes=[]
    for i in range(5):
        p=Process(target=square,args=(i,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()