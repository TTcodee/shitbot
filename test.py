from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

options = Options()
options.page_load_strategy = 'eager'

driver = webdriver.Firefox(options=options)
driver.get("https://bookyourcourt.psm.tu.ac.th/app/main/bookings/home")

# driver.maximize_window()

id = "6422782100"
passwd = "1102200185194"

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
                court = driver.find_element(By.XPATH, "//span[text()=' Badminton Court Gym 4']")
                print("fdsafdasfsdafsdafsadfasd")
                break
        except:
                print("something wrong")
court.click()
while True:
        try:
                book_date_ele = driver.find_element(By.ID, "Booking_BookingDate")
                break
        except:
                print("5555555555555")
book_date_ele.clear()
book_date_ele.send_keys("15/01/2023")

