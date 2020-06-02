import os
import sys
import requests
import uuid
import hashlib
from multiprocessing import Pool


cpu =  os.cpu_count()

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


url =["http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg",
"https://upload.wikimedia.org/wikipedia/tr/9/98/Mu%C4%9Fla_S%C4%B1tk%C4%B1_Ko%C3%A7man_%C3%9Cniversitesi_logo.png",
"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024pxHawai%27i.jpg",
"http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg",
"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024pxHawai%27i.jpg"]

def download_file(url, file_name=None):
    r = requests.get(url, allow_redirects=True)
    file = file_name if file_name else str(uuid.uuid4())
    open(file, 'wb').write(r.content)

def hash_dict(dict):
    arr = os.listdir('.')
    arr.remove("ceng_2034_2020_final.py")
    print(arr)
    for i in range(len(arr)):
        hash = md5(arr[i])
        dict[arr[i]] = hash
    return dict

def check_hash(hashdict, hash):
    duplicate = []
    keys_list = list(hashdict)
    values = hashdict.values()
    values_list = list(values)
    for i in range(len(values_list)):
        if hash == values_list[i]:
            duplicate.append(keys_list[i])
    if len(duplicate) >1 :
        print(duplicate, "these files are same" )
    



def parent_child():    # for child proces
    n = os.fork() 
  
    # n greater than 0  means parent process 
    if n > 0: 
        print("Parent process and id is : ", os.getpid()) 
        os.waitpid(n,0)    # parent process waits for child process
    # n equals to 0 means child process 
    else: 
        print("Child process and id is : ", os.getpid())
        for i in range(len(url)):
            download_file(url[i])
            print("file dowlanded")
        hashdict = {}
        hash_dict(hashdict)
        print(hashdict)
        values = hashdict.values()
        values_list = list(values)
        print("all file is hashed")
        with Pool(cpu) as p:
            print(p.starmap(check_hash, [(hashdict,values_list[0]),(hashdict,values_list[1]),(hashdict,values_list[2]),(hashdict,values_list[3]),(hashdict,values_list[4])]))
        print("finished")



parent_child() 





