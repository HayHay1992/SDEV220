import multiprocessing,time,datetime
 
def process1():
    t1 = random.randint(0,1)
    print("Waiting for "+str(t1)+" seconds")
    time.sleep(t1)
    print(datetime.datetime.now())


start = time.time()
process1 = zoo.process1()
process2 = zoo.process1()
process3 = zoo.process1()

print(datetime.datetime.now())
if __name__=="__main__":
    
    
    
    p1 = multiprocessing.Process(target=process1)
    p2 = multiprocessing.Process(target=process2)
    p3 = multiprocessing.Process(target=process3)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

end = time.time()
