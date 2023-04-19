from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import common

FromSearch = common.FromProvince
FromCityString = "//span[contains(.,'" + \
    common.FromProvince+" - "+common.FromCounty+"')]"
FromDetails = common.FromDetails
ToSearch = common.ToProvince
ToCityString = "//span[contains(.,'" + \
    common.ToProvince+" - "+common.ToCounty+"')]"
ToDetails = common.ToDetails

PATH = "D:\App Folders\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.araskargo.com.tr/kargo-ucreti-hesaplama")
driver.implicitly_wait(2)

title = driver.title
print(title)

try:
    driver.execute_script("""
        var l = document.getElementsByClassName("efilli-layout-default")[0];
        l.parentNode.removeChild(l);
    """)
    print("cookie closer did it.")
except:
    print("cookie closer failed.")
    
driver.find_element(By.ID, "mat-input-1").click()
driver.find_element(By.ID, "mat-input-1").send_keys(FromSearch)
driver.find_element(By.XPATH, (FromCityString)).click()

driver.find_element(By.ID, "mat-input-3").send_keys(FromDetails)

driver.find_element(By.ID, "mat-input-2").click()
driver.find_element(By.ID, "mat-input-2").send_keys(ToSearch)
driver.find_element(By.XPATH, (ToCityString)).click()

driver.find_element(By.ID, "mat-input-4").send_keys(ToDetails)

driver.find_element(By.CSS_SELECTOR, ".desi-btn > .ng-star-inserted").click()
driver.find_element(By.CSS_SELECTOR, ".mat-select-placeholder").click()
driver.find_element(By.CSS_SELECTOR, ".mat-option-text").click()

driver.find_element(By.ID, "mat-input-5").click()
driver.find_element(By.ID, "mat-input-5").send_keys("1")
driver.find_element(By.ID, "mat-input-6").send_keys("2")
driver.find_element(By.ID, "mat-input-7").send_keys("5")
driver.find_element(By.ID, "mat-input-8").send_keys("10")

driver.find_element(
    By.CSS_SELECTOR, ".col-md-12:nth-child(5) > .desi-btn").click()


print(driver.find_element(By.CSS_SELECTOR, ".item-total-price").text)
