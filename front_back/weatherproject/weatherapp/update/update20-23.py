from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv


def sevenpants():
    browser = webdriver.Chrome('C:/chromedriver.exe')
    browser.get('https://www.musinsa.com/app/')
    browser.implicitly_wait(3)

    search = browser.find_element_by_css_selector(
        'input.search.head-search-inp')
    search.click()

    search.send_keys('7부 바지')
    search.send_keys(Keys.ENTER)

    time.sleep(2)

    # ..
    browser.execute_script('window.scrollTo(0, 2000)')
    time.sleep(2)

    products = browser.find_element_by_css_selector('a.btn-all.font-mss')
    products.click()

    # scrolling
    before_h = browser.execute_script("return window.scrollY")
    while True:
        # To END : 전 높이 (before_h) /후 높이
        browser.find_element_by_css_selector("body").send_keys(Keys.END)
        time.sleep(1)

        after_h = browser.execute_script("return window.scrollY")

        if after_h == before_h:
            break
        before_h = after_h

    f = open(r"7부바지_data.csv", 'w', encoding='CP949', newline='')
    csvWriter = csv.writer(f)
    items = browser.find_elements_by_css_selector("#searchList li.li_box")

    for item in items:
        title = item.find_element_by_css_selector(
            ".list_img > a").get_attribute('title')
        print(title)
        link = item.find_element_by_css_selector(
            ".list_img > a").get_attribute('href')
        print(link)
        image = item.find_element_by_css_selector(
            ".lazyload.lazy").get_attribute('data-original')
        print(image)
        csvWriter.writerow([title, link, image])


def longt():

    browser = webdriver.Chrome('C:/chromedriver.exe')
    browser.get('https://www.musinsa.com/app/')
    browser.implicitly_wait(3)

    search = browser.find_element_by_css_selector(
        'input.search.head-search-inp')
    search.click()

    search.send_keys('긴팔티')
    search.send_keys(Keys.ENTER)

    time.sleep(2)

    # ..
    browser.execute_script('window.scrollTo(0, 2000)')
    time.sleep(2)

    products = browser.find_element_by_css_selector('a.btn-all.font-mss')
    products.click()

    # scrolling
    before_h = browser.execute_script("return window.scrollY")
    while True:
        # To END : 전 높이 (before_h) /후 높이
        browser.find_element_by_css_selector("body").send_keys(Keys.END)
        time.sleep(1)

        after_h = browser.execute_script("return window.scrollY")

        if after_h == before_h:
            break
        before_h = after_h

    f = open(r"긴팔티_data.csv", 'w', encoding='CP949', newline='')
    csvWriter = csv.writer(f)
    items = browser.find_elements_by_css_selector("#searchList li.li_box")

    for item in items:
        title = item.find_element_by_css_selector(
            ".list_img > a").get_attribute('title')
        print(title)
        link = item.find_element_by_css_selector(
            ".list_img > a").get_attribute('href')
        print(link)
        image = item.find_element_by_css_selector(
            ".lazyload.lazy").get_attribute('data-original')
        print(image)
        csvWriter.writerow([title, link, image])


def shirt():

    browser = webdriver.Chrome('C:/chromedriver.exe')
    browser.get('https://www.musinsa.com/app/')
    browser.implicitly_wait(3)

    search = browser.find_element_by_css_selector(
        'input.search.head-search-inp')
    search.click()

    search.send_keys('셔츠')
    search.send_keys(Keys.ENTER)

    time.sleep(2)

    # ..
    browser.execute_script('window.scrollTo(0, 2000)')
    time.sleep(2)

    products = browser.find_element_by_css_selector('a.btn-all.font-mss')
    products.click()

    # scrolling
    before_h = browser.execute_script("return window.scrollY")
    while True:
        # To END : 전 높이 (before_h) /후 높이
        browser.find_element_by_css_selector("body").send_keys(Keys.END)
        time.sleep(1)

        after_h = browser.execute_script("return window.scrollY")

        if after_h == before_h:
            break
        before_h = after_h

    f = open(r"셔츠_data.csv", 'w', encoding='CP949', newline='')
    csvWriter = csv.writer(f)
    items = browser.find_elements_by_css_selector("#searchList li.li_box")

    for item in items:
        title = item.find_element_by_css_selector(
            ".list_img > a").get_attribute('title')
        print(title)
        link = item.find_element_by_css_selector(
            ".list_img > a").get_attribute('href')
        print(link)
        image = item.find_element_by_css_selector(
            ".lazyload.lazy").get_attribute('data-original')
        print(image)
        csvWriter.writerow([title, link, image])


def onepiece():

    browser = webdriver.Chrome('C:/chromedriver.exe')
    browser.get('https://www.musinsa.com/app/')
    browser.implicitly_wait(3)

    search = browser.find_element_by_css_selector(
        'input.search.head-search-inp')
    search.click()

    search.send_keys('반팔 원피스')
    search.send_keys(Keys.ENTER)

    time.sleep(2)

    # ..
    browser.execute_script('window.scrollTo(0, 2000)')
    time.sleep(2)

    products = browser.find_element_by_css_selector('a.btn-all.font-mss')
    products.click()

    # scrolling
    before_h = browser.execute_script("return window.scrollY")
    while True:
        # To END : 전 높이 (before_h) /후 높이
        browser.find_element_by_css_selector("body").send_keys(Keys.END)
        time.sleep(1)

        after_h = browser.execute_script("return window.scrollY")

        if after_h == before_h:
            break
        before_h = after_h

    f = open(r"원피스_data.csv", 'w', encoding='CP949', newline='')
    csvWriter = csv.writer(f)
    items = browser.find_elements_by_css_selector("#searchList li.li_box")

    for item in items:
        title = item.find_element_by_css_selector(
            ".list_img > a").get_attribute('title')
        print(title)
        link = item.find_element_by_css_selector(
            ".list_img > a").get_attribute('href')
        print(link)
        image = item.find_element_by_css_selector(
            ".lazyload.lazy").get_attribute('data-original')
        print(image)
        csvWriter.writerow([title, link, image])


def mozori():
    sevenpants()
    longt()
    shirt()
    onepiece()


mozori()