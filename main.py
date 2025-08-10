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

account_field.send_keys("CHANGE TO YOUR ACCOUNT")#key account
driver.find_element(By.XPATH, "//*[@id='user_password']").send_keys("CHANGE TO YOUR PASSWORD")#find password part and key password
driver.find_element(By.XPATH, "//*[@id='new_user']/input[3]").click()#click login button


# ---CAPTCHA part start(manually)

# ---CAPTCHA part end(manually)
