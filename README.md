# PythonProject
some small python project

## spider_me
主要是爬虫抓取程序。

### baike_spider
一个百度百科页面的抓取程序，根据一个初始的url，找到这个url相关的所有url，抓取这些url对应页面的url、title和summary，使用的是request和BeautifulSoup。代码来源: http://www.imooc.com/learn/563
url_manager：主要负责url的管理，包括新获取页面中包含的所有页面需要存入set（选择set因为可以自动去重），已经访问过的页面需要删除等
html_downloader：主要负责通过url拉取html页面
html_parser：主要负责html页面的解析，需要抓取的内容需要使用关键字class_或者id等获取，也可以通过正则表达式获取
html_outputer：主要负责将爬取的数据写入文件中
spider_main:主程序，控制流程和初始url
output.html：输出文件，输出抓取的数据内容

### teacherInfo_baike
20171022：根据baike_spider改的（将对多个url的操作改成针对一个url，不循环遍历相关的url），目前的功能是对于输入的很多姓名，一一抓取他们百科页面的内容，目前是对整个百度百科页面（main-content）的抓取，使用的是request和BeautifulSoup。如果后续需要只抓取基本信息等，需要重新解析html，若需要获取研究内容等，因为他们没有独立的label，因此目前的打算是将整个页面内容爬取，再根据关键字等定位

### teacherInfo_zhilifang
智立方作者搜索网址如下：http://buidea.com:9001/writer/WriterSearch.aspx
主要改动及原因：在teacherInfo_baike的基础上将BeautifulSoup改成了使用lxml，主要是BeautifulSoup定位时只能使用class_，id等关键字或者正则表达式定位，比较难，而lxml可以使用Xpath定位，简单
主要完成功能：根据作者姓名和学校联合搜索，爬取搜索页面的第一个查询结果的姓名、作品数、被引量、H指数、学校、研究主题
主要使用的request和lxml（可以使用Xpath定位html，非常方便）
