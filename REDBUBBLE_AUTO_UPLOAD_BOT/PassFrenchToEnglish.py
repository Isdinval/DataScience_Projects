# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 08:40:21 2023

@author: Olivi
"""

import pyautogui
import time
import winsound
import keyboard
from tqdm import tqdm

 
# # Get the new mouse position after the click 
# new_x, new_y = pyautogui.position() 
# print(f"New mouse position: x={new_x}, y={new_y}")  
 
# # ==============================================================
# # COMMENTS
# # ==============================================================  
# 1. Windows size is maximize       
# 2. Zoom is 80%. 


def sleep_with_progress_bar(seconds):
    for remaining in tqdm(range(seconds), desc="Waiting", unit="sec"):
        time.sleep(1)


  
sleetpTime = 0.20  
  

# # ==============================================================   
# # OPEN THE 8 DESIGNS THAT WE WANTS TO MODIFY FRENCH AND ENGLISH 
# # ==============================================================  
def get_user_input():
    print("Move your mouse to the desired position and press the spacebar.") 
    print("Press 'q' to quit.")  
       
    while True: 
        x, y = pyautogui.position()   
        position_str = f"Current mouse position: x={x}, y ={y}\n" 
        print(position_str, end="")
        
        if keyboard.is_pressed('q'):
            print("\nQuitting...")
            return None
         
        if keyboard.is_pressed('space'):
            print(f"\nPosition selected: x={x}, y={y}")
            return x, y 

# Get Coordinates of the first Design (IT HAS TO BE THE FIRST OF A ROW !!!) 
coordinates = get_user_input()
target_x_user, target_y_user = coordinates


# 1ST ROW
for i in range(1, 5):
        # click on the wheel
        time.sleep(sleetpTime ) 
        target_x, target_y = target_x_user+(i-1)*190, target_y_user  # Replace these coordinates with the desired location
        pyautogui.click(x=target_x, y=target_y)
        # right click on edit
        time.sleep(sleetpTime) 
        target_x, target_y = target_x_user+(i-1)*190, target_y_user+69  # Replace these coordinates with the desired location
        pyautogui.rightClick(x=target_x, y=target_y)
        # click on Ouvrir  le lien dans un nouvel onglet
        time.sleep(sleetpTime) 
        target_x, target_y = target_x_user+(i-1) *190+45, target_y_user+81  # Replace these coordinates with the desired location
        pyautogui.click(x=target_x, y=target_y)
        
# 2ND ROW
for i in range(1, 5):
        # click on the wheel
        time.sleep(sleetpTime) 
        target_x, target_y = target_x_user+(i-1)*190, target_y_user+272  # Replace these coordinates with the desired location
        pyautogui.click(x=target_x, y=target_y)
        # right click on edit
        time.sleep(sleetpTime)   
        target_x, target_y = target_x_user+(i-1)*190, target_y_user+272+69  # Replace these coordinates with the desired location
        pyautogui.rightClick(x=target_x, y=target_y)
        # click on Ouvrir le lien dans un nouvel onglet
        time.sleep(sleetpTime) 
        target_x, target_y = target_x_user+(i-1)*190+45, target_y_user+272+81  # Replace these coordinates with the desired location
        pyautogui.click(x=target_x, y=target_y) 


# ==============================================================
# WAIT THAT ALL IMAGES ARE DISPLAYED, SO THE TEXT IS INTERACTIBLE
# ==============================================================
sleep_with_progress_bar(18)

# ==============================================================
# CHANGE FRENCH TO ENGLISH
# ==============================================================
for i in range(1, 9):
    # ======================================================
    # TAB
    # ======================================================
    # click on tab
    time.sleep(sleetpTime) 
    target_x, target_y = 2210+(i-1)*184, 18  # Replace these coordinates with the desired location
    pyautogui.click(x=target_x, y=target_y)
    time.sleep(1)
    
    # ======================================================
    # TITLE
    # ======================================================
    # click on French
    time.sleep(sleetpTime) 
    target_x, target_y = 3037, 407  # Replace these coordinates with the desired location
    pyautogui.click(x=target_x, y=target_y)
    time.sleep(sleetpTime) 
    # click on title, then select all and copy
    target_x, target_y = 3010, 550  # Replace these coordinates with the desired location
    pyautogui.click(x=target_x, y=target_y)
    time.sleep(sleetpTime) 
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(sleetpTime) 
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(sleetpTime)  # Add a small delay to allow time for copying to the clipboard
    # click on English
    target_x, target_y = 2848, 407  # Replace these coordinates with the desired location
    pyautogui.click(x=target_x, y=target_y)
    # click on title, then select all and paste
    target_x, target_y = 2910, 507  # Replace these coordinates with the desired location
    pyautogui.click(x=target_x, y=target_y)
    time.sleep(sleetpTime) 
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(sleetpTime) 
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(sleetpTime)  # Add a small delay to allow time for copying to the clipboard
    
    # ======================================================
    # TAGS
    # ======================================================
    # click on French
    target_x, target_y = 3037, 407  # Replace these coordinates with the desired location
    pyautogui.click(x=target_x, y=target_y)
    # click on tags, then select all and copy
    target_x, target_y = 2977, 675  # Replace these coordinates with the desired location
    pyautogui.click(x=target_x, y=target_y)
    time.sleep(sleetpTime) 
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(sleetpTime) 
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(sleetpTime)  # Add a small delay to allow time for copying to the clipboard
    # click on English
    target_x, target_y = 2848, 407  # Replace these coordinates with the desired location
    pyautogui.click(x=target_x, y=target_y)
    # click on title, then select all and paste
    target_x, target_y = 2884, 641  # Replace these coordinates with the desired location
    pyautogui.click(x=target_x, y=target_y)
    time.sleep(sleetpTime) 
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(sleetpTime) 
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(sleetpTime)  # Add a small delay to allow time for copying to the clipboard
    
    # ======================================================
    # DESCRIPTION
    # ======================================================
    # click on French
    target_x, target_y = 3037, 407  # Replace these coordinates with the desired location
    pyautogui.click(x=target_x, y=target_y)
    # click on tags, then select all and copy
    target_x, target_y = 2967, 783  # Replace these coordinates with the desired location
    pyautogui.click(x=target_x, y=target_y)
    time.sleep(sleetpTime) 
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(sleetpTime) 
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(sleetpTime)  # Add a small delay to allow time for copying to the clipboard
    # click on English
    target_x, target_y = 2848, 407  # Replace these coordinates with the desired location
    pyautogui.click(x=target_x, y=target_y)
    # click on title, then select all and paste
    target_x, target_y = 2881, 746  # Replace these coordinates with the desired location
    pyautogui.click(x=target_x, y=target_y)
    time.sleep(sleetpTime) 
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(sleetpTime) 
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(sleetpTime)  # Add a small delay to allow time for copying to the clipboard
    
    # ======================================================
    # REMOVE "WANT TO TRANSLATE ...  ?"
    # ======================================================
    # click on "WANT TO TRANSLATE .. ?"
    # click on French
    target_x, target_y = 3037, 407  # Replace these coordinates with the desired location
    pyautogui.click(x=target_x, y=target_y)
    time.sleep(sleetpTime)  # Add a small delay to allow time for copying to the clipboard
    target_x, target_y = 2814, 445  # Replace these coordinates with the desired location
    pyautogui.click(x=target_x, y=target_y)
    time.sleep(sleetpTime)  # Add a small delay to allow time for copying to the clipboard
    
    
    # ======================================================
    #  Scroll the mouse wheel down
    # ======================================================
    scroll_amount = -4500
    pyautogui.scroll(scroll_amount)
    
    # ======================================================
    #  I AGREE.... AND .... SAVE WORK ...
    # ======================================================
    time.sleep(sleetpTime)  # Add a small delay to allow time for copying to the clipboard
    target_x, target_y = 2499, 493  # Replace these coordinates with the desired location
    pyautogui.click(x=target_x, y=target_y)
    time.sleep(sleetpTime)  # Add a small delay to allow time for copying to the clipboard
    target_x, target_y = 3220, 555  # Replace these coordinates with the desired location
    pyautogui.click(x=target_x, y=target_y)
    

# At the end of the script, after the loop
# Add a music signal when the script finishes
frequency = 1500  # Frequency of the beep sound in Hz
duration = 3000   # Duration of the beep sound in milliseconds
winsound.Beep(frequency, duration)
