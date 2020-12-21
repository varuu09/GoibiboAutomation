from selenium import webdriver as wb
from selenium.webdriver.support.ui import Select
import time


# intialising driver
driver= wb.Chrome()

driver.get('https://www.goibibo.com/')
driver.maximize_window()
driver.implicitly_wait(6)

#----------------Selecting Locations and date
driver.find_element_by_id('roundTrip').click()

#-----------------Selecting Delhi as Source Location
driver.find_element_by_id('gosuggest_inputSrc').send_keys("Delhi (DEL)")
result_src= driver.find_element_by_id("react-autosuggest-1" )
print(result_src.get_attribute('innerHTML'))
result_src.find_element_by_xpath("//li[contains(@class,'autosuggest__suggestion')]//span[contains(text(),'Delhi, India')]").click()

#Selecting Mumbai as Destination Location
driver.find_element_by_id('gosuggest_inputDest').send_keys("Mumbai (BOM)")
result_dest= driver.find_element_by_id("react-autosuggest-1")
print(result_dest.get_attribute('innerHTML'))
result_dest.find_element_by_xpath("//li[contains(@class,'autosuggest__suggestion')]//span[contains(text(),'Mumbai, India')]").click()

#Selecting Date
date_src=driver.find_elements_by_class_name('DayPicker-Day')
for i in range(len(date_src)):
    dateSelectorArr = date_src[i].find_elements_by_xpath('//div[@aria-disabled="false"]')

dateSelectorArr[1].click()

#------------click search button
time.sleep(4)
driver.find_element_by_id('gi_search_btn').click()

#------------------------------------------------------------------------
#Sorting Price Low to High
price_sort= driver.find_elements_by_id('PRICE')

price_sort[0].click()
price_sort[1].click()
time.sleep(2)
#Selecting flights of highest rate
max_price_container1 = driver.find_element_by_xpath("//*[@id='content']/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[5]/div[1]")
max_price_container2 = driver.find_element_by_xpath("//*[@id='content']/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[5]/div[2]")

max_price_container1.find_element_by_class_name('custRad').click() # onwards trip price

max_price_container2.find_element_by_class_name('custRad').click() # return trip price

#--------------clicking on book button
time.sleep(4)
driver.find_element_by_class_name('button.fr.fltbook.fb.widthF105.quicks.fb').click()

#-----------------------------------------------------------
#---------selecting gender title
title = Select(driver.find_element_by_id("Adulttitle1"))
gender = input("Select Gender\n 1. Mr \n 2. Mrs \n 3. Ms \n")
if gender == "1":
    title.select_by_index(1)
elif gender == "2":
    title.select_by_index(2)
elif gender == "3":
    title.select_by_index(3)
else:
    pass

#----------------- Entering user details from command line
firstname = input("Please Enter First Name: ")
middlename = input("Please Enter Middle Name: \n Just press Enter if you don't have Middle name: ")
lastname = input("Please Enter Last Name: ")
email = input("Please Enter Email Address: ")
mobile = input("Please Enter your Mobile Number: ")
driver.find_element_by_id("AdultfirstName1").send_keys(firstname)
driver.find_element_by_id("AdultmiddleName1").send_keys(middlename)
driver.find_element_by_id("AdultlastName1").send_keys(lastname)
driver.find_element_by_id("email").send_keys(email)
driver.find_element_by_id("mobile").send_keys(mobile)

# ------- selecting option to secure flight or not
secure = input("Do you want to Secure your trip?\n Enter 1 for Secure your trip \n Enter 2 for not securing your trip:")
if secure == "1":
    driver.find_element_by_xpath("//*[contains(text(),'Yes, secure my trip')]").click()
elif secure == "2":
    driver.find_element_by_xpath("//*[contains(text(),'I am willing to risk my trip')]").click()
else:
    pass

time.sleep(4)
driver.find_element_by_class_name("button.orange.col-md-3.fr.large.dF.justifyCenter.min37").click()
#-----------------------------------------------------------------------------------

#----------- Accepting covid pop up overlay by clicking ok
body = driver.find_element_by_xpath("//div[@class='popOverlay popShow']")

body.find_element_by_xpath("//div[@class='popModal zoom large popShow']//button").click()

driver.find_element_by_xpath('//*[@id="addonCard"]/button').click()
time.sleep(10)

# --------------Selecting wallet for payment by amazon pay
driver.find_element_by_id("tab_wallet").click()

amazonPay = driver.find_element_by_name('walletRadio').is_enabled()

if amazonPay:
    print("Payment method amazon poy is selected")
else:
    amazonPay.click()

driver.find_element_by_class_name("button.green.large.citipatBtn.btn.payNowBtn")
#driver.quit()