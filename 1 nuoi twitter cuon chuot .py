###IMPORT VÍ VÀO METAMASK
import threading
from getpass import getpass
import time
import sys
sys.path.append("..")
from GPMLoginAPI import GPMLoginAPI
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import random
########################
def read_file(a):
    try:
        file = open(a, encoding="utf-8")
    except FileNotFoundError:
        file = open(a, "a+", encoding="utf-8")
    sst = file.read()
    file.close()
    return sst

def run(x):
    
    api = GPMLoginAPI('http://127.0.0.1:19995')  
    file=read_file(r'C:\Users\ADMIN\OneDrive\Desktop\code\ID\ID52.txt')    
    ID=file.split('\n')[x] 
    print(ID) 
    profileId = ID
    startedResult = api.Start(profileId)
    time.sleep(1)
    chrome_options = Options()
    chrome_options.add_argument("--lang=en-US")
    chrome_options.add_experimental_option("debuggerAddress", startedResult["selenium_remote_debug_address"])
    chrome_options.arguments.extend(["--no-default-browser-check", "--no-first-run"])
    driver_path = startedResult["selenium_driver_location"]
    print('driver_path: ', driver_path)
    ser = Service(driver_path)
    driver = webdriver.Chrome(service=ser, options=chrome_options)
    time.sleep(1)
# set kich thuoc
    driver.set_window_size(300, 1000)
#Random time
    random_time=[3,5,7,6,1,2,4]
    nn_time=random.choice(random_time)
    time.sleep(nn_time)
#tạo metamask
    print("Dang tao vi cua so:",x)
    driver.get("https://twitter.com/home")
    time.sleep(nn_time)

    ######################Xong Trạng thái###################
    for t in range(3):
        driver.execute_script("window.scrollBy(0,1000)","")
        value=driver.execute_script("return window.pageYOffset;")
        time.sleep(nn_time)

        driver.execute_script("window.scrollBy(0,1700)","")
        driver.execute_script("return window.pageYOffset;")
        time.sleep(nn_time)

        driver.execute_script("window.scrollBy(0,3000)","")
        driver.execute_script("return window.pageYOffset;")
        time.sleep(nn_time)

        driver.execute_script("window.scrollBy(0,2500)","")
        driver.execute_script("return window.pageYOffset;")
        time.sleep(nn_time)

    driver.close()
    driver.quit()
# ĐẶT SỐ ACC (CỬA SỔ) CẦN CHẠY
luong = 1
threads = []
for x in range(luong):
    t = threading.Thread(target=run, args=(x,))
    threads.append(t)
    t.start()

# Chờ cho tất cả các luồng hoàn thành
for t in threads:
    t.join()
print("Kết thúc số luồng")