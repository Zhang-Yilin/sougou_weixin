# sougou_weixin
搜狗微信搜索爬虫


搜狗微信搜索获得微信公众号文章

最近学习爬虫，看了点视频教程(有点老)，发现上面的爬虫都不能用了，想着不会反爬虫跟不会爬虫没什么区别，就写了个爬虫练习了一下

研究流程：1.发现教程的爬虫用不了了，打开微信公众号文章需要重定向，直接点href的连接就进反爬虫页面；抓包发现发的url后面加了k和h，返回的包里有微信的url，可以直接点，发送的url里有个uuid，能从搜索列表页面里面找到，直接用就行。 2.找了原网站，最下面有段js，生成了k和h，问了一下，用python重构了一下，生成了k和h。但是用requests连还是不行。 3.可能是cookie有问题，清了cookie，从各个包里招set cookie，最后还差一个PHPSESSION之类的cookie，但是能连上。 4.挨个发包，搞到cookie，从response里找到uuid，再把js生成的k和h加上，发一个approve和一个请求微信url的包，就能弄到微信的url了。 5.连了个自己的代理池
