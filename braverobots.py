#add selenium
from selenium import webdriver
import time

# add math
import math

#open browser
#link = "http://suninjuly.github.io/math.html"
link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

#formula
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#find x, add text from tag
#x_element = browser.find_element_by_id('input_value')
#x = x_element.text

#find x from img
x_fromimg = browser.find_element_by_id('treasure')
print("vot iks")
print(x_fromimg)
x_attr = x_fromimg.get_attribute('valuex')
print("vot igrek")
y = calc(x_attr)

print(y)

#search form. write y
input1 = browser.find_element_by_id('answer')
input1.send_keys(y)

#search checkbox
checkbox = browser.find_element_by_id('robotCheckbox')
checkbox.click()

#search radiobutton
radiobutton = browser.find_element_by_id('robotsRule')
radiobutton.click()

#search button          
button = browser.find_element_by_class_name('btn')
button.click()

time.sleep(10)
browser.quit()

#git!