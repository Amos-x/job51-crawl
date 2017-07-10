job51-crawl
可爬取51job.com 网站上的所有城市的招聘信息，并将数据保存至数据库，利用scrapy框架

使用方法：
修改设置后，运行run.py即可

修改 setting.py 文件中的 CRAWL_ALL_CITYS,CRAWL_CITY_LIST 可自定义需要爬取的城市
example:
 CRAWL_ALL_CITYS = True #则为全部爬取，为真时忽略CRAWL_CITY_LIST
 CRAWL_CITY_LIST = ['珠海','广州','深圳']

修改 setting。py 文件中的 REDIS_URL 制定你自己的redis数据库地址
 REDIS_URL = 'redis://yourusername:redispassword@hostaddress:port'
 example：
 REDIS_URL = 'redis://root:123456@192.168.0.2:6379'

run.py 为模拟分布式爬取的单机多进程爬取启动文件,通过设置settings.py 文件中的CORE_NUMBER 来自定义开启核心数(ps:最好不大于电脑自身核心数)
CORE_NUMBER = 3

效果等同于多机分布式爬取，但有cpu核心数限制，速度有限。
实测速度为 22万items =~ 22min  ，即大约 1万/1min ，当然还可以进行优化提高速度。

 仅用于学习交流，By Amos

所需软件及python库,基于python3.6
scrapy
scrapy-redis
pymongo
redis

软件：
redis
mongodb
python3.6




