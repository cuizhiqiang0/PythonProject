from bs4 import BeautifulSoup
from lxml import etree
import urllib
import re

# HtmlParser(object)的功能是：负责解析html文本，取得页面的title，summary，页面中的urls

class HtmlParser2(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_data = self.get_new_data(page_url, soup)
        return new_data

    def get_new_databeiyogn(self, page_url, soup):
        res_data = {}
        # url
        res_data['url'] = page_url
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find("h1")
        res_data['title'] = title_node.get_text()
        # <div class="lemma-summary" label-module="lemmaSummary">
        # summary_node = soup.find('div', class_="lemma-summary")
        # res_data['summary'] = summary_node.get_text()
        return res_data

    def get_new_data(self, page_url, soup):
        res_data = {}
        # url
        # res_data['url'] = page_url
        div_node = soup.find('div', class_='search_list type_writer')
        res_data = div_node.get_text()
        return res_data


class HtmlParser(object):

    def parse(self, html_cont):
        res_data = {}
        if html_cont is None:
            print("html count:", html_cont)
            return
        # soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        tree = etree.HTML(html_cont)
        print('tree: ', tree)
        # /html/body/div[2]/div[2]/div[1]/div[1]
        #信息依次为：姓名、作品数、被引量、H指数、供职机构、研究主题
        print('ddad1')
        node_XingMing = tree.xpath("//html//body/div[@class='body r3']/div[@class='main']/div[@class='m']/div[2]/dl/dt[@class='writer']/a/span/text()")
        print('ddad2')
        ZuoPinShu = tree.xpath("//html/body/div[@class='body r3']/div[@class='main']/div[@class='m']/div[@class='search_list type_writer']/dl/dd[@class='data hide3']/span[@class='zps']/text()")
        print('ddad3', ZuoPinShu)
        # ZuoPinShu返回的是一个list
        node_ZuoPinShu = ZuoPinShu[0].split(u'：')[1]
        print('ddad4', node_ZuoPinShu)
        BeiYinLiang = tree.xpath("//html/body/div[@class='body r3']/div[@class='main']/div[@class='m']/div[@class='search_list type_writer']/dl/dd[@class='data hide3']/span[@class='bys']/text()")
        print('ddad5', BeiYinLiang)
        node_BeiYinLiang = BeiYinLiang[0].split(u'：')[1]
        print('ddad6')
        HZhiShu = tree.xpath("//html/body/div[@class='body r3']/div[@class='main']/div[@class='m']/div[@class='search_list type_writer']/dl/dd[@class='data hide3']/span[@class='hzs']/text()")
        print('ddad7')
        node_HZhiShu = HZhiShu[0].split(u'：')[1]
        print('ddad8')
        node_GongZhiJiGou = tree.xpath("//html//body//div[@class='body r3']//div[@class='main']//div[@class='m']//div[@class='search_list type_writer']//dl//dd[@class='organ hide3 hide2']/span/text()")
        print('ddad9')
        node_YanJiuZhuTi = tree.xpath("//html//body//div[@class='body r3']//div[@class='main']//div[@class='m']//div[@class='search_list type_writer']//dl//dd[@class='subject hide3 hide2']/text()")
        print('node_XingMing: ', node_XingMing, "node_ZuoPinShu: ", node_ZuoPinShu, "node_BeiYinLiang: ", node_BeiYinLiang,
              "node_HZhiShu: ", node_HZhiShu, "node_GongZhiJiGou", node_GongZhiJiGou, " node_YanJiuZhuTi: ", node_YanJiuZhuTi)
        res_data['node_XingMing'] = node_XingMing
        res_data['node_ZuoPinShu'] = node_ZuoPinShu
        res_data['node_BeiYinLiang'] = node_BeiYinLiang
        res_data['node_HZhiShu'] = node_HZhiShu
        res_data['node_GongZhiJiGou'] = node_GongZhiJiGou[0]
        res_data['node_YanJiuZhuTi'] = node_YanJiuZhuTi
        return res_data





