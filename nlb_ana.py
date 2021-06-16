#! -*- coding:utf-8 -*-
import datetime
import time

import pymysql
import requests
from lxml import etree
from selenium import webdriver
import pyautogui

driver = webdriver.Chrome()

if __name__ == '__main__':

    for num in range(6,999):
        big_list = []

        f_num = '{0:05}'.format(num) # 输出格式00001   00002
        url = 'https://nlb.ninjal.ac.jp/headword/N.{0}/'.format(f_num)   # 直接到登录界面！

        time.sleep(10)

        driver.get(url)
        time.sleep(10)

        driver.find_element_by_xpath('//*[@id="tab2"]/a').click()
        time.sleep(10)


        html =driver.page_source
        selector = etree.HTML(html)
        time.sleep(10)
        top1 = selector.xpath('//*[@id="header"]/h2/text()')
        top2 = selector.xpath('//*[@id="F001"]/td[1]/div/text()')
        words = ["名词"]

        for i1, i2,i3 in zip(top1, top2,words):
            big_list.append((i1, i2,i3))
        connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                     db='nlb_A',
                                     charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        cursor.executemany('insert into nlb_as (k1,k2,k3) values (%s,%s,%s)', big_list)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
        print(big_list,'{0}'.format(f_num))








# #
# create table nlb_as(
# id int not null primary key auto_increment,
# k1 varchar(80) unique,
# k2 varchar(88) ,
# k3 varchar(88)
# ) engine=InnoDB  charset=utf8;
#
# drop table nlb_as;