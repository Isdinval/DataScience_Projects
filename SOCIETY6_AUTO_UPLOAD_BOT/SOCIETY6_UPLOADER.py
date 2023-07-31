# ==========================================================================
# LIRBARY
# ==========================================================================
import glob
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
from random import randint
import pyautogui
import pyperclip

# ==========================================================================
# VARIOUS METHODS
# ==========================================================================
def sleep_with_progress_bar(seconds):
    for remaining in tqdm(range(seconds), desc="Waiting", unit="sec"):
        time.sleep(1)

# Function to check if the element exists or not
def is_element_present(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
        return True
    except:
        return False
    
    
    
# This is a work-around for the bug in pyautogui.write() with non-QWERTY keyboards
# It copies the text to clipboard and pastes it, instead of typing it.
def _workaround_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')
    # pyperclip.copy('')
    # pyautogui.click()  # Simulate a click to ensure the input field is selected



# Slicing product name if you need. You can see the example below
# In the example we get the product name from "black_and_white_abstract_dots_pattern_baby_blanket-r38548522b52d4124bd270cf8060f89b3_jz0n5.jpg"
# After function pre_name will be  "BLACK AND WHITE ABSTRACT DOTS PATTERN BABY BLANKET"
# You can edit this section to get desired name
def pre_name():
    ind = img.rfind(".")  # Find the last occurrence of "." to get the file extension
    product = img[:ind]  # Get the part of the filename before the extension
    pre_name = product.replace("_", " ")  # Replace underscores with spaces
    pre_name = pre_name.upper()  # Convert to uppercase
    return pre_name



def login():
    print('You must login into SOCIETY6')
    # Open Pinterest on Chrome Driver
    driver.get('https://society6.com/')

    # Click log in button
    time.sleep(2) 
    login_button_xpath = '/html/body/div[1]/div/div[4]/div[1]/div/header/div/nav[2]/div[3]/span'
    element_PreLoginButton = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, login_button_xpath)))
    element_PreLoginButton.click()
    
    
    ## Log in
    email_textbox_xpath = '/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/form/input[1]'
    element_identifiant = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, email_textbox_xpath)))
    element_identifiant.clear()
    element_identifiant.send_keys(user_name)
    
    password_textbox_xpath = '/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/form/input[2]'
    element_password = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, password_textbox_xpath)))
    element_password.clear()
    element_password.send_keys(user_password)
    
    signin_button_xpath = '/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/form/button'
    element_loginButton = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, signin_button_xpath)))
    element_loginButton.click()
    
    # Now, wait for the element to disappear signin_button_xpath. It means that the connexion succedeed. 
    timeout = 40  # Maximum waiting time in seconds
    interval = 2  # Time interval between each check in seconds
    while timeout > 0:
        if not is_element_present(signin_button_xpath):
            break
        else:
            timeout -= interval
            time.sleep(interval)          
                
        
def upload_Design():
    # Add New Design
    print("Add New Design")
    addNewDesign_button_xpath = '/html/body/div[1]/div/div[4]/div[2]/div/div/div[1]/div[2]/button'
    element_AddNewDesign = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, addNewDesign_button_xpath)))
    element_AddNewDesign.click()

    # Add An Image
    # sleep_with_progress_bar(10)
    print("Add An Image")
    # Get path of the current image
    test_image_file = name.title() + '.jpg'
    image_path = os.path.abspath(os.path.join(image_file, test_image_file))
    
    selectFile_Container_xpath = '/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div/div[1]'
    element_selectFile = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, selectFile_Container_xpath)))
    element_selectFile.send_keys(image_path)
    print(image_path)
    time.sleep(3)   
    _workaround_write(image_path)
    sleep_with_progress_bar(5)   
    # Get the new mouse position after the click
    new_x, new_y = pyautogui.position()
    print(f"New mouse position: x={new_x}, y={new_y}")
    # pyautogui.typewrite(['enter'])  # Use typewrite() to simulate pressing "Enter"


    # Add A Title
    print("Add A Title")
    enterDesignTitle_xpath = '/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/input'
    element_enterDesignTitle = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, enterDesignTitle_xpath)))
    element_enterDesignTitle.clear()
    element_enterDesignTitle.send_keys(name.title())
    
    sleep_with_progress_bar(50)
# ==========================================================================
# INIT
# ==========================================================================
# SOCIETY6 DETAILS
user_name = ""
user_password = ""


# Definitions about pins
image_file = "path"
# Replacing backslashes with forward slashes
image_file = image_file.replace("\\", "\\\\")
description = "In the realm of boundless imagination, a captivating scene of enchantment unfolds, crafted by the visionary Designer Isdinval. Within the ethereal strokes of watercolor dreams, a delicate girl, reminiscent of a sylph or sprite, finds herself entrapped in a sealed glass jar. The alchemy of glass and watercolor brings her to life, blurring the lines between fantasy and reality, leaving us spellbound by the artistry."

# ==========================================================================
# GET IMAGE LIST FROM FOLDER
# ==========================================================================
image_list = []
folder_path = image_file
for filename in glob.glob(os.path.join(folder_path, '*.jpg')):
    filename = os.path.basename(filename)
    image_list.append(filename)
    
    

# ==========================================================================
# UNDETECTED CHROMEDRIVER
# ==========================================================================
options = ChromeOptions()
options.add_argument('--user-data-dir=' + os.getcwd() + '/chrome_profile')
driver = undetected_chromedriver.Chrome(options=options)
driver.maximize_window()




# ==========================================================================
#  ================                  MAIN                   ================
# ==========================================================================
login()
i = 0

# while i < len(image_list):
while i < 2:
    for img in image_list:
        driver.get('https://society6.com/artist-studio')
        name = pre_name()
        print('name')
        print(name)
        upload_Design()
        i += 1
        print("{} image(s) have been uploaded.".format(i))

print("All done! I've uploaded {} images!".format(i))
# driver.quit()

