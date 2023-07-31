# Title: Society6 Design Upload Automation Script

## Description:
This Python script is an automation tool designed to facilitate the bulk uploading of artistic designs to Society6, a popular online marketplace for artists and creators. The script leverages various libraries and frameworks to interact with the Society6 website, manage image files, and perform repetitive tasks.

## Key Features:

### Web Automation: 
The script uses the Selenium library in conjunction with the undetected_chromedriver to automate interactions with the Society6 website. It can log in to the user's account and navigate through the design upload process seamlessly.

### Graphical User Interface (GUI): 
The script employs the tkinter library to create a simple GUI that allows users to select the folder containing their design images. The GUI also prompts the user to enter their Society6 account login credentials.

### Bulk Image Upload: 
The script utilizes the glob library to retrieve a list of image files (in .jpg format) from the specified folder. It then iterates through the images, pre-processes their names, and uploads them one by one to the Society6 platform.

### Image Preprocessing: 
The script includes a method called pre_name() that extracts the product name from the image filename. The method removes underscores and converts the name to uppercase for a clean and consistent presentation on Society6.

### Workaround for Keyboard Layout Issue: 
The script addresses a bug in the pyautogui.write() method related to non-QWERTY keyboard layouts. It employs pyperclip to copy the text to the clipboard and uses pyautogui.hotkey() to paste it, bypassing the issue and ensuring smooth text input.

### Progress Tracking: 
For improved user experience, the script includes a custom sleep_with_progress_bar() method that displays a progress bar while waiting for certain tasks to complete, enhancing the visibility of ongoing operations.

## Potential Use Case:
This automation script could be valuable for artists and designers who wish to showcase their work on Society6 efficiently. By automating the design upload process, the script saves time and effort, especially for artists with a large collection of artwork to upload. The GUI allows users to input their credentials easily and select the appropriate image folder, making it accessible to users with varying technical expertise.

## Note:
To use this script, users need to have Python and the required libraries installed on their system, such as Selenium, undetected_chromedriver, BeautifulSoup, tqdm, pyautogui, and pyperclip. Additionally, the script relies on an active internet connection and access to the Society6 website.

## Disclaimer:
This script is provided for educational and demonstration purposes only. Users should adhere to Society6's terms of service and guidelines when using this automation tool to avoid any potential violations or misuse of the platform.
