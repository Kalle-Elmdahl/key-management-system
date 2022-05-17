# import all required frameworks
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# inherit TestCase Class and create a new test class

class KMS_test_class(unittest.TestCase):

    # initialization of webdriver
    def setUp(self):
        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome(ChromeDriverManager().install())


    # Test case method. It should always start with test_
    def tests(self):

        # call login function
        self.login_test()
        # call overview function
        self.overview_test()
        

    def login_test(self):
        # get driver
        driver = self.driver
        # get python.org using selenium
        driver.get("http://localhost:3000/")
        time.sleep(2)
        # locate element using name
        go_to_case = driver.find_element_by_xpath("//*[@id='root']/main/div/form/div[4]/button").click()
        time.sleep(2)
        fill_in_email = driver.find_element_by_xpath("//*[@id='email']").send_keys("mi.cho123@hotmail.com")
        fill_in_pass = driver.find_element_by_xpath("//*[@id='password']").send_keys("abc123")

        press_login = driver.find_element_by_xpath("//*[@id='root']/main/div/form/button").click()

        assert "SIGN UP" not in driver.page_source
        return


    def overview_test(self):
        # get driver
        driver = self.driver
        # get python.org using selenium
        #driver.get("http://localhost:3000/overview")

        time.sleep(2)
        # press_visit //*[@id="root"]/div/div[2]/div/div/div/div/div/div/button
        press_visit = driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div/div/div/div/div/button").click()
        time.sleep(2)
        # press //*[@id="root"]/div/div[2]/div/div[3]/div/div/div[6]/button
        press_add_case_2 = driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[3]/div/div/div[6]/button").click()
        time.sleep(2)

        #Clears text in element
        driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div/div[2]/div/input").send_keys(Keys.CONTROL + 'a' + Keys.BACK_SPACE)
        time.sleep(2)


        # change text in  /html/body/div[3]/div[3]/div/div/div/div[2]/div/input to "Worst view ever"
        driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div/div[2]/div/input").send_keys("Worst view in town")
        time.sleep(2)

        #change_checkin_time in /html/body/div[3]/div[3]/div/div/div/div[4]/div/input to 10:00
        driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div/div[4]/div/input").send_keys(Keys.CONTROL + 'a' + Keys.BACK_SPACE)
        change_checkin_time = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div/div[4]/div/input").send_keys("10:00")
        time.sleep(2)

        #change check out time to 14:00 in //*[@id=":r6l:"]
        driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div/div[5]/div/input").send_keys(Keys.CONTROL + 'a' + Keys.BACK_SPACE)
        change_time_out = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div/div[5]/div/input").send_keys("14:00")
        time.sleep(2)

        #click on /html/body/div[3]/div[3]/div/div/div/div[6] 
        driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div/div[6]").click()
        time.sleep(2)

        #click /html/body/div[3]/div[3]/div/div/div/div[7]/button
        driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div/div[7]/button").click()
        time.sleep(2)
        
        assert "Overview" in driver.page_source
        return

    # cleanup method called after every test performed
    def tearDown(self):
        self.driver.close()

# execute the script
if __name__ == "__main__":
    unittest.main()