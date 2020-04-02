import time
from datetime import datetime as dt

host_temp = r"G:\Projekty Python\WebBlcoker\hosts"
host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com", "www.youtube.com", "youtube.com", "www.tvn24.pl", "tvn24.pl"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,23) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,12):
        print("Work")
        with open(host_temp, "r+") as file:
            content= file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect +" "+ website + "\n")

    else: 
        print("No Work")
        with open(host_temp, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)
    

