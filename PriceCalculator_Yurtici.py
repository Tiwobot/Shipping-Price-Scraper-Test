from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import common
from dependencies import ChromeDriverLocation

SearchSourceCityandCountry = common.FromProvince + \
    " "+common.FromCounty+" "+common.FromDetails
SearchDestinationCityandCountry = common.ToProvince + \
    " "+common.ToCounty+" "+common.ToDetails
desiWeight = common.desiKG
desiWidth = common.desiWidth
desiLength = common.desiLength
desiHeight = common.desiHeight
isSMSwanted = common.isSMSwanted

PATH = ChromeDriverLocation
driver = webdriver.Chrome(PATH)
driver.get("https://www.yurticikargo.com/tr/online-servisler/fiyat-hesapla")
driver.implicitly_wait(2)

title = driver.title
print(title)

driver.find_element(By.ID, "SourceCityAndCounty").send_keys(
    SearchSourceCityandCountry)
driver.find_element(By.CSS_SELECTOR, "em:nth-child(3)").click()
driver.find_element(By.ID, "DestinationCityAndCounty").send_keys(
    SearchDestinationCityandCountry)
driver.find_element(By.CSS_SELECTOR, "em:nth-child(2)").click()
driver.find_element(By.ID, "button-select-address").click()
driver.find_element(By.CSS_SELECTOR, ".package > svg").click()
driver.find_element(
    By.XPATH, "(//input[@type=\'number\'])[5]").send_keys(desiWidth)
driver.find_element(
    By.XPATH, "(//input[@type=\'number\'])[6]").send_keys(desiLength)
driver.find_element(
    By.XPATH, "(//input[@type=\'number\'])[7]").send_keys(desiHeight)
driver.find_element(
    By.XPATH, "(//input[@type=\'number\'])[8]").send_keys(desiWeight)
driver.find_element(By.ID, "btn-price-calculation").click()
print(driver.find_element(By.CSS_SELECTOR,
      "#product-genaral-total > b:nth-child(1)").text)
print(driver.find_element(By.CSS_SELECTOR,
      "#product-genaral-total > b:nth-child(3)").text)
