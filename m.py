from bs4 import BeautifulSoup
import requests
import json
import threading
import datetime
import time

lock = threading.Lock()
array = []


def check_url(url,string):
    global array
    r = requests.get(url)   

    date = str(datetime.datetime.now())
    if string in r.text:
        result = date + url +" - "+string+" - "+" bulundu"
    else:
        result = date + url +" - "+string+" - "+" bulunamadı"         
    lock.acquire()
    array.append(result)
    lock.release()   

def start_check():           
    with open('task.json') as json_file:  
        data = json.load(json_file)
    threads = []
    for row in data:
        t = threading.Thread(target=check_url, args=(row["url"], row["string"],))
        date = str(datetime.datetime.now())
        print(row['url'] + ' started at ' + date)
        t.start()

        threads.append(t)

    for t in threads:
        t.join()

    return array
            
        #check_url(row["url"], row["string"])


