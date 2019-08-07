# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 16:15:56 2019

@author: yamamoto
"""

from selenium import webdriver	

def main():
    # chromedriverのPATHを指定(herokuにおけるパスを指定しています)
    driver_path = '/app/.chromedriver/bin/chromedriver'
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    #driverに設定 ※optionsを指定しないとheadlessにならないので注意
    driver = webdriver.Chrome(options=options, executable_path=driver_path)
    driver.get("https://freebitco.in/?op=home")
    time.sleep(1) #1秒間待つ
    print(driver.current_url) #現在のURLを出力

    # 処理開始
    # 情報取得・加工
    # 処理終了

    # 終了
    driver.quit()

if __name__ == '__main__':
    main()