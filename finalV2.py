from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
from selenium.webdriver.support.wait import WebDriverWait

#17:00 = 1, 18:00 = 2, 19:00 = 3, 20:00 = 4
time_code = 1

#Row of court in website. Ex. Court 3 is row 2, Court 6 is row 4
court_row = 8

#DD/M/YYYY
date_format = "14/1/2023"

#ID/PASS for website
id = "#############################"
passwd = "############################"


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
                court = driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/default-layout/div/div/div[2]/div[2]/ng-component/div/div/div[3]/div/div/div/div[1]/div/div/div/div/span[1]")
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

while True:
        try:
                button = driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/default-layout/div/div/div[2]/div[2]/ng-component/div/div/div[3]/div[2]/div/div[{x}]/div[1]/div[2]/div[2]/div[2]/button[{y}]".format(x=court_row,y=time_code))
                
                print("Button Found")
                break
        except:
                print("something wrong")
                
search_button = driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/default-layout/div/div/div[2]/div[2]/ng-component/div/div/div[3]/div[1]/div/div/div[5]/button");
while not button.is_enabled():
        print(button.is_enabled())
        search_button.click()
        # time.sleep(0.5)
        # button = driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/default-layout/div/div/div[2]/div[2]/ng-component/div/div/div[3]/div[2]/div/div[{x}]/div[1]/div[2]/div[2]/div[2]/button[{y}]".format(x=court_row,y=time_code))
        button = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.XPATH, "/html/body/app-root/ng-component/div/default-layout/div/div/div[2]/div[2]/ng-component/div/div/div[3]/div[2]/div/div[{x}]/div[1]/div[2]/div[2]/div[2]/button[{y}]".format(x=court_row,y=time_code)))
button = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.XPATH, "/html/body/app-root/ng-component/div/default-layout/div/div/div[2]/div[2]/ng-component/div/div/div[3]/div[2]/div/div[{x}]/div[1]/div[2]/div[2]/div[2]/button[{y}]".format(x=court_row,y=time_code)))
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