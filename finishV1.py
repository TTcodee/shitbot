from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
options = Options()
options.page_load_strategy = 'eager'

driver = webdriver.Firefox(options=options)
driver.get("https://bookyourcourt.psm.tu.ac.th/app/main/bookings/home")

id = "6422771756"
passwd = "1830101157674"

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
                print("meow")
                None
time.sleep(3)               
username_ele.clear()
username_ele.send_keys(id)
passwd_ele.clear()
passwd_ele.send_keys(passwd)
button_ele = form.find_element(By.TAG_NAME, "button")
while True:
        try:
                button_ele.click()
                break
        except:
                None
                
while True:
        try:
                court = driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/default-layout/div/div/div[2]/div[2]/ng-component/div/div/div[3]/div/div/div/div[1]/div/div/div/div/span[1]")
                print("fdsafdasfsdafsdafsadfasd")
                break
        except:
                print("something wrong")
                

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
                print("5555555555555")
book_date_ele.clear()
book_date_ele.send_keys("15/01/2023")

while True:
        try:
                button = driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/default-layout/div/div/div[2]/div[2]/ng-component/div/div/div[3]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[2]/button[1]")
                
                print("Button Found")
                break
        except:
                print("something wrong")
                
search_button = driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/default-layout/div/div/div[2]/div[2]/ng-component/div/div/div[3]/div[1]/div/div/div[5]/button");
while not button.is_enabled():
        print(button.is_enabled())
        search_button.click()
        time.sleep(10)
        while True:
                try:
                   button = driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/default-layout/div/div/div[2]/div[2]/ng-component/div/div/div[3]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[2]/button[1]")
                   break
                except:
                   print("fail")

button.click()
time.sleep(0.2)
confirm = driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/default-layout/div/div/div[2]/div[2]/ng-component/div/confirmmodal/div/div/div/div/div/a[2]");
confirm.click()