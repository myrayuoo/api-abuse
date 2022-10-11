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
import json
import random
import time
import threading
import os

def run(front, message):
    def connect():
        print("Connecting")
        #r = requests.post(f"https://{front}.omegle.com/start?caps=recaptcha2,t&firstevents=1&spid=&randid=KGAAB3MW&lang=cs")
        for x in range(10):
            r = requests.post(f"https://{front}.omegle.com/start?caps=recaptcha2,t&firstevents=1&spid=&randid=KGAAB3MW22%5D&lang=en")
            if "waiting" not in str(r.content).lower():
                break
            time.sleep(1)
            r.status_code = 69

        if r.status_code == 200:
            print(f"Connected to {front}")
            event(json.loads(r.content)["clientID"])
        else:
            print("Failed to connect")

    def request_gif():
        r = requests.get("https://ssl.google-analytics.com/__utm.gif?utmwv=5.7.2&utms=16&utmn=801864847&utmhn=www.omegle.com&utmt=event&utme=5(Omegle%20chat%20started*Text)&utmcs=UTF-8&utmsr=1920x1080&utmvp=1365x979&utmsc=24-bit&utmul=cs-cz&utmje=0&utmfl=-&utmdt=Omegle&utmhid=1673003378&utmr=-&utmp=%2F&utmht=1661344243357&utmac=UA-1307731-4&utmcc=__utma%3D229593027.1020738013.1660766923.1660766923.1661343028.2%3B%2B__utmz%3D229593027.1660766923.1.1.utmcsr%3D(direct)%7Cutmccn%3D(direct)%7Cutmcmd%3D(none)%3B&aip=1&utmjid=&utmu=6BQAAAAAAAAAAAAAAAAAAAAE~")
        if r.status_code != 200:
            print("Failed to request the gif")

    def event(client_id):
        r = requests.post(f"https://{front}.omegle.com/events", data={"id": client_id}, headers={"accept": "application/json", "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"})
        if r.status_code == 200:
            print("Event successful")
            request_gif()
            send_msg(message, client_id)
        else:
            print("Event Failed")

    def send_msg(text, client_id):
        time.sleep(2)
        r  = requests.post(f"https://{front}.omegle.com/send", data={"msg": text, "id": client_id})
        if r.status_code == 200:
            print("Message sent")
        disconnect(client_id)

    def disconnect(client_id):
        r = requests.post(f"https://{front}.omegle.com/disconnect", data={"id": client_id})
        if r.status_code == 200:
            print("Disconnected")
    connect()

def random_front():
    return "front"+str(random.randint(1,40))

def main():
    print("""                            _       _     _   
  __ _ _   _  __ _ _   _  | | __ _| |__ | |_ 
 / _` | | | |/ _` | | | | | |/ _` | '_ \| __|
| (_| | |_| | (_| | |_| |_| | (_| | |_) | |_ 
 \__, |\__,_|\__, |\__,_(_)_|\__, |_.__/ \__|
 |___/       |___/           |___/           
> Omegle bot                                               
    """)

    message = input("Message> ")
    amount = int(input("Amount> "))

    for x in range(amount):
        threading.Thread(target=run, args=(random_front(),message)).start()
main()