"""
點擊滑鼠右鍵: context_click()
雙擊滑鼠左鍵: double_click()
按著滑鼠左鍵不放: click_and_hold()
放開滑鼠左鍵: release()
拖曳到某個元素後放開: drag_and_drop(source, target)
拖曳到某個座標後放開: drag_and_drop_by_offset(source, xoffset, yoffset)
按下鍵盤上某個按鍵: key_down(value)
放開鍵盤上某個按鍵: key_up(value)
滑鼠指標從當前位置移動到某個座標: move_by_offset(xoffset, yoffset)
滑鼠指標移動到某個元素: move_to_element(to_element)
移動到某元素附近座標位置: move_to_element_with_offset(to_element, xoffset, yoffset)
執行當前這個ActionChain的動作: perform()
在元素上輸入值(ex:input): send_keys(value)
在指定的元素上輸入值: send_keys_to_element(element, value)
"""
from selenium import webdriver#control website
from selenium.webdriver.chrome.options import Options#how website do
from selenium.webdriver.common.by import By#how to find element
from selenium.webdriver.support.ui import WebDriverWait#wait when open website
from selenium.webdriver.support import expected_conditions as EC#certain condition

# --- Keep Chrome open after script ends ---
options = Options()#create a object
options.add_experimental_option("detach", True)#A startup setting
#detach:not detach(kill) the process automaticallly when session end
#Ture:enable the action(detach)

# --- website open after the line ---
driver = webdriver.Chrome(options=options)#Create a chrome and set options variable as my own options(setting)
#webdriver:make you control the website
driver.get('https://kktix.com/')  # direct chrome to this URL

driver.find_element(By.XPATH, "//*[@id='navbar']/ul[2]/li[2]/a").click()#by the XPATH to find button and click it.
#By.XPATH:by its XPATH to......
account_field = WebDriverWait(driver, 5).until(#wait maximum 5 sec and find account input part
    EC.visibility_of_element_located((By.XPATH, "//*[@id='user_login']"))
)

account_field.send_keys("006481")#key account
driver.find_element(By.XPATH, "//*[@id='user_password']").send_keys("Aa006481")#find password part and key password
driver.find_element(By.XPATH, "//*[@id='new_user']/input[3]").click()#click login button

iframe = driver.find_element(By.CSS_SELECTOR, "iframe selector here")
driver.switch_to.frame(iframe)

check_box = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='RInW4']/div/label/input"))
)
check_box.click()

driver.switch_to.default_content()  # go back to main page