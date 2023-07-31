# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 13:37:37 2023

@author: Olivi
"""

import os

folder_path = r"D:\easy_diffusion\TODO\JELLYFISHFOREST\RED JELLY\BIG\TRANSFORMED"
text_file_path = r"D:\easy_diffusion\TODO\JELLYFISHFOREST\RED JELLY\BIG\newTitles.txt"

def remove_empty_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Remove empty lines
        lines = [line for line in lines if line.strip()]
        
        with open(file_path, 'w') as file:
            file.writelines(lines)
    except IOError as e:
        print(f"Error removing empty lines: {str(e)}")

def rename_images(folder_path, text_file_path):
    if not os.path.exists(folder_path):
        print("Folder path does not exist.")
        return

    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    if not os.path.isfile(text_file_path):
        print("Invalid text file path.")
        return

    try:
        remove_empty_lines(text_file_path)  # Remove empty lines from the text file

        with open(text_file_path, 'r') as file:
            titles = file.read().splitlines()
    except IOError as e:
        print(f"Error reading text file: {str(e)}")
        return

    file_names = os.listdir(folder_path)
    if len(file_names) != len(titles):
        print("Number of titles does not match the number of images.")
        print("Number of titles: " + str(len(titles)))
        print("Number of files: " + str(len(file_names)))
        return

    for i, file_name in enumerate(file_names):
        if file_name.endswith(".jpg"):  # Adjust the file extension if necessary
            new_title = titles[i]
            file_path = os.path.join(folder_path, file_name)
            new_file_name = f"{new_title}.jpg"  # Adjust the file extension if necessary
            new_file_path = os.path.join(folder_path, new_file_name)
            try:
                os.rename(file_path, new_file_path)
                print(f"Renamed '{file_name}' to '{new_file_name}'.")
            except OSError as e:
                print(f"Error renaming file '{file_name}': {str(e)}")

rename_images(folder_path, text_file_path)
