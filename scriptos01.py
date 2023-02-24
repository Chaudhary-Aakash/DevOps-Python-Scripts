from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys  
print("sample test case started")  
driver = webdriver.Chrome()  
#driver=webdriver.firefox()  
#driver=webdriver.ie()  
#maximize the window size  
driver.maximize_window()  
#navigate to the url  
driver.get("https://www.google.com/")  
#identify the Google search text box and enter the value  
#driver.find_element_by_name("q").send_keys("javatpoint") 
search_box = driver.find_element("name", "q")

search_box.send_keys('instagram')

search_box.submit() 
time.sleep(3)  
#click on the Google search button  
#driver.find_element_by_name("btnK").send_keys(Keys.ENTER)  
push_box = driver.find_element("name", "btnK")

push_box.send_keys(Keys.ENTER)

push_box.submit()
time.sleep(3)  
#close the browser  
driver.close()  
print("sample test case successfully completed")  
