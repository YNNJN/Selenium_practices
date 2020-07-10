'''
웹사이트 매크로 제작

1. 로그인
2. 편지쓰기
3. 보내기

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome() # 크롬을 사용
url = 'https://google.com'
driver.get(url)
driver.maximize_window() # 창을 제일 크게 엶
action = ActionChains(driver) # 액션 변수를 이용해서 driver를 사용할 수 있도록 지정

driver.find_element_by_css_selector('#gb_70').click()

action.send_keys('myung2ing@gmail.com').perform()
action.reset_actions()
driver.find_element_by_css_selector('.CwaK9').click() # 로그인 시 이메일 다음 클릭

time.sleep(2)
driver.find_element_by_css_selector('whsOnd.zHQkBf').send_keys('password')
driver.find_element_by_css_selector('.CwaK9').click() # 로그인 시 비밀번호 다음 클릭
time.sleep(2)

driver.get('https://mail.google.com/mail/u/0/?tab=wm&ogbl#inbox') # 메일박스로 이동
time.sleep(2)

driver.find_element_by_css_selector('.T-I.J-J5-Ji.T-I-KE.L3').click() # 편지쓰기 버튼 클릭
time.sleep(1)

send_button = driver.find_element_by_css_selector('.gU.Up') # 보내기 버튼 클릭

(
action.send_keys('myung2ing@gmail.com').pause(2).key_down(Keys.TAB).key_down(Keys.TAB)
.send_keys('제목입니다').pause(2).key_down(Keys.TAB)
.send_keys('abcde').pause(2).key_down(Keys.ENTER)
.key_down(Keys.SHIFT).send_keys('abcde').key_up(Keys.SHIFT).pause(2)
.move_to_element(send_button).click() # 클릭되지 않는 요소도 클릭 가능
.perform()
)