from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import common
from dependencies import ChromeDriverLocation

FromSearch = common.FromProvince
ToSearch= common.ToProvince
FromCityString = (common.FromProvince+" - "+common.FromCounty).upper().replace("I", "İ")
ToCityString = (common.ToProvince+" - "+common.ToCounty).upper().replace("I", "İ")
desiWeight = common.desiKG
desiWidth = common.desiWidth
desiLength = common.desiLength
desiHeight = common.desiHeight
isSMSwanted = common.isSMSwanted

PATH = ChromeDriverLocation
driver = webdriver.Chrome(PATH)
driver.get("https://www.mngkargo.com.tr/ucret-hesapla")
driver.implicitly_wait(2)

title = driver.title
print(title)
print(FromCityString)

driver.find_element(By.CSS_SELECTOR, ".closed").click()

driver.find_element(By.ID, "form_locationFirst").send_keys(FromSearch)
driver.find_element(By.LINK_TEXT, FromCityString).click()
driver.find_element(By.ID, "form_locationLast").send_keys(ToSearch)
driver.find_element(By.LINK_TEXT, ToCityString).click()
driver.find_element(By.CSS_SELECTOR, ".linkBox:nth-child(3) span:nth-child(1)").click()
driver.find_element(By.CSS_SELECTOR, ".packageParcel a").click()

