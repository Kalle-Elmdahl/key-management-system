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
from selenium.webdriver.support.ui import Select
# inherit TestCase Class and create a new test class


#  ! ! ! HOW TO TEST! ! !
# Vid testning, installera Google Chrome driver
# https://chromedriver.chromium.org/downloads
# Checka om ni har python genom att skriva py i CMD, 
# installera om needed.
# pip install selenium (i terminalen)
# pip install webdriver-manager 
# Skapa tester som egna funktioner i denna tests.py fil.
# Vid testning behövs att npm start är running i en annan
# terminal. När det är gjort så kan ni köra testen. 
# (I.E. PATH/admin-panel/tests py tests.py)


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
        # call new booking test function
        #self.new_booking_test()
        self.editbox_test()


    def login_test(self):
        # get driver
        driver = self.driver
        # get python.org using selenium
        driver.get("http://localhost:3000/")
        time.sleep(2)
        # locate element using name
        go_to_case = driver.find_element(by=By.XPATH, value="//*[@id='root']/main/div/form/div[4]/button").click()
        time.sleep(2)
        fill_in_email = driver.find_element(by=By.XPATH, value="//*[@id='email']").send_keys("mi.cho123@hotmail.com")
        fill_in_pass = driver.find_element(by=By.XPATH, value="//*[@id='password']").send_keys("abc123")

        press_login = driver.find_element(by=By.XPATH, value="//*[@id='root']/main/div/form/button").click()
        time.sleep(2)
        # press_visit //*[@id="root"]/div/div[2]/div/div/div/div/div/div/button
        press_visit = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div[1]/div/div/button/div[2]/button").click()
        assert "SIGN UP" not in driver.page_source

    def editbox_test(self):
        # get driver
        driver = self.driver
        time.sleep(2)
        edit_box = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/button[2]").click()
        time.sleep(2)
        name_field = driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[3]/div/div[1]/div[1]/div/input")
        time.sleep(2)
        name_field.send_keys(Keys.COMMAND + 'a' + Keys.BACK_SPACE)
        time.sleep(2)
        name_field.send_keys("Apartment Uno")
        time.sleep(5)
        driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[3]/div/div[2]/button").click()
        time.sleep(2)
        driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[3]/div/div[2]/button[2]").click()
        time.sleep(2)
        assert "Apartment Uno" in driver.page_source
        return

    def overview_test(self):
        # get driver
        driver = self.driver
        # get python.org using selenium
        #driver.get("http://localhost:3000/overview")
        time.sleep(2)
        # press //*[@id="root"]/div/div[2]/div/div[3]/div/div/div[6]/button
        press_add_case_2 = driver.find_element(by=By.XPATH, value="//*[@id='root']/div/div[2]/div/div[3]/div/div/div[6]/button").click()
        time.sleep(2)

        # press /html/body/div[3]/div[3]/div/div[2]/button[2]
        press_add_case_3 = driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[3]/div/div[2]/button[2]").click()
        time.sleep(2)

        #Clears text in element
        driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[3]/div/div[1]/div[2]/div/textarea[1]").send_keys(Keys.COMMAND + 'a' + Keys.BACK_SPACE)
        time.sleep(2)

        # change text in  /html/body/div[3]/div[3]/div/div/div/div[2]/div/input to "Worst view ever"
        driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[3]/div/div[1]/div[2]/div/textarea[1]").send_keys("Worst view in town")
        time.sleep(2)

        #change_checkin_time in /html/body/div[3]/div[3]/div/div/div/div[4]/div/input to 10:00
        driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[3]/div/div[1]/div[4]/div[1]/div/input").send_keys(Keys.COMMAND + 'a' + Keys.BACK_SPACE)
        time.sleep(2)

        change_checkin_time = driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[3]/div/div[1]/div[4]/div[1]/div/input").send_keys("10:00")
        time.sleep(2)

        #change check out time to 14:00 in //*[@id=":r6l:"]
        driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[3]/div/div[1]/div[4]/div[2]/div/input").send_keys(Keys.COMMAND + 'a' + Keys.BACK_SPACE)
        time.sleep(2)

        change_time_out = driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[3]/div/div[1]/div[4]/div[2]/div/input").send_keys("14:00")
        time.sleep(2)

        #click on /html/body/div[3]/div[3]/div/div/div/div[6] 
        driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[3]/div/div[1]/div[5]/div[2]/canvas").click()
        time.sleep(2)

        #click /html/body/div[3]/div[3]/div/div/div/div[7]/button
        driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[3]/div/div[2]/button").click()
        time.sleep(2)

        assert "Overview" in driver.page_source
        return

    def new_booking_test(self):
        #get driver
        driver = self.driver

        # Press new_booking //*[@id="root"]/div/div[2]/div/div[1]/div[2]/div/button[1]
        press_new_booking = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/button[1]").click()
        time.sleep(2)

        # enter "MichellTest" in /html/body/div[3]/div[3]/div/div[1]/div[1]/div[1]/div/input
        driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[3]/div/div[1]/form/div[1]/div/input").send_keys("Michell Test")
        time.sleep(2)

        # enter_email in /html/body/div[3]/div[3]/div/div[1]/div[1]/div[2]/div/input to "mi.cho123@hotmail.com"
        driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[3]/div/div[1]/form/div[2]/div/input").send_keys("mi.cho123@hotmail.com")
        time.sleep(1)

        # enter_guest_message /html/body/div[3]/div[3]/div/div[1]/div[1]/div[3]/div "Welcome to KMS"
        driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[3]/div/div[1]/form/div[3]/div/textarea[1]").send_keys("Welcome to KMS")
        time.sleep(1)

        # press /html/body/div[3]/div[3]/div/div[1]/div[1]/div[4]/div/div
        driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[3]/div/div[1]/form/div[4]/div/div").click()
        time.sleep(1)

        #press /html/body/div[4]/div[3]/ul/li[2]
        driver.find_element(by=By.XPATH, value="/html/body/div[4]/div[3]/ul/li[2]").click()
        time.sleep(1)
        
        # Clear checkin-time space
        driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[3]/div/div[1]/form/div[5]/div[1]/div/input").send_keys(Keys.COMMAND + 'a' + Keys.BACK_SPACE)
        time.sleep(2)

        #enter checkin time in /html/body/div[3]/div[3]/div/div[1]/div[1]/div[5]/div[1]/div/input to 1100
        driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[3]/div/div[1]/form/div[5]/div[1]/div/input").send_keys("1100")
        time.sleep(2)

        #Clear checkout time in /html/body/div[3]/div[3]/div/div[1]/div[1]/div[5]/div[2]/div/input
        driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[3]/div/div[1]/form/div[5]/div[2]/div/input").send_keys(Keys.COMMAND + 'a' + Keys.BACK_SPACE)
        time.sleep(2)

        #enter checkout time in /html/body/div[3]/div[3]/div/div[1]/div[1]/div[5]/div[2]/div/input to 1400
        driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[3]/div/div[1]/form/div[5]/div[2]/div/input").send_keys("1400")
        time.sleep(2)
        # press select = /html/body/div[3]/div[3]/div/div[1]/div[2]/div/div[2]/div[2]/div[2]/span/span[1]/select
        select = Select(driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[1]/form/div[6]/div[2]/div[2]/div[2]/span/span[1]/select"))

        #click /html/body/div[3]/div[3]/div/div[1]/div[2]/div/div[2]/div[2]/div[2]/span/span[1]/select
        driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[1]/form/div[6]/div[2]/div[2]/div[2]/span/span[1]/select").click()
        time.sleep(2)

        #Select by text "May"
        select.select_by_visible_text("June")
        time.sleep(2)

        #press day /html/body/div[3]/div[3]/div/div[1]/div[2]/div/div[2]/div[2]/div[3]/div[1]/div[3]/button[18]/span[2]
        driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[3]/div/div[1]/form/div[6]/div[2]/div[2]/div[3]/div[1]/div[3]/button[20]").click()
        time.sleep(5)

        #press confirm_booking /html/body/div[3]/div[3]/div/div[2]/button
        driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[3]/div/div[2]/button").click()
        
        time.sleep(2)
        #Assert NEW BOOKING
        return
        assert "CONFIRM BOOKING" in driver.page_source

    # cleanup method called after every test performed
    def tearDown(self):
        self.driver.close()

# execute the script
if __name__ == "__main__":
    unittest.main()