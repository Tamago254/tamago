# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""

from selenium import webdriver	

# chromedriverのPATHを指定(herokuにおけるパスを指定しています)
    driver_path = '/app/.chromedriver/bin/chromedriver'
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    #driverに設定 ※optionsを指定しないとheadlessにならないので注意
    driver = webdriver.Chrome(options=options, executable_path=driver_path)
    driver.get("https://freebitco.in/?op=home")
