from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import common
from dependencies import ChromeDriverLocation


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