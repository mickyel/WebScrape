from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
def get_driver():
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("https://titan22.com/account/login?return_url=%2Faccount")
  return driver
def get_value(text):
  output = float(text.split(": ")[1])
  return output
def main():
  driver = get_driver()
  driver.find_element(by="id", value="CustomerEmail").send_keys("mickyelmb@yahoo.com")
  time.sleep(2)
  driver.find_element(by="id", value="CustomerPassword").send_keys("Shop4shoes" + Keys.RETURN)
  time.sleep(2)
  driver.find_element(by="xpath", value="/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a").click()
  time.sleep(4)
  #text =  driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]").text
 
  ##print(text)

print(main())