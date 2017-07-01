import os
from multiprocessing import Process

class scheduler(object):

    @staticmethod
    def crawl():
        os.system('scrapy crawl gd_job')

    def run(self):
        process1 = Process(target=scheduler.crawl)
        process2 = Process(target=scheduler.crawl)
        process3 = Process(target=scheduler.crawl)
        process1.start()
        process2.start()
        process3.start()

if __name__ == '__main__':
    r = scheduler()
    r.run()