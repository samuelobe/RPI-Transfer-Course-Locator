from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import config

course_code = "CSCI 2350" # Enter the course code here in the following format: "CSCI 1200"

start = time.time() # Begin runtime calculation
SIS_link = 'https://sis.rpi.edu/rss/yhwwkwags.P_Web_Artic_Guide?'
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install(),options = options)
driver.get(SIS_link) 
driver.maximize_window()

time.sleep(2)
num_states = len(driver.find_elements_by_xpath('/html/body/div[3]/form/table[1]/tbody/tr[2]/td[1]/select/option'))

for i in range(1, num_states+1): # Loop through all states
    driver.find_element_by_xpath('/html/body/div[3]/form/table[1]/tbody/tr[2]/td[1]/select/option['+str(i)+']').click()
    get_instititions_btn = driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[1]/td/input')
    get_instititions_btn.click()

    num_institutions = len(driver.find_elements_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr/td[2]/select/option'))

    for j in range(1, num_institutions+1): # Loop through all institutions in a state
        uni_name = driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr/td[2]/select/option['+str(j)+']')
        uni_name.click()
        uni_name = uni_name.text
        get_courses_btn = driver.find_element_by_xpath('/html/body/div[3]/form/table[3]/tbody/tr[1]/td/input')
        get_courses_btn.click()

        num_courses = len(driver.find_elements_by_xpath('/html/body/div[3]/table[1]/tbody/tr'))
      
        for k in range(2, num_courses//2,2): # Loop through all courses in an institution
            try:
                ren_course = driver.find_element_by_xpath('/html/body/div[3]/table[1]/tbody/tr['+str(k)+']/td[4]').text
                if ren_course == course_code:
                    print(uni_name)
                    break
            except:
                print('Exception in', uni_name)
                break

        driver.execute_script("window.history.go(-1)")

    if i > 1:
        reset_btn = driver.find_element_by_xpath('/html/body/div[3]/form/table[3]/tbody/tr[2]/td/input')
        reset_btn.click()

driver.close()
end = time.time()
print("Runtime:", end-start, "seconds")
