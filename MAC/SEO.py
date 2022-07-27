
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

print("\nAuthor: FunkMan","\n")
sendkeys_list=[]

while True :
    count = 0
    keys = input("輸入搜尋關鍵字? Enter(確定/開始執行): ")
    if keys == "" :
        break

    else :
        sendkeys_list.append(keys)
        for k in sendkeys_list :
            count += 1
            print("關鍵字{}: {}".format(count,k))
    print(" ")

number_of_times = int(input("執行次數: "))

Opts = Options()
Opts.add_argument("--incognito")

driver = webdriver.Chrome("/usr/local/bin/chromedriver",options=Opts) 
driver.get("https://www.google.com/")

for number in range(1,number_of_times+1) :

    if number <= number_of_times :
        for sk in sendkeys_list:
            try:
                driver.find_element(By.NAME, "q").send_keys("{}".format(sk))
                # sleep(1)
                driver.find_element(By.CLASS_NAME, "gNO89b").click()
                driver.back()
                sleep(1)

            except:

                webElement = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]")

                JavaScript = "arguments[0].click()"
                driver.execute_script(JavaScript, webElement)
                sleep(1)
                driver.back()
                sleep(1)

    else :
        pass

print("\n程式執行完畢","\n")
driver.close()
























