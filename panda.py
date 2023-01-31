from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select

opt = Options()
opt.add_argument(r"--silent")
opt.add_argument(r"--no-sandbox")
opt.add_argument(r"--disable-dev-shm-usage")
opt.add_argument(r'--ignore-certificate-errors')
opt.add_experimental_option("detach", True)
#opt.add_argument('headless')
#opt.add_argument(f'user-agent={user_agent}')
opt.add_experimental_option('excludeSwitches', ['enable-logging'])

access_code = input("Enter Code No Spaces: ")
email = input('Enter Your Email: ')

driver = webdriver.Chrome(options=opt)
driver.get('https://www.pandaexpress.com/feedback')

def next_button():
    nxtbtn = (By.ID, 'NextButton')
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(nxtbtn)).click()

def fill_code(a_code):
    code_list = []
    code_list.append(a_code[:4])
    code_list.append(a_code[4:8])
    code_list.append(a_code[8:12])
    code_list.append(a_code[12:16])
    code_list.append(a_code[16:20])
    code_list.append(a_code[20:])
    
    for i in range(1,7):
        element = 'CN' + str(i)
        snippet = (By.ID, element)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(snippet)).send_keys(code_list[i-1])
    
    next_button()
    

def fill_survey(eml):

    #page 1
    fill_circle = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[3]/span')
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(fill_circle)).click()
    next_button()



    #page 2
    for i in range(2,8):
        fill = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[' + str(i) + ']/td[3]/span')
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(fill)).click()
    next_button()

    #page 3
    for i in range(2,8):
        fill = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[' + str(i) + ']/td[3]/span')
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(fill)).click()
    next_button()

    #page 4
    fill = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[4]')
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(fill)).click()
    next_button()

    #page 5
    fill = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/div/fieldset/div/div/div[4]/span/span')
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(fill)).click()
    next_button()

    #page 6
    next_button()

    #page 7
    next_button()

    #page 8
    next_button()

    #page 9
    next_button()

    #page 10
    next_button()

    #page 11
    fill = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[2]/span')
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(fill)).click()
    next_button()

    #page 12
    for i in range(2,4):
        fill = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[' + str(i) + ']/td[3]/span')
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(fill)).click()
    next_button()

    #page 13
    paragraph = 'Panda Express is a great fast food restaurant that offers a wide variety of delicious Chinese-inspired dishes. The restaurant has been around since 1983 and has become a popular choice for many people looking for a quick and tasty meal. One of the things that makes Panda Express so good is the quality of their food. They use fresh ingredients and prepare their dishes with care, ensuring that each dish is flavorful and satisfying. The restaurant also offers a variety of options, from classic Chinese dishes like orange chicken and chow mein to more creative dishes like honey walnut shrimp and Beijing beef. This variety ensures that there is something for everyone, no matter what their tastes may be. Another great thing about Panda Express is their customer service. The staff is always friendly and helpful, and they are willing to go the extra mile to make sure that customers have a great experience. They also offer a variety of promotions and discounts, making it easy to save money while still enjoying a delicious meal. Finally, Panda Express is a great choice for those looking for a quick and convenient meal. The restaurant is open late, making it easy to grab a bite to eat after a long day. The restaurant also offers delivery and takeout options, making it even easier to enjoy their delicious food. Overall, Panda Express is a great choice for those looking for a delicious and convenient meal. The restaurant offers a variety of tasty dishes, friendly customer service, and convenient options, making it a great choice for anyone looking for a quick and tasty meal.'
    fill = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/div/div[2]/div[2]/div/div/div[2]/textarea')
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(fill)).send_keys(paragraph)
    next_button()

    #page 14
    fill = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[6]/span')
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(fill)).click()
    next_button()

    #page 15
    fill = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[3]/span')
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(fill)).click()
    next_button()

    #page 16
    fill = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/div/fieldset/div/div/div[2]/span/span')
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(fill)).click()
    next_button()

    #page 17
    fill = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/div/fieldset/div/div/div[2]/span/span')
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(fill)).click()
    next_button()
    
    #page 18
    fill = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[2]/span')
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(fill)).click()
    next_button()

    #page 19
    fill = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/div/fieldset/div/div/div[8]/span/span')
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(fill)).click()
    next_button()

    #page 20
    fill = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/div/fieldset/div/div/div[1]/span/span')
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(fill)).click()
    next_button()

    #page 21
    for i in range(2,6):
        fill = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[' + str(i) + ']/td[3]/span')
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(fill)).click()
    next_button()

    #page 22
    drp1 = Select(driver.find_element(By.ID, 'R000130'))
    drp1.select_by_visible_text('Male')
    drp2 = Select(driver.find_element(By.ID,'R000131'))
    drp2.select_by_visible_text('18 to 24')
    drp3 = Select(driver.find_element(By.ID,'R000132'))
    drp3.select_by_visible_text('Prefer not to answer')
    drp4 = Select(driver.find_element(By.ID,'R000133'))
    drp4.select_by_visible_text('Asian')
    next_button()

    #page 23
    for i in range(3,5):
        fill = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/div/div[' + str(i) + ']/div[2]/div/div/input')
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(fill)).send_keys(eml)
    
    next_button()


fill_code(access_code)
fill_survey(email)
print('complete! check email in 24 hours.')