import time
from datetime import datetime as dt

host_temp = r"Path to file goes here"
host_file_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]

user_time_start = 8
user_time_end = 23
user_reload_time = 5
minutes = user_reload_time #* 60

while True:
    if  dt(dt.now().year, dt.now().month, dt.now().day, user_time_start) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, user_time_end):
        print("Protocol : ACTIVE  -- Work Session is ACTIVE")

        with open(host_file_path, "r+") as file:
            content = file.read()
            for website in website_list:
                 if website in content:
                     pass
                 else:
                     file.write(redirect + " " + website + "\n")
    else:
        with open(host_file_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
        print("Protocol : NOT ACTIVE")
    
    time.sleep(minutes)



