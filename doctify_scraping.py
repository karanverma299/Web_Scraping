from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
##pagination links#####
links=[]
l=('https://www.doctify.com/en-ae/find/dentistry/dubai/practices/page-{}#location=Dubai&distance=25')
for i in range(1,3):
 url = l.format(i)
 links.append(url)
len(links)


##to fetch clinics link###
clinicslink=[]
for i in links:
 from selenium import webdriver
 from time import sleep
 driver= webdriver.Chrome()
 driver.maximize_window()
 driver.get(i)
 print("Processing page:",i,len(clinicslink))
 wait = WebDriverWait(driver, 20)
 element = wait.until(EC.presence_of_element_located((By.XPATH,'//div//button[@mode="primary"]')))
 button=driver.find_element(By.XPATH,'//div//button[@mode="primary"]')
 button.click()
 sleep(1)
 y=driver.find_elements(By.XPATH,'//div//a[@class="MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineAlways muiltr-13a7lcf"]')
 for i in y:
  try:
    clinicslink.append(i.get_attribute("href"))
  except NoSuchElementException:
    clinicslink.append('none')
 driver.quit()
len(clinicslink)


##################################################

##updating because of some error in  previous clinic link list

l=[]
l.append(clinicslink)
updated_clinic_list = l[0]
len(updated_clinic_list)




###################             fetching  clinic details               #################

clinic_logo=[]
clinic_name=[]
clinic_address=[]
phonenumber=[]
aboutclinic=[]
doctorslink=[]
about=[]
email=[]
for i in xx:
 driver= webdriver.Chrome()
 driver.maximize_window()
 driver.get(i)
 wait = WebDriverWait(driver, 20)
 element = wait.until(EC.presence_of_element_located((By.XPATH,'//div//button[@mode="primary"]')))
 button=driver.find_element(By.XPATH,'//div//button[@mode="primary"]')
 button.click()
 try:
  x=driver.find_element(By.XPATH,'//*[@id="overview"]/div/div/div[1]/div/div[1]/div/div[1]/div/img')
 except NoSuchElementException:
  clinic_logo.append('none')
 o=driver.find_elements(By.XPATH,'//*[@id="overview"]/div/div/div[1]/div/div[1]/div/div[1]/div/img')
 for i in o:
  try:
   clinic_logo.append(i.get_attribute("src"))
  except NoSuchElementException:
    clinic_logo.append('none')
 try:
    z=driver.find_elements(By.XPATH,'//*[@id="overview"]/div/div/div[1]/div/div[2]/div/div[1]/h2')
 except NoSuchElementException:
   clinic_name.append('none')
 for i in z:
  try:
   clinic_name.append(i.text)
  except NoSuchElementException:
    clinic_name.append('none') 

 try:
    q=driver.find_elements(By.XPATH,'//*[@id="overview"]/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/p')
 except NoSuchElementException:
   clinic_address.append('none')
 for i in q:
  try:
   clinic_address.append(i.text)
  except NoSuchElementException:
    clinic_address.append('none')
 try:
  x=driver.find_elements(By.XPATH,'//div[@class="MuiBox-root muiltr-6i0pur"]')
  button=driver.find_element(By.XPATH,'//div//button[@class="MuiBox-root muiltr-1s887v"]')
  button.click()
 except NoSuchElementException:
  phonenumber.append('none')
  email.append('none')
 try:
  for i in x:
   phonenumber.append(driver.find_element(By.XPATH,'//div//a[@class="MuiBox-root muiltr-1t7jkp"]').get_attribute("href"))
 except NoSuchElementException:
  phonenumber.append('none')
 try:
  for i in x:
   if driver.find_element(By.XPATH,'//div//a[@class="MuiBox-root muiltr-1s887v"]').get_attribute("href").startswith("mailto:"):
      email.append(driver.find_element(By.XPATH,'//div//a[@class="MuiBox-root muiltr-1s887v"]').get_attribute("href"))
   else: 
     email.append('none')
 except NoSuchElementException:
  email.append('none')
    

  load_more_button_xpath = "//button[contains(text(), 'Load more specialists')]"
 max_attempts = 5
 for attempt in range(max_attempts):
    try:
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, load_more_button_xpath)))
        driver.find_element(By.XPATH, load_more_button_xpath).click()
        WebDriverWait(driver,2).until(EC.invisibility_of_element_located((By.XPATH, load_more_button_xpath)))
    except:
        continue  
 try:
   driver.find_element(By.XPATH,'//div//div[@class="MuiGrid-root MuiGrid-container MuiGrid-item MuiGrid-direction-xs-column MuiGrid-grid-xs-true muiltr-j6ucl"]//a')
 except NoSuchElementException:
   doctorslink.append('none')
 try:
  p=driver.find_elements(By.XPATH,'//div//div[@class="MuiGrid-root MuiGrid-container MuiGrid-item MuiGrid-direction-xs-column MuiGrid-grid-xs-true muiltr-j6ucl"]//a')
  for i in p:
   doctorslink.append(i.get_attribute("href"))
 except NoSuchElementException:
   doctorslink.append('none')
 try:
  about.append(driver.find_element(By.XPATH,'//div//span[@class=" muiltr-427cpn"]').text)
 except NoSuchElementException:
  about.append('none')
 driver.quit()
 print("Processing page:",i,len(clinic_address),len(clinic_logo),len(phonenumber),len(clinic_name),len(email),len(doctorslink))


