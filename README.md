# job51-crawl


# 修改 setting.py 文件中的 CITYNUM_LIST 可自定义需要爬取的城市,城市编号需自己去job51官网上查看请求信息
# CITYNUM_LIST = []
# example:
# CITYNUM_LIST = ['030200','040000','030500']


# 修改 setting。py 文件中的 REDIS_URL 制定你自己的redis数据库地址
# REDIS_URL = 'redis://yourusername:redispassword@hostaddress:port'
# example：
# REDIS_URL = 'redis://root:123456@192.168.0.2:6379'


# run.py 为模拟分布式爬取的单机多进程爬取启动文件,通过设置settings.py 文件中的CORENUM 来自定义开启核心数(ps:最好不大于电脑自身核心数)，启动方式：
# CORENUM = 3
# python run.py （处于文件目录下）


# 效果等同于多机分布式爬取，但有cpu核心数限制，速度有限。
# 实测速度为 22万items =~ 22min  ，即大约 1万/1min ，当然还可以进行优化提高速度。


# 仅用于学习交流，By Amos


# 所需软件及python库,基于python3.6
scrapy
scrapy-redis
pymongo
redis

软件：
redis
mongodb
python3.6




