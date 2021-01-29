import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import pandas

PATH = "chromedriver.exe"
options = selenium.webdriver.ChromeOptions()
options.add_argument('--headless')
driver = selenium.webdriver.Chrome(PATH, options=options)

excel_data = pandas.read_excel('Hesaplar.xlsx', sheet_name='PORTFÖY')
excel_data_category = excel_data['KATEGORİ'].tolist()
excel_data_code = excel_data['KOD'].tolist()
print(excel_data_category)
print(excel_data_code)

for index in range(len(excel_data_category)):
    if(excel_data_category[index] == "FON"):
        driver.get("https://www.tefas.gov.tr/FonAnaliz.aspx?FonKod=" + excel_data_code[index])
        value = driver.find_element_by_xpath("/html/body/form/div[3]/div[3]/div/div[2]/div[1]/ul[1]/li[1]/span").text
        print(excel_data_code[index] + "-" + value)
        time.sleep(3)

    elif(excel_data_category[index] == "HİSSE"):
        driver.get("https://tr.tradingview.com/symbols/BIST-" + excel_data_code[index] + "/")
        value = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div/header/div/div[3]/div[1]/div/div/div/div[1]/div[1]").text
        print(excel_data_code[index] + "-" + value)
        time.sleep(3)

    elif(excel_data_category[index] == "COIN"):
        driver.get("https://tr.tradingview.com/")
        search_bar = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[3]/form/label/tv-autocomplete/input")
        search_bar.click()
        search_bar.send_keys(excel_data_code[index] + "USD")
        search_button = driver.find_element_by_class_name("tv-header-search__icon").click()
        value = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div/header/div/div[3]/div[1]/div/div/div/div[1]/div[1]").text
        print(excel_data_code[index] + "-" + value)
        time.sleep(3)

driver.quit()
