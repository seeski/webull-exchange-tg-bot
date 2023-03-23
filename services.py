import time
import os
from datetime import datetime
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from lexicon import LEXICON as lex


def create_info_image(paths):

    if len(paths) == 1:
        return paths[0]


    if len(paths) == 3:
        result = Image.new('RGB', (1354, 184), color='white')
        for index, file in enumerate(paths):
            path = os.path.expanduser(file)
            img = Image.open(path)
            x = index * 452
            y = 0
            w, h = img.size
            result.paste(img, (x, y, x + w, y + h))
            print(path, (x, y, x + w, y + h))

        result.save(os.path.expanduser('final.png'))

        return 'final.png'

    if len(paths) == 6:
        result = Image.new('RGB', (1354, 369), color='white')
        for index, file in enumerate(paths):
            path = os.path.expanduser(file)
            img = Image.open(path)
            x = index // 2 * 452
            y = index % 2 * 186
            w, h = img.size
            result.paste(img, (x, y, x + w, y + h))
            print(path, (x, y, x + w, y + h))

        result.save(os.path.expanduser('final.png'))

        return 'final.png'


def get_info(tickers):
    # if len(ticker.split('-')) == 1:
    #     ticker = f'nasdaq-{ticker}'
    service = Service('/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service=service)

    tickers = tickers.split(', ')

    paths = []
    for index, ticker in enumerate(tickers):
        if len(ticker.split('-')) == 1:
            ticker_url = f'nasdaq-{ticker}'
        else:
            ticker_url = ticker

        driver.get(f'https://www.webull.com/quote/{ticker_url}')
        # time.sleep(3)
        info = driver.find_element(by=By.XPATH, value='/html/body/div[3]/section/div[1]')
        info.screenshot(f'info{index}.png')
        img = Image.open(f'info{index}.png')
        cropped = img.crop(box=(50, 50, 500, 234))
        cropped.save(fp=f'cropped{index}.png')
        paths.append(f'cropped{index}.png')


    return create_info_image(paths)


def get_caption(tickers):
    temp = datetime.now()
    now = temp.strftime("%d/%m/%Y %H:%M:%S")
    caption = lex['info'].format(tickers) + now

    return caption
