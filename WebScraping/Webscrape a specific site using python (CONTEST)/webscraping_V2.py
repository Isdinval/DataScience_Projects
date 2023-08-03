# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 12:44:39 2023

@author: Olivi
"""

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# URLs to scrape
urls = [
    ("https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket", "S3 Bucket"),
    ("https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_acl", "S3 Bucket ACL"),
    ("https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_cors_configuration", "S3 Bucket CORS Configuration"),
    ("https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_intelligent_tiering_configuration", "S3 Bucket Intelligent Tiering Configuration")
]

# Configure the options for the Chrome web driver (You can adjust this according to your preference)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without a graphical interface)

# Function to scrape and parse bullet points
def parse_bullet_points(url):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(5)  # You may need to increase or decrease this sleep time depending on the page loading time
    html_content = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html_content, 'html.parser')
    article_element = soup.find('article', {'id': 'provider-docs-content', 'class': 'column is-6 provider-docs-content'})
    ul_element = article_element.find('ul')

    bullet_points = []

    if ul_element:
        li_elements = ul_element.find_all('li')
        for li in li_elements:
            bullet_points.append(li.get_text())

    return bullet_points

# Initialize a writer to save DataFrames to Excel
writer = pd.ExcelWriter("parsed_bullet_points.xlsx", engine='xlsxwriter')

# Loop through each URL, parse the bullet points, and save them in a separate tab
for i, (url, tab_title) in enumerate(urls, 1):
    bullet_points = parse_bullet_points(url)

    parsed_bullet_points = []
    for bullet_point in bullet_points:
        parts = bullet_point.split(' - ', 1)
        if len(parts) == 2:
            parsed_bullet_points.append(parts)

    data = []
    for parsed_bullet_point in parsed_bullet_points:
        number, content = parsed_bullet_point
        data.append({"argument_name": number.strip(), "argument_description": content.strip()})

    df = pd.DataFrame(data)
    sheet_name = f"URL_{i}"
    df.to_excel(writer, sheet_name=sheet_name, index=False)

    # Add title to the tab
    worksheet = writer.sheets[sheet_name]
    worksheet.write(0, 0, tab_title, writer.book.add_format({'bold': True}))

# Save and close the writer
writer.save()
writer.close()

print("Data has been written to parsed_bullet_points.xlsx")