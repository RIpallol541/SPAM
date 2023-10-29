import random
from selenium import webdriver
import time
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from multiprocessing import Pool

from read_file_expression import read_expression as re
from read_file_log_pas import log_pas as lp
from read_file_time import read_time as rt

options = webdriver.ChromeOptions()
useragent = UserAgent()
options.add_argument(useragent.random)
options.add_argument("--start-maximized")
# options.add_argument("--headless")

link = "https://1whkgo.top/bets/home"


def get_data(user):
    count_ran = 0
    list_e = list(set(re(rt()[2])[0]))
    random.shuffle(list_e)
    driver = webdriver.Chrome(
        options=options
    )
    try:
        driver.get(link)
        time.sleep(random.randint(2, 6))

        corr_site = driver.find_element(By.CSS_SELECTOR,
                                        '.navigation-item-image[src=\'https://1win-cdn.com/img/lucky-jet.f927485da.svg\']')
        corr_site.click()
        time.sleep(random.randint(2, 6))

        come_input = driver.find_element(By.CSS_SELECTOR,
                                         'button[class=\'button df-aic-jcc secondary theme-default header-button login\']')
        come_input.click()
        time.sleep(random.randint(2, 6))

        email_input = driver.find_element(By.NAME, 'login')
        email_input.clear()
        email_input.send_keys(f"{user[0]}")
        time.sleep(random.randint(2, 6))

        password_input = driver.find_element(By.NAME, 'password')
        password_input.clear()
        password_input.send_keys(f"{user[1]}")
        time.sleep(random.randint(2, 6))
        password_input.send_keys(Keys.ENTER)
        time.sleep(random.randint(30, 50))

        text_input = driver.find_element(By.CSS_SELECTOR,
                                         'iframe[src=\'https://lucky-jet-ws.1play.one/?exitUrl=null&language=ru&b=demo\']')
        driver.switch_to.frame(text_input)
        while True:
            if count_ran != re(rt()[2])[1]:
                text_get = driver.find_element(By.CSS_SELECTOR, 'input[placeholder=\'Введите сообщение\']')
                text_get.click()
                text_get.clear()
                for item in list_e:
                    text_get.send_keys(item)
                    text_get.send_keys(Keys.ENTER)
                    time.sleep(random.randint(int(rt()[0]), int(rt()[1])))
                    count_ran += 1
            else:
                count_ran = 0
                list_e = list(set(re(rt()[2])[0]))
                random.shuffle(list_e)

    except Exception as ex:
        print(ex)
        time.sleep(300)
    finally:
        driver.close()
        driver.quit()


def main(response_time_left, response_time_right, mes, log, acc):
    print(response_time_left, response_time_right, mes, log, acc)
    ftime = open("time.txt", "w")
    ftime.seek(0)
    ftime.write(response_time_left + "\n")
    ftime.write(response_time_right + "\n")
    ftime.write(mes)
    ftime.close()
    n = int(acc)
    user = lp(log)
    p = Pool(processes=n)
    p.map(get_data, user)
