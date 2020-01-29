# coding=utf-8
import requests
from urllib.parse import urlencode
import random
import re
from lxml import etree
from bs4 import BeautifulSoup
import sys


class get_weixin():
    BASE_URL = "https://weixin.sogou.com/weixin?"
    params = {
              '_sug_type_': None,
              'sut': '3701',
              'lkt': '1, 1580180285154, 1580180285154',
              's_from': 'input',
              '_sug_': 'n',
              'type': '2',
              'sst0': '1580180285256',
              'ie': 'utf8',
              'w': '01019900',
              'dr': '1',
              }
    COOKIE0_HEADERS = {
            'Host': 'www.sogou.com',
            'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101Firefox/72.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }

    COOKIE1_HEADERS = {
            'Host': 'pb.sogou.com',
            'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101Firefox/72.0',
            'Accept': 'image/webp,*/*',
            'Accept - Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip,deflate,br',
            'Connection': 'keep-alive',
            'Referer': 'https://weixin.sogou.com/',
        }

    LIST_PAGE_HEADERS = {
            'Host': 'weixin.sogou.com',
            'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101Firefox/72.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept - Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip,deflate,br',
            'Connection': 'keep-alive',
            'Referer': 'https://weixin.sogou.com/',
        }

    COOKIE2_HEADERS = {
            'Host': 'weixin.sogou.com',
            'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101Firefox/72.0',
            'Accept': '*/*',
            'Accept - Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip,deflate,br',
            'Connection': 'keep-alive',
        }

    APPROVAL_HEADERS = {
            'Host': 'weixin.sogou.com',
            'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101Firefox/72.0',
            'Accept': '*/*',
            'Accept - Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip,deflate,br',
            'Connection': 'keep-alive',
        }

    REDIRECT_HEADERS = {
                'Host': 'weixin.sogou.com',
                'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101Firefox/72.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept - Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                'Accept-Encoding': 'gzip,deflate,br',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
            }

    WEIXIN_HEADER = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
                "cache-control": "max-age=0",
                "user-agent": 'Mozilla/5.0(Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101Firefox/72.0',
            }

    def __init__(self, keyword, page = [1]):
        #self.PROXY = self.get_proxy()
        self.PROXY = None
        self.PROXY_IP = None
        self.params['query'] = keyword
        self.params['page'] = page
        self.main_url = self.BASE_URL + urlencode(self.params)
        self.cookie_params = {}

    def get_proxy(self):
        """
        获取代理
        :return: 代理的ip地址:端口号
        """
        response = requests.get("http://127.0.0.1:5000/get")
        self.PROXY = response.text

    def set_keyword(self, keyword):
        """
        设置搜索内容
        :param keyword: 关键词
        :return: None
        """
        self.params['query'] = keyword

    def get_proxy_id(self, use_proxy=True):
        """
        将端口信息转换为代理地址
        :param use_proxy:
        :return:
        """
        if use_proxy:
            if self.PROXY:
                self.PROXY_IP = {
                    "http": "http://" + self.PROXY
                }
                return True
            else:
                raise AttributeError("未获得代理")
        else:
            self.PROXY_IP = None

    def get_list_page(self, renew_proxy=False):
        if renew_proxy:
            self.PROXY = get_proxy()

        self.LIST_PAGE_HEADERS['Cookie'] =  'ABTEST={}; IPLOC={}; SUID={}; sct=1; weixinIndexVisited=1'.\
            format(self.cookie_params['ABTEST'], self.cookie_params['IPLOC'], self.cookie_params['SUID'])
        html = requests.get(self.main_url, headers=self.LIST_PAGE_HEADERS, proxies=self.PROXY_IP)
        if html.status_code == 200:
            html.encoding = 'utf-8'
            SetCookie = html.headers['Set-Cookie']
            self.cookie_params['SNUID'] = re.findall('SNUID=(.*?);', SetCookie, re.S)[0]
            return html, html.url
        else:
            fun_name = sys._getframe().f_code.co_name
            raise IOError("{}步骤连接失败，错误代码为".format(fun_name, html.status_code))


    def get_k_h(self, url):
        b = int(random.random() * 100) + 1

        a = url.find("url=")
        url = url + "&k=" + str(b) + "&h=" + url[a + 4 + 21 + b: a + 4 + 21 + b + 1]
        return url

    def get_linked_url(self, html):
        e_tree = etree.HTML(html.text)
        urls = ['https://weixin.sogou.com' + i for i in e_tree.xpath('//div[@class="img-box"]/a/@href')]
        return urls

    def get_cookie0(self):
        """
        获取基础cookies
        :return:
        """
        html = requests.get('https://weixin.sogou.com/', headers=self.COOKIE0_HEADERS, proxies=self.PROXY_IP)
        if html.status_code == 200:
            SetCookie = html.headers['Set-Cookie']
            self.cookie_params['IPLOC'] = re.findall('IPLOC=(.*?);', SetCookie, re.S)[0]
            self.cookie_params['SUID'] = re.findall('SUID=(.*?);', SetCookie, re.S)[0]
            self.cookie_params['ABTEST'] = re.findall('ABTEST=(.*?);', SetCookie, re.S)[0]
            return SetCookie
        else:
            fun_name = sys._getframe().f_code.co_name
            raise IOError("{}步骤连接失败，错误代码为".format(fun_name, html.status_code))


    def get_cookie1(self):
        """
        获取cookie: SUV
        :return:
        """
        self.COOKIE1_HEADERS['Cookie'] = 'IPLOC={}; SNUID={}'.format(self.cookie_params['IPLOC'], self.cookie_params['SUID'])

        url='https://pb.sogou.com/pv.gif?uigs_t=1580263145232&uigs_productid=vs_web&terminal=web&vstype=weixin&' \
            'pagetype=index&channel=index_pc&type=weixin_search_pc&wuid=&snuid=&uigs_uuid=1580263144641343&' \
            'login=0&uigs_refer='
        html = requests.get(url, headers= self.COOKIE1_HEADERS, proxies=self.PROXY_IP)

        if html.status_code == 200:
            SetCookie = html.headers['Set-Cookie']
            self.cookie_params['SUV'] = re.findall('SUV=(.*?);', SetCookie, re.S)[0]
            return SetCookie
        else:
            fun_name = sys._getframe().f_code.co_name
            raise IOError("{}步骤连接失败，错误代码为".format(fun_name, html.status_code))

    def get_cookie2(self):
        """
        获取：JSESSIONID
        :return:
        """
        url = "https://weixin.sogou.com/websearch/wexinurlenc_sogou_profile.jsp"
        self.COOKIE2_HEADERS['Referer'] = self.main_url
        self.COOKIE2_HEADERS['Cookie']= 'ABTEST={}; IPLOC={}; SUID ={}; SNUID={}; sct=1; weixinIndexVisited=1'.\
            format(self.cookie_params['ABTEST'], self.cookie_params['IPLOC'], self.cookie_params['SUID'],
            self.cookie_params['SNUID'])
        html = requests.get(url, headers=self.COOKIE2_HEADERS, proxies=self.PROXY_IP)

        if html.status_code == 200:
            SetCookie = html.headers['Set-Cookie']
            self.cookie_params['JSESSIONID'] = re.findall('JSESSIONID=(.*?);', SetCookie, re.S)[0]
            return SetCookie
        else:
            fun_name = sys._getframe().f_code.co_name
            raise IOError("{}步骤连接失败，错误代码为".format(fun_name, html.status_code))


    def get_uuid(self, html):
        uuid = re.findall('var uuid = "(.*?)";', html.text, re.S)[0]
        return uuid

    def output_method(self, html_input, *args, **kwargs):
        """
        输出方法
        获得文章正文所有的文字
        :param html: 目标网页的requests返回对象
        :param args:
        :param kwargs:
        :return:
        """
        url_index = kwargs["url_index"]
        encoding = kwargs["encoding"]
        html = etree.HTML(html_input.text)
        html_input.encoding = encoding
        title = html.xpath('//meta[@property="og:title"]/@content')[0]
        soup = BeautifulSoup(html_input.text, 'lxml')
        text_content = title + "\r\n" + soup.find("div", {"id": "js_content"}).get_text()

        with open("data{}.txt".format(url_index), "w+", encoding="utf-8") as f:
            f.write(text_content)
            f.write("\r\n")

    def get_data(self, use_proxy = False):
        """
        爬取内容
        :param use_proxy: 是否使用代理
        :return:
        """
        if use_proxy:
            try:
                self.get_proxy()
                self.get_proxy_id()
            except Exception as e:
                print(e)
        try:
            self.get_cookie0()
            self.get_cookie1()
            html, refer_url = self.get_list_page()
            uuid = self.get_uuid(html)
            self.get_cookie2()
        except IOError as e:
            print(e)
            if use_proxy:
                self.get_data(use_proxy=True)
        except Exception as e:
            print(e)
            return None
        else:
            print("成功获取cookies")
        approve_url = "https://weixin.sogou.com/approve?uuid={}&token=undefined&from=outer".format(uuid)

        self.APPROVAL_HEADERS['Referer'] = refer_url
        self.APPROVAL_HEADERS['Cookie'] = 'ABTEST={}; IPLOC={}; JSESSIONID={}; sct=1; SNUID={}; SUID={};' \
                                          ' SUV={}; weixinIndexVisited=1'.format(self.cookie_params['ABTEST'], self.cookie_params['IPLOC'], self.cookie_params['JSESSIONID'],
                                        self.cookie_params['SUID'], self.cookie_params['SNUID'], self.cookie_params['SUV'])
        urls = self.get_linked_url(html)

        for url_index in range(len(urls)):
            print("正在处理第{}篇".format(url_index+1))
            url = self.get_k_h(urls[url_index])
            approve = requests.get(approve_url, headers=self.APPROVAL_HEADERS, proxies=self.PROXY_IP)
            self.REDIRECT_HEADERS['Referer'] = refer_url
            self.REDIRECT_HEADERS['Cookie'] = 'ABTEST={}; IPLOC={}; JSESSIONID={}; sct=1; SNUID={}; SUID={}; SUV={}; ' \
                                           'weixinIndexVisited=1'.format(self.cookie_params['ABTEST'], self.cookie_params['IPLOC'], self.cookie_params['JSESSIONID'],
                                            self.cookie_params['SUID'], self.cookie_params['SNUID'], self.cookie_params['SUV'])
            response_for_getting = requests.get(url, headers=self.REDIRECT_HEADERS, proxies = self.PROXY_IP)
            url_fragment = re.findall("url \+= '(.*?)'", response_for_getting.text, re.S)
            data_url = ''
            for i in url_fragment:
                data_url += i

            response_data = requests.get(data_url, headers=self.WEIXIN_HEADER)
            self.output_method(response_data, url_index=url_index, encoding="utf-8")



if "__main__" == __name__:
    test = get_weixin('虚构推理', 2)
    test.get_data(use_proxy=True)

