from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.common.action_chains import ActionChains


# 디버깅 모드
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="~/ChromeProfile"'
driver = webdriver.Chrome(chrome_driver, options= chrome_options)


# 실행할 웹페이지 불러오기 (네이버 영화)
driver.get("https://movie.naver.com/")

#1-20위 개요, 감독, 평점
rankbtn1 = driver.find_element(By.XPATH, '//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
rankbtn1.click()
rankbtn11 = driver.find_element(By.XPATH, '/html/body/div/div[4]/div/div/div/div/div[1]/div[1]/ul/li[2]/a')
rankbtn11.click()

file = open('navermovie.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(['제목','개요','감독','평점'])

for i in range(2,12):
    rankbtn2 = driver.find_element(By.XPATH, f'/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i}]/td[2]/div/a')
    rankbtn2.click()
    title = driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[1]/h3/a[1]').text
    info = driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p').text
    PD = driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
    score = driver.find_element(By.XPATH, '//*[@id="actualPointPersentBasic"]/div/span/span').text
    print(title+info+PD+score)
    rankbtn3 = driver.find_element(By.XPATH, '//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
    rankbtn3.click()
    rankbtn11 = driver.find_element(By.XPATH, '/html/body/div/div[4]/div/div/div/div/div[1]/div[1]/ul/li[2]/a')
    rankbtn11.click()
    writer.writerow([title,info,PD,score])


for e in range(13,23):
    rankbtn2 = driver.find_element(By.XPATH, f'/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{e}]/td[2]/div/a')
    rankbtn2.click()
    title = driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[1]/h3/a[1]').text
    info = driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p').text
    PD = driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
    score = driver.find_element(By.XPATH, '//*[@id="actualPointPersentBasic"]/div/span/span').text
    print(title+info+PD+score)
    rankbtn3 = driver.find_element(By.XPATH, '//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
    rankbtn3.click()
    rankbtn11 = driver.find_element(By.XPATH, '/html/body/div/div[4]/div/div/div/div/div[1]/div[1]/ul/li[2]/a')
    rankbtn11.click()
    writer.writerow([title,info,PD,score])
file.close()



#좋아하는 영화 제목, 감독, 평점, 리뷰 개수
search = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/fieldset/div/span/input')
search.click()
kw = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/fieldset/div/span/input')
ActionChains(driver).send_keys('슬램덩크').perform()
search2 = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/fieldset/div/button')
search2.click()
sd = driver.find_element(By.XPATH, '//*[@id="old_content"]/ul[2]/li[1]/dl/dt/a')
sd.click()
sdtitle = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/h3/a[1]').text
sdPD = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
sdscore = driver.find_element(By.XPATH, '//*[@id="actualPointPersentBasic"]/div/span/span').text
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
sd_rv = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[2]/div[1]/div[4]/div[5]/div[2]/div[3]/strong/em').text
print(sdtitle+sdPD+sdscore+sd_rv)
file = open('navermovie.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow([sdtitle,sdPD,sdscore,sd_rv])




