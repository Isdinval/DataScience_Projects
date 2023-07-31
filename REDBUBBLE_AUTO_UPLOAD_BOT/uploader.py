# ===============================================================================================================================
#                                                   IMPORT LIBRARIES
# ===============================================================================================================================
import undetected_chromedriver
from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import os
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
from bs4 import BeautifulSoup
from functools import partial
from tqdm import tqdm
import shutil



# ===============================================================================================================================
#                                                       FUNCTIONS
# ===============================================================================================================================
def sleep_with_progress_bar(seconds):
    for remaining in tqdm(range(seconds), desc="Waiting", unit="sec"):
        time.sleep(1)

def is_logged_in(driver):
    driver.get('https://www.redbubble.com/portfolio/manage_works?ref=account-nav-dropdown')
    time.sleep(0.5)
    return driver.current_url != 'https://www.redbubble.com/auth/login'

def get_template_link(driver):
    # Manual selection
    return 'https://www.redbubble.com/fr/portfolio/images/148915537-jellyfish-forest-twilight-magic-in-a-mushroomed-wonderland/duplicate'

def create_driver():
    options = ChromeOptions()
    options.add_argument('--user-data-dir=' + os.getcwd() + '/chrome_profile')
    #return uc.Chrome(options=options)
    return undetected_chromedriver.Chrome(options=options)

def is_image(file):
    return file[-3:] == 'png' or file[-3:] == 'jpg'



# ===============================================================================================================================
#                                                       CLASS DESIGN
# ===============================================================================================================================
class Design:
    def __init__(self, location, tags):
        self.location = location.replace('/', '\\')
        self.title = self.location.split('\\')[-1][:-4]
        self.tags = ', '.join(self.title.split()) if tags is None else tags
        self.desc = f'{self.title}: {self.tags}'

    def __repr__(self):
        return f'RB Design: {self.title}'



# ===============================================================================================================================
#                                                       CLASS BOT
# ===============================================================================================================================
class Bot:
    def __init__(self):
        self.designs = []

    def add_designs(self, dir):
        tags = open(dir + '/tags.txt', 'r').read() if os.path.exists(dir + '/tags.txt') else None
        print("TAGS")
        print(tags)
        self.designs += [Design(f'{dir}/{file}', tags) for file in os.listdir(dir) if is_image(file)]

    def upload_designs(self):
        print('')
        print("I. CREATE DRIVER")
        driver = create_driver()
        driver.maximize_window()
        if not is_logged_in(driver):
            print(
                'You must login into Redbubble. If you are using the same Chrome Profile, you only need to do this once\nOnce you login, the bot will automatically continue')
            wait = WebDriverWait(driver, 300)
            # This should be the landing page after logging in
            wait.until(lambda driver: driver.current_url == "https://www.redbubble.com/explore/for-you/#" or
                                       driver.current_url == 'https://www.redbubble.com/portfolio/manage_works?ref=account-nav-dropdown')

        template_link = get_template_link(driver)
        
        # sleep to wait pass
        time.sleep(6) 
        
        start = time.time()
        cnt_design = 0
        for design in self.designs:
            try:
                cnt_design = cnt_design+1
                
                print("\n")
                print('Design'+str(cnt_design))
                
                print("II. GET TEMPLATE LINK")
                driver.get(template_link)
                
                print("III. TITTLE")
                element_tittleV0 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#work_title_en")))
                element_tittleV0.clear()
                element_tittleV0.send_keys(design.title)
                #element_tittle = driver.find_element(By.CSS_SELECTOR, '#work_title_fr')
                #element_tittle.clear()
                #element_tittle.send_keys(design.title)
                
                print("IV. TAGS")
                element_tags = driver.find_element(By.CSS_SELECTOR, '#work_tag_field_en')
                element_tags.clear()
                element_tags.send_keys(design.tags)
                
                print("V. DESCRIPTION")
                element_description = driver.find_element(By.CSS_SELECTOR, '#work_description_en')
                element_description.clear()
                element_description.send_keys(design.desc)
    
                print("VI. SELECT IMAGE")
                driver.find_element(By.CSS_SELECTOR, '#select-image-base').send_keys(design.location)
                #time.sleep(90)
                element_circleProgress = '0'
                while int(element_circleProgress) < 100:
                    element_circleProgress = driver.find_element(By.CSS_SELECTOR, '#add-new-work > div > div.duplicate > div.single-upload.with-uploader > div.circle-progress').get_attribute('data-value')
                print('VI. SELECT IMAGE - UPLOAD FINISHED')
                    
                sleep_with_progress_bar(8)
                
                print("VII. SUBMIT WORK")
                element_rightsDeclaration = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#rightsDeclaration")))
                element_rightsDeclaration.click()
                
                #driver.find_element(By.CSS_SELECTOR, '#rightsDeclaration').click()
                element_submitWork = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#submit-work")))
                element_submitWork.click()
                wait = WebDriverWait(driver, 90)
                wait.until(lambda driver: ('https://www.redbubble.com/fr/studio/promote/' or 'https://www.redbubble.com/studio/promote/148917210?ref=uploader-to-promote&visit_status=first-time') in driver.current_url)
                
                # Move the image to the destination folder
                parent_folder = os.path.dirname(design.location)
                destination_folder = os.path.join(parent_folder, 'END')
                os.makedirs(destination_folder, exist_ok=True)  # Create the "END" subfolder if it doesn't exist
                shutil.move(design.location, destination_folder)
                print("VIII. IMAGE HAVE BEEN MOVED TO SUBPARENT FOLDER /END !!!")
            
            except TimeoutException as e:
                print(f"Timeout occurred while processing Design {cnt_design}. Error: {e}")
                break

        print(f'Uploaded {len(self.designs)} Design(s) in {round((time.time() - start) / 60, 2)} Minutes')
        driver.quit()

# ===============================================================================================================================
#                                                       MAIN
# ===============================================================================================================================
def run_gui():
    bot = Bot()
    current_row = ['']
    root = Tk()

    def open_dir(current_row):
        root.filename = filedialog.askdirectory(title='Select A Folder With Your Designs')
        if root.filename != '':
            dir_entry = Entry(root, width=50)
            dir_entry.insert(0, root.filename)
            dir_entry.grid(row=len(current_row), column=0)
            found_designs_label = Label(root,
                                        text='Found ' + str(
                                            len([file for file in os.listdir(root.filename) if is_image(file)])) + ' Designs')
            found_designs_label.grid(row=len(current_row), column=1)
            upload_button.grid(row=len(current_row) + 1, column=0, pady=(15, 15))
            current_row.append('')
            bot.add_designs(root.filename)

    def upload():
        if len(bot.designs) != 0:
            bot.upload_designs()
        else:
            messagebox.showwarning('Empty Fields', 'Please select at least one folder with valid designs')

    open_dir_current = partial(open_dir, current_row)
    dir_button = Button(root, text='Add Designs', command=open_dir_current)
    upload_button = Button(root, text='upload', command=upload)
    dir_button.grid(row=0, column=0)

    root.mainloop()


if __name__ == '__main__':
    run_gui()