## extracting country & city from clinic_address ##
country=[]
for i in clinic_address:
    parts = i.split(',')
    last_part = parts[-1].strip()
    country.append(last_part)

city=[]
for i in clinic_address:
 parts = i.split(',')
 last_part = parts[-2].strip()
 city.append(last_part)

##clinic data###########
import pandas as pd
df=pd.DataFrame({'clinic name':clinic_name,'clinic_address':clinic_address,'city':city,'country':country,'phonenumber':phonenumber,'email':email,'about':about,'clinic_logo':clinic_logo,'clinicslink':clinicslink})
len(clinic_name),len(clinic_address),len(city),len(country),len(phonenumber),len(email),len(clinic_logo),len(clinicslink),len(about)
df.head(2)
df.to_csv('doctify_hospital_list.csv', index=False)
################################################






###fetching  doctor details### 
## u can replace linkss with doctors_link###



linkss=['https://www.doctify.com/en-ae/specialist/bashir-mustafa', 'https://www.doctify.com/en-ae/specialist/david-aman-eddine', 'https://www.doctify.com/en-ae/specialist/david-amaneddine', 'https://www.doctify.com/en-ae/specialist/alaa-obeid', 'https://www.doctify.com/en-ae/specialist/zoubir-boudi', 'https://www.doctify.com/en-ae/specialist/safiah-yousef', 'https://www.doctify.com/en-ae/specialist/swarna-latha', 'https://www.doctify.com/en-ae/specialist/nishi-grover', 'https://www.doctify.com/en-ae/specialist/syed-mohammed-ashraf', 'https://www.doctify.com/en-ae/specialist/urmi-mazumder','https://www.doctify.com/en-ae/specialist/aruna-satpathy', 'https://www.doctify.com/en-ae/specialist/jibsy-vakayil-verghezse', 'https://www.doctify.com/en-ae/specialist/sindhu-ambujakshi', 'https://www.doctify.com/en-ae/specialist/urumese-mampilly-antony','https://www.doctify.com/en-ae/specialist/archana-prince', 'https://www.doctify.com/en-ae/specialist/rhea-vibin', 'https://www.doctify.com/en-ae/specialist/navya', 'https://www.doctify.com/en-ae/specialist/prateek-mathur', 'https://www.doctify.com/en-ae/specialist/mawada-hussain-alabo', 'https://www.doctify.com/en-ae/specialist/rayyan-bhalla', 'https://www.doctify.com/en-ae/specialist/rimpal-rao', 'https://www.doctify.com/en-ae/specialist/reem-abdelrahman', 'https://www.doctify.com/en-ae/specialist/amer-bahaa-sweiss', 'https://www.doctify.com/en-ae/specialist/roula-samir-nasser', 'https://www.doctify.com/en-ae/specialist/divya-nair', 'https://www.doctify.com/en-ae/specialist/esther-gina', 'https://www.doctify.com/en-ae/specialist/sherin-shahana', 'https://www.doctify.com/en-ae/specialist/ahmad-deeb', 'https://www.doctify.com/en-ae/specialist/salahudeen-aboobacker', 'https://www.doctify.com/en-ae/specialist/mahmood-elrayes']
len(linkss)
name=[]
doctor_image_link=[]
specialization=[]
about=[]
doctor_phone_number=[]
experience=[]
doctor_email=[]
qualification=[]
working_clinic=[]
for i in linkss:
 driver= webdriver.Chrome()
 driver.maximize_window()
 driver.get(i)
 wait = WebDriverWait(driver, 20)
 element = wait.until(EC.presence_of_element_located((By.XPATH,'//div//button[@mode="primary"]')))
 button=driver.find_element(By.XPATH,'//div//button[@mode="primary"]')
 button.click()
 try:
     qualification.append(driver.find_element(By.XPATH,'//div[@class="MuiBox-root muiltr-87zgb4"]').text)
 except NoSuchElementException:
  qualification.append('none')
 try:
     doctor_image_link.append(driver.find_element(By.XPATH,'//*[@id="overview"]/div/div/div[1]/div/div[1]/div/div[1]/div/img').get_attribute("src"))
 except NoSuchElementException:
  doctor_image_link.append('none')
 try:
     name.append(driver.find_element(By.XPATH,'//div//h2[@class="MuiTypography-root MuiTypography-h2 muiltr-icysp"]').text)
 except NoSuchElementException:
  name.append('none')
 try:
     specialization.append(driver.find_element(By.XPATH,'//div[@class="MuiGrid-root MuiGrid-container MuiGrid-spacing-xs-2.5 muiltr-xj0bra"]').text)
 except NoSuchElementException:
    specialization.append('none')
 try:
     experience.append(driver.find_element(By.XPATH,'//*[@id="overview"]/div/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[2]/div/h2').text)
 except NoSuchElementException:
    experience.append('none')
 try:
     about.append(driver.find_element(By.XPATH,'//div//span[@class=" muiltr-427cpn"]').text)
 except NoSuchElementException:
  about.append('none')
 try:
     driver.find_element(By.XPATH,'//div[@class="MuiBox-root muiltr-15hiasm"]')
 except NoSuchElementException:
    doctor_phone_number.append('none')
 try:
     button=driver.find_element(By.XPATH,'//div[@class="MuiBox-root muiltr-15hiasm"]')
     button.click()
     buttonr=driver.find_element(By.XPATH,'//div//button[@class="MuiBox-root muiltr-1s887v"]')
     buttonr.click()
     doctor_phone_number.append(driver.find_element(By.XPATH,'//div//a[@class="MuiBox-root muiltr-1t7jkp"]').get_attribute("href"))
     doctor_email.append(driver.find_element(By.XPATH,'//div//a[@class="MuiBox-root muiltr-sqdczr"]').get_attribute("href"))
 except NoSuchElementException:
    doctor_email.append('none')
 try:
     working_clinic.append(driver.find_element(By.XPATH,'//div//h4[@class="MuiTypography-root MuiTypography-h4 muiltr-11p984c"]').text)
 except NoSuchElementException:
   working_clinic.append('none')


location=[]
for i in specialization:
     end=i.split('\n')
     ending=end[-1].strip()
     location.append(ending)





name,specialization,about,qualification,experience,doctor_phone_number,doctor_image_link,location,doctor_email,linkss,working_clinic

len(name),len(specialization),len(about),len(qualification),len(experience),len(doctor_phone_number),len(doctor_image_link),len(location),len(doctor_email),len(linkss),len(working_clinic)

df1=pd.DataFrame({'doctor_name':name,'specialization':specialization,'about':about,'qualification':qualification,'experience':experience,'doctor_phone_number':doctor_phone_number,'abodoctor_image_link':doctor_image_link,'location':location,'doctor_email':doctor_email,'link':linkss,'working_clinic':working_clinic})
df1.head()


df1.to_csv('doctify_doctor_list.csv', index=False)