# job51-crawl
> 可爬取51job.com 网站上的所有城市的招聘信息，并将数据保存至数据库，利用scrapy框架
PS: 不提供长期支持，仅用于学习交流，By Amos

## 使用

1.修改配置
修改 `setting.py` 文件中的 `CRAWL_ALL_CITYS`,`CRAWL_CITY_LIST` 可自定义需要爬取的城市
```
CRAWL_ALL_CITYS = True #则为全部爬取，为真时忽略CRAWL_CITY_LIST
CRAWL_CITY_LIST = ['珠海','广州','深圳']
```

<br>

修改 `setting.py` 文件中的 `REDIS_URL` 制定你自己的redis数据库地址
```
REDIS_URL = 'redis://yourusername:redispassword@hostaddress:port'
```

<br>

设置settings.py 文件中的CORE_NUMBER 来自定义多进程爬取开启核心数(ps:最好不大于电脑自身核心数)
> 效果等同于多机分布式爬取，但有cpu核心数限制，速度有限。
> 实测速度为 22万items =~ 22min  ，即大约 1万/1min ，当然还可以进行优化提高速度。

```
CORE_NUMBER = 3
```

 

所需软件及python库,基于python3.6
scrapy
scrapy-redis
pymongo
redis

软件：
redis
mongodb
python3.6




