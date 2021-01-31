import os
import fileinput
import time
import requests

localtime = time.asctime(time.localtime(time.time()))
status = 0
global x
tablica = ["Administrator", "All Users", "Default", "Default User", "Public"]



for x in os.listdir("C:\\Users"):
    if os.path.isdir("C:\\Users\\" + x) and not (x in tablica) and os.path.exists("C:\\Users\\" + x + "\\stopka\\"):
        for szukana in os.listdir("C:\\Users\\" + x + "\\stopka\\"):
            if szukana.endswith(".html") and szukana != "x.html":
                try:
                    os.path.join("C:\\Users\\" + x + "\\stopka\\", szukana)
                    
                    with fileinput.FileInput("C:\\Users\\" + x + "\\stopka\\" + szukana, inplace=True,
                                             backup='.bak') as file:
                        for line in file:
                            print(line.replace("53.200", "3 053 200,00"), end='')
                            
                    status = 1
                    if status == 1:
                        r = requests.post('http://192.168.1.1/api/log/stopka',
                                          json={"key": localtime + "   " + x})
                except Exception as e:
                    requests.post('http://192.168.1.1/api/log/stopka', json={"key": e})




