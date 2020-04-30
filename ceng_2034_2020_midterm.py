import os
import sys
import requests
from time import perf_counter 
import threading


urls = ["https://api.github.com", "http://bilgisayar.mu.edu.tr/", "https://www.python.org/", "http://akrepnalan.com/ceng2034","https://github.com/caesarsalad/wow"]

os.system("clear")

def url_ok(urls):
    r = requests.head(url)
    if(r.status_code == 200):
        print( url , "is working\n")
    else :
        print(url , " is not working\n")


print("script PID: ",os.getpid(),"\n") # py scriptin pıd sini veriyor
print("CPU work: ",os.getloadavg(),"\n")   # işlemci yoğunluğunu (1 dk, 5 dk , 15 dk) şeklinde gösteriyor

loadavg = os.getloadavg()  #işlemci yoğunluğunu arrayı
cpu =  os.cpu_count()  # çekirdek sayısı

if (cpu-loadavg[1] < 1):
    print("suitable cpu: ",cpu-loadavg[1]) 
    print("your cpu is busy and this script was stop\n")
    sys.exit()
else:
    print("suitable cpu: ",cpu-loadavg[1]) 
    print("your cpu is OK\n") 


# LINEAR
print("Linear process: ")
time_linear_start = perf_counter()    #start time
for url in urls:
    url_ok(url)     #linear process
time_linear_end = perf_counter()   # end time
print("Linear url check time: ", time_linear_end-time_linear_start   ,"second\n") # linear process time


# THREAD
print("Thread proces: ")
time_thread_start = perf_counter()    #start time
thread0= threading.Thread(target=url_ok, args=(urls[0],))  #thread  process
thread1= threading.Thread(target=url_ok, args=(urls[1],))  #thread  process
thread2= threading.Thread(target=url_ok, args=(urls[2],))  #thread  process
thread3= threading.Thread(target=url_ok, args=(urls[3],))  #thread  process
thread4= threading.Thread(target=url_ok, args=(urls[4],))  #thread  process
thread0.start()   #thread  start
thread1.start()    #thread  start
thread2.start()    #thread  start
thread3.start()    #thread  start
thread4.start()    #thread  start
thread0.join()   
thread1.join()
thread2.join()
thread3.join()
thread4.join()
time_thread_end = perf_counter()  # end time

print("Thread url check time: ", time_thread_end-time_thread_start   ,"second") # thread process time
