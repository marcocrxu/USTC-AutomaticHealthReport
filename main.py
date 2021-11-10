from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from constant import LOGIN_PAGE, USERNAME, PASSWORD
from mail import send_mail
import requests
import time
from mail import send_mail


def click_login(driver, login):
    print('prepared to login')
    ActionChains(driver).click(login).perform()


def CNN(image_name):
    pass


def handle_validate(driver, validate):
    image = driver.find_element_by_xpath('//*[@id="valiCode"]/div[2]/div/img')
    location = image.location  # 获取验证码x,y轴坐标
    size = image.size  # 获取验证码的长宽
    r = requests.get(image.get_attribute('src'))

    with open('tmp/validate.png', 'wb') as f:
        # 对于图片类型的通过r.content方式访问响应内容，将响应内容写入baidu.png中
        f.write(r.content)

    # 调用model去解决
    s = CNN('tmp/validate.png')
    validate.send_keys(s)


def login_with_user(driver, username, password, validate, submit_login):
    print('login')
    username.send_keys(USERNAME)
    password.send_keys(PASSWORD)
    if validate is None:
        handle_validate(driver, validate)
    ActionChains(driver).click(submit_login).perform()


chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(LOGIN_PAGE)


try:
    login = driver.find_element_by_xpath('//*[@href="/2020/caslogin"]')
except Exception as e:
    login = None
    print(e)

if login!=None:
    click_login(driver, login)

try:
    username = driver.find_element_by_xpath('//*[@id="username"]')
    password = driver.find_element_by_xpath('//*[@id="password"]')
    submit_login = driver.find_element_by_xpath('//*[@id="login"]')
except Exception as e:
    username = None
    password = None
    submit_login = None

try:
    validate = driver.find_element_by_xpath('//*[@id="validate"]')
except Exception as e:
    validate = None

if username and password and submit_login:
    login_with_user(driver, username, password, validate, submit_login)

# print(driver.page_source)

try:
    submit_health_btn = driver.find_element_by_xpath('//*[@id="report-submit-btn-a24"]')
except Exception as e:
    submit_health_btn = None

time.sleep(2)

if submit_health_btn != None:
    print('click submit btn')
    ActionChains(driver).click(submit_health_btn).perform()

# print(driver.page_source)

try:
    is_success = driver.find_element_by_xpath('//*[@id="wrapper"]/div[2]/div[1]/p')
except Exception as e:
    is_success = None

if is_success != None:
    s = "上报成功"
    res = is_success.text
    if s in res:
        print('打卡成功')
        send_mail('log.txt', True)
    else:
        print('打卡失败')
        send_mail('log.txt', False)
else:
    print('click failed, check the source of the webpage!')
    send_mail('log.txt', False)

driver.quit()