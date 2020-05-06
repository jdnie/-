from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os
import json
import re
import pandas as pd


def save_csv(df, data, fileName):
    new_df = pd.DataFrame(data)
    df = pd.concat([new_df, df])
    df.to_csv(fileName, index=0)


def get_second_house(driver, url, start_page=1, ed_page=10000):
    filename = './secondary_houses.csv'
    df = pd.read_csv(filename)
    scgpshsj = df['挂牌时间'][0]

    dump_data = {
        '房源核验统一编码':[],
        '所属城区':[],
        '小区':[],
        '面积':[],
        '委托价格':[],
        '均价':[],
        '挂牌时间':[]
    }

    try:
        for i in range(start_page, ed_page):
            newurl = url % i
            driver.get(newurl)
            print(newurl)
            u = driver.page_source
            soup = BeautifulSoup(u, "html5lib")
            if not hasattr(soup.pre, 'string'):
                print('dump %d page failed, try again!' % i)
                driver.get(newurl)
                u = driver.page_source
                soup = BeautifulSoup(u)
                if not hasattr(soup.pre, 'string'):
                    print('dump %d page failed again, not try!' % i)
                    continue
                else:
                    print('dump %d page success' % i)
            else:
                print('dump %d page success' % i)
            data = json.loads(soup.text)
            list = data['list']
            print(list[0]['scgpshsj'])
            for item in list:
                dump_data['房源核验统一编码'].append(item['fwtybh'])
                dump_data['所属城区'].append(item['cqmc'])
                dump_data['小区'].append(item['xqmc'])
                dump_data['面积'].append(item['jzmj'])
                dump_data['委托价格'].append(item['wtcsjg'])
                dump_data['均价'].append(int(item['wtcsjg']*10000/item['jzmj']))
                dump_data['挂牌时间'].append(item['scgpshsj'])
                if item['scgpshsj'] == scgpshsj:
                    save_csv(df, dump_data, filename)
                    return
    except:
        save_csv(df, dump_data, filename)

    save_csv(df, dump_data, filename)


if __name__=="__main__":
    url = 'http://jjhygl.hzfc.gov.cn/webty/WebFyAction_getGpxxSelectList.jspx?' \
          'gply=&wtcsjg=&jzmj&ordertype&fwyt&hxs&havepic&xzqh&secondxzqh&starttime&endtime&keywords&' \
          'page=%d&xqid=0&signid=ff80808166484c980166486b4e0b0023&' \
          'threshold=ff80808166484c980166486b4e0b0021&salt=ff80808166484c980166486b4e0b0022&' \
          'nonce=0&hash=0448c9b2298cc81d7e0b7a2ab77fcd9261f956537b0939664985b08a1bc4ce20'
    # driver = webdriver.PhantomJS()
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    get_second_house(driver, url, 1, ed_page=10000)
    driver.quit()
    # os.system('pause')  # windows