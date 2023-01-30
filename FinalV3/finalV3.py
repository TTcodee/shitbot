from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
from selenium.webdriver.support.wait import WebDriverWait
import sys

#ID/PASS for website
id = sys.argv[1]
passwd = sys.argv[2]
# court number
court_number = "Badminton Court {x}".format(x = str(sys.argv[3]))
# time
t = sys.argv[4]
# date_format = "18/01/2023"
date_format = sys.argv[5]

options = Options()
options.page_load_strategy = 'eager'

driver = webdriver.Firefox(options=options)
driver.get("https://bookyourcourt.psm.tu.ac.th/app/main/bookings/home")



while True:
        try:
                form = driver.find_element(By.TAG_NAME, "form")
                break
        except:
                print('wait\n')
while True:
        try:
                username_ele = form.find_element(By.NAME, 'userNameOrEmailAddress')
                passwd_ele = form.find_element(By.NAME, "password")
                break
        except:
                None
time.sleep(1.5)
WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')).click()
# while True:
#         try:
#                 cookie_bt = driver.find_element(By.XPATH,'//*[@id="onetrust-accept-btn-handler"]')     
#                 break
#         except:
#                 None
# cookie_bt.click()  
username_ele.clear()
username_ele.send_keys(id)
passwd_ele.clear()
passwd_ele.send_keys(passwd)
button_ele = form.find_element(By.TAG_NAME, "button")
button_ele.click()
time.sleep(0.5)
while True:
        try:
                court = driver.find_element(By.XPATH, '//span[text() = " Badminton Court Gym 4"]')
                break
        except:
                print("Court Not Found")
                

while True:
        try:
                court.click()
                break
        except:
                print("click fail")



while True:
        try:
                book_date_ele = driver.find_element(By.ID, "Booking_BookingDate")
                break
        except:
                print("Date not found")
book_date_ele.clear()
book_date_ele.send_keys(date_format)
# find court option
court_option_eles = driver.find_elements(By.XPATH, '//option[contains(text(), "{x}")]'.format(x=court_number))
court_option_ele = court_option_eles[0]
for x in court_option_eles:
        print(x.text)
        if x.text == court_number:
                print("YESS")
                court_option_ele = x
        else:
                print("NOO")
court_option_ele.click()
search_button = driver.find_element(By.XPATH, '//button[contains(text(),"Search" )]');
search_button.click()
button = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.XPATH, '//button[contains(text(), "{x}")]'.format(x=t)))

while not button.is_enabled():
        print(button.is_enabled())
        search_button.click()
        # time.sleep(30)
        # button = driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/default-layout/div/div/div[2]/div[2]/ng-component/div/div/div[4]/div[2]/div/div[{x}]/div[1]/div[2]/div[2]/div[2]/button[{y}]".format(x=court_row,y=time_code))
        button = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.XPATH, '//button[contains(text(), "{x}")]'.format(x=t)))
button = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.XPATH, '//button[contains(text(), "{x}")]'.format(x=t)))
while not button.is_enabled():
        None
while True:
        try:
                button.click()
                break
        except:
                None
confirm = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.XPATH, "/html/body/app-root/ng-component/div/default-layout/div/div/div[2]/div[2]/ng-component/div/confirmmodal/div/div/div/div/div/a[2]"))
while True:
        try:
                confirm.click()
                break
        except:
                None