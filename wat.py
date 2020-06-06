from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys
from keyboard import press
import time
driver = webdriver.Chrome(executable_path="C:\seleniumdrivers\chromedriver.exe")
driver.get("https://web.whatsapp.com/")
time.sleep(10)
msz = "Saurabh ka lund kala h "
msz2 = "kala hee rhega"

sr = driver.find_element_by_css_selector('span[title="saurabh"]')
sr.click()
i = 0
time.sleep(5)
ri = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]")
while True:
    ri.send_keys(msz)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]").click()
    ri.send_keys(msz2)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]").click()
    ri.send_keys("MA K LODE")
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]").click()
    ri.send_keys("count == " + str(i))
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]").click()
    i = i+1
# while i < 10000:
#     ri.send_keys(msz)
#     press('enter')
#     ri.send_keys(msz2)
#     press('enter')
#     ri.send_keys(msz3)
#     press('enter')
#     i = i+1
