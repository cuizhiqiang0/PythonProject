import GrabWeb.spider_me.teacherInfo_zhilifang.html_downloader as html_downloader
import GrabWeb.spider_me.teacherInfo_zhilifang.html_outputer as html_outputer
import GrabWeb.spider_me.teacherInfo_zhilifang.html_parser as html_parser
import urllib.parse as parse

class SpiderMain(object):

    # 初始化
    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    # 抓取
    def craw(self, urls):
        count = 1
        for url in urls:
            try:
                print("craw", count, ": ", url)
                print('test1')
                html_cont = self.downloader.download(url)
                print('test2')
                new_data = self.parser.parse(html_cont)
                print('new_data: ', new_data)
                self.outputer.collect_data(new_data)
            except:
                print('craw failed')
            count = count + 1
        self.outputer.output_html()

if __name__ == "__main__":
    queries = {"周傲英, 华东师范大学", "金澈清, 华东师范大学"}
    # print('queries[0]', queries.pop())
    # print('queries[1]', queries.pop())
    urls = set()
    for query in queries:
        name = query.split(',')[0]
        university = query.split(',')[1]
        print(name, " ", university)
        # new_url = "https://baike.baidu.com/item/"+parse.quote(name)
        new_url = "http://buidea.com:9001/writer/writersearch.aspx?invokemethod=search&q=%7B"+parse.quote("\"")\
                  +"search"+parse.quote("\"")+"%3A"+parse.quote("\"")+parse.quote(name)+"%20"\
                  +parse.quote(university)+parse.quote("\"")+"%2C"+parse.quote("\"")+"sType"\
                  +parse.quote("\"")+"%3A"+parse.quote("\"")+"writer"+parse.quote("\"")+"%7D&"
        #new_url = "http://buidea.com:9001/writer/writersearch.aspx?invokemethod=search&q=%7B%22search%22%3A%22%E5%91%A8%E5%82%B2%E8%8B%B1%20%E5%8D%8E%E4%B8%9C%E5%B8%88%E8%8C%83%E5%A4%A7%E5%AD%A6%22%2C%22sType%22%3A%22writer%22%7D&"
        urls.add(new_url)
    print(urls)
    obj_spider = SpiderMain()
    obj_spider.craw(urls)
