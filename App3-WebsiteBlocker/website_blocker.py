import time
from datetime import datetime as dt
# r is used to take the string within "" as a complete unit and not consider any sequence as a special character
# hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
host_path_temp = "hosts"
redirect="127.0.01"
websites_to_be_blocked = ["http://art.yale.edu/","art.yale.edu/","mssplus.mcafee.com"]
# ["youtube.com","www.youtube.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,2) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,3):
        print("Working hours")
        with open("hosts",'r+') as file:
            content = file.read()
            print(content)
            for website in websites_to_be_blocked:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+'\n')
    else:
        with open("hosts","r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_to_be_blocked):
                    file.write(line)
            file.truncate()
        print("Fun time!!")
    # print(1)
    time.sleep(5)
    # will print 1 every 5 sec
